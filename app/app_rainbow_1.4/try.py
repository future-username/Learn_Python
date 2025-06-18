DEFAULT_FIGURES: dict[str, any] = {
    "Линия": (),
    "Прямоугольник": (),
    "Овал": (),
    "Елочка": ()  # Добавляем новую фигуру
}


class Canvas(tk.Canvas, ICanvas, IEventHandler):
    """Холст для рисования фигур."""
    def __init__(self, master: tk.Widget, controller: Optional['IController'] = None, **kwargs):
        super().__init__(master, bg=kwargs.pop('bg', DEFAULT_CANVAS_BG), **kwargs)
        self.drawing_color: str = DEFAULT_DRAWING_COLOR_HEX
        self.active_figure: str = DEFAULT_ACTIVE_FIGURE
        self.controller: Optional['IController'] = controller
        
        self._start_x: Optional[int] = None
        self._start_y: Optional[int] = None
        self._current_shape_id: Optional[int] = None # ID временной фигуры при перетаскивании

        self.bind("<ButtonPress-1>", self.on_press)
        self.bind("<B1-Motion>", self.on_drag)
        self.bind("<ButtonRelease-1>", self.on_release)

    def set_drawing_color(self, color_hex: str):
        self.drawing_color = color_hex

    def set_active_figure(self, figure_name: str):
        self.active_figure = figure_name

    def on_press(self, event: tk.Event):
        self._start_x = event.x
        self._start_y = event.y
        # Для линий начинаем рисовать сразу (как временную)
        if self.active_figure == FIGURE_LINE:
            self._current_shape_id = self.create_line(
                self._start_x, self._start_y, event.x, event.y, 
                fill=self.drawing_color, width=2, tags="temp_shape"
            )

    def on_drag(self, event: tk.Event):
        if self._start_x is None or self._start_y is None:
            return

        if self._current_shape_id:
            self.delete(self._current_shape_id)
            self._current_shape_id = None

        # Dictionary mapping figure types to their creation functions
        shape_creators = {
            FIGURE_LINE: self.create_line,
            FIGURE_RECTANGLE: self.create_rectangle,
            FIGURE_OVAL: self.create_oval,
            FIGURE_TREE: lambda *args, **kwargs: self.create_rectangle(*args, dash=(4,2), **kwargs)
        }

        # Common parameters for all shapes
        common_params = {
            'tags': "temp_shape",
            'width': 2
        }

        # Get the appropriate creator function
        creator = shape_creators.get(self.active_figure)
        if not creator:
            return

        # Add specific parameters based on shape type
        specific_params = {
            'fill' if self.active_figure == FIGURE_LINE else 'outline': self.drawing_color
        }

        # Create the shape with combined parameters
        self._current_shape_id = creator(
            self._start_x, self._start_y, event.x, event.y,
            **common_params,
            **specific_params
        )

    def on_release(self, event: tk.Event):
        if self._current_shape_id: # Удаляем временную фигуру
            self.delete(self._current_shape_id)
            self._current_shape_id = None

        if self._start_x is not None and self._start_y is not None and self.controller:
            end_x, end_y = event.x, event.y
            # Игнорируем клик без перемещения для фигур, кроме, возможно, точки
            if self._start_x == end_x and self._start_y == end_y and self.active_figure != "Точка":
                self._start_x, self._start_y = None, None
                return

            coordinates = ((self._start_x, self._start_y), (end_x, end_y))
            self.controller.handle_draw_shape_request(coordinates, self.active_figure)
        
        self._start_x = None
        self._start_y = None

    def draw_shape(self, coordinates: Tuple[Tuple[int, int], Tuple[int, int]], figure_type: str):
        (x1, y1), (x2, y2) = coordinates
        fill_color = ""
        # Для елочки заливка может быть применена к стволу или частям кроны
        ask_fill = figure_type not in [FIGURE_LINE]
        
        if ask_fill:
            if messagebox.askyesno("Заливка фигуры", f"Залить {figure_type.lower()} выбранным цветом?", parent=self):
                fill_color = self.drawing_color

        if figure_type == FIGURE_LINE:
            self.create_line(x1, y1, x2, y2, fill=self.drawing_color, width=2)
        elif figure_type == FIGURE_RECTANGLE:
            self.create_rectangle(x1, y1, x2, y2, outline=self.drawing_color, fill=fill_color, width=2)
        elif figure_type == FIGURE_OVAL:
            self.create_oval(x1, y1, x2, y2, outline=self.drawing_color, fill=fill_color, width=2)
        elif figure_type == FIGURE_TREE:
            self._draw_christmas_tree(x1, y1, x2, y2, self.drawing_color, fill_color)
        # elif figure_type == "Полилиния":
        #    self.create_polygon(coordinates_tuple, outline=self.drawing_color, fill=fill_color, width=2)

    def _draw_christmas_tree(self, x1: int, y1: int, x2: int, y2: int, outline_color: str, fill_color: str):
        """Рисует елочку на холсте."""
        # Определяем базовые размеры и положение елочки
        # Елочка будет вписана в прямоугольник (x1,y1) - (x2,y2)
        # Нормализуем координаты, чтобы x1 < x2 и y1 < y2
        min_x, max_x = min(x1, x2), max(x1, x2)
        min_y, max_y = min(y1, y2), max(y1, y2)

        width = max_x - min_x
        height = max_y - min_y

        if width == 0 or height == 0: return # Нечего рисовать

        # Ствол (коричневый по умолчанию, если не выбран другой цвет для заливки)
        trunk_width = width / 5
        trunk_height = height / 4
        trunk_x1 = min_x + (width - trunk_width) / 2
        trunk_y1 = max_y - trunk_height
        trunk_x2 = trunk_x1 + trunk_width
        trunk_y2 = max_y
        # Если есть fill_color, используем его для ствола, иначе - коричневый
        actual_trunk_fill = fill_color if fill_color else "#A0522D" # SaddleBrown
        self.create_rectangle(trunk_x1, trunk_y1, trunk_x2, trunk_y2, 
                                outline=outline_color, fill=actual_trunk_fill, width=2)

        # Крона (три треугольника)
        crown_base_y = trunk_y1
        crown_segment_height = (crown_base_y - min_y) / 3

        # Нижний ярус кроны
        poly1_coords = [
            min_x, crown_base_y, 
            max_x, crown_base_y,
            min_x + width / 2, crown_base_y - crown_segment_height
        ]
        self.create_polygon(poly1_coords, outline=outline_color, fill=fill_color if fill_color else "", width=2)

        # Средний ярус кроны
        poly2_coords = [
            min_x + width / 6, crown_base_y - crown_segment_height * 0.8, # Немного выше и уже
            max_x - width / 6, crown_base_y - crown_segment_height * 0.8,
            min_x + width / 2, min_y + crown_segment_height * 1.2 # Вершина чуть ниже
        ]
        self.create_polygon(poly2_coords, outline=outline_color, fill=fill_color if fill_color else "", width=2)

        # Верхний ярус кроны (верхушка)
        poly3_coords = [
            min_x + width / 3, min_y + crown_segment_height * 1.5, # Еще уже
            max_x - width / 3, min_y + crown_segment_height * 1.5,
            min_x + width / 2, min_y
        ]
        self.create_polygon(poly3_coords, outline=outline_color, fill=fill_color if fill_color else "", width=2)