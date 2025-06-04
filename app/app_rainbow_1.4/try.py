import tkinter as tk
from tkinter import messagebox
from typing import Optional, Tuple, Dict, Any # Убедитесь, что эти импорты есть
import math # Добавлен импорт math

# Предполагается, что эти константы определены где-то выше
# Например:
# DEFAULT_CANVAS_BG = "white"
# DEFAULT_DRAWING_COLOR_HEX = "black"
# DEFAULT_ACTIVE_FIGURE = "Линия"
# FIGURE_LINE = "Линия"
# FIGURE_RECTANGLE = "Прямоугольник"
# FIGURE_OVAL = "Овал"
# FIGURE_TREE = "Елочка"

# Также предполагается наличие интерфейсов ICanvas, IEventHandler, IController
# class ICanvas: pass
# class IEventHandler: pass
# class IController: pass

DEFAULT_FIGURES: Dict[str, Any] = {
    "Линия": (),
    "Прямоугольник": (),
    "Овал": (),
    "Елочка": () 
}


class Canvas(tk.Canvas, ICanvas, IEventHandler):
    """Холст для рисования фигур."""
    def __init__(self, master: tk.Widget, controller: Optional['IController'] = None, **kwargs):
        super().__init__(master, bg=kwargs.pop('bg', 'white'), **kwargs) # Используйте DEFAULT_CANVAS_BG если определен
        self.drawing_color: str = 'black' # Используйте DEFAULT_DRAWING_COLOR_HEX если определен
        self.active_figure: str = 'Линия' # Используйте DEFAULT_ACTIVE_FIGURE если определен
        self.controller: Optional['IController'] = controller
        
        self._start_x: Optional[int] = None
        self._start_y: Optional[int] = None
        self._current_shape_id: Optional[int] = None # ID временной фигуры при перетаскивании

        self.bind("<ButtonPress-1>", self.on_press)
        self.bind("<B1-Motion>", self.on_drag)
        self.bind("<ButtonRelease-1>", self.on_release)

    def _get_oval_points(self, x1: int, y1: int, x2: int, y2: int, segments: int = 36) -> list[float]:
        """Генерирует координаты точек для полигона, аппроксимирующего овал."""
        points = []
        # Нормализуем координаты
        rx1, ry1 = min(x1, x2), min(y1, y2)
        rx2, ry2 = max(x1, x2), max(y1, y2)

        center_x = (rx1 + rx2) / 2
        center_y = (ry1 + ry2) / 2
        radius_x = (rx2 - rx1) / 2
        radius_y = (ry2 - ry1) / 2

        if radius_x == 0 and radius_y == 0: # Точка
            return [rx1, ry1, rx1+1, ry1, rx1+1, ry1+1, rx1, ry1+1, rx1, ry1] # Маленький квадрат для точки
        if radius_x == 0 or radius_y == 0: # Линия (вертикальная или горизонтальная)
            # Возвращаем прямоугольник, который будет выглядеть как линия при width > 0
            return [rx1, ry1, rx2, ry1, rx2, ry2, rx1, ry2, rx1, ry1]

        for i in range(segments):
            angle = (2 * math.pi / segments) * i
            x = center_x + radius_x * math.cos(angle)
            y = center_y + radius_y * math.sin(angle)
            points.extend([x, y])
        # Замыкаем полигон, добавляя первую точку в конец, если она еще не там
        if points and (points[0] != points[-2] or points[1] != points[-1]):
             points.extend([points[0], points[1]])
        return points

    def set_drawing_color(self, color_hex: str):
        self.drawing_color = color_hex

    def set_active_figure(self, figure_name: str):
        self.active_figure = figure_name

    def on_press(self, event: tk.Event):
        self._start_x = event.x
        self._start_y = event.y
        # Для линий начинаем рисовать сразу (как временную)
        # Предполагаем, что FIGURE_LINE определена как "Линия"
        if self.active_figure == "Линия": # Замените "Линия" на FIGURE_LINE
            self._current_shape_id = self.create_polygon(
                [self._start_x, self._start_y, event.x, event.y],
                fill="",  # Линии не заливаются
                outline=self.drawing_color,
                width=2,
                tags="temp_shape"
            )

    def on_drag(self, event: tk.Event):
        if self._start_x is None or self._start_y is None:
            return

        if self._current_shape_id:
            self.delete(self._current_shape_id)
            self._current_shape_id = None

        temp_shape_params = {
            'tags': "temp_shape",
            'width': 2,
            'outline': self.drawing_color,
            'fill': ""  # Временные фигуры - это контуры, они не заливаются
        }
        
        # Предполагаем, что FIGURE_LINE, FIGURE_RECTANGLE, FIGURE_OVAL, FIGURE_TREE определены
        # Замените строки на соответствующие переменные констант
        active_fig = self.active_figure 

        coords: list[float] = []
        specific_params = {}

        if active_fig == "Линия": # FIGURE_LINE
            coords = [self._start_x, self._start_y, event.x, event.y]
        elif active_fig == "Прямоугольник": # FIGURE_RECTANGLE
            coords = [self._start_x, self._start_y, event.x, self._start_y, 
                      event.x, event.y, self._start_x, event.y, 
                      self._start_x, self._start_y]
        elif active_fig == "Овал": # FIGURE_OVAL
            coords = self._get_oval_points(self._start_x, self._start_y, event.x, event.y)
        elif active_fig == "Елочка": # FIGURE_TREE (рисуем ограничивающий прямоугольник)
            coords = [self._start_x, self._start_y, event.x, self._start_y, 
                      event.x, event.y, self._start_x, event.y, 
                      self._start_x, self._start_y]
            specific_params['dash'] = (4, 2)
        else:
            return

        if not coords: # Если _get_oval_points вернул пустой список для вырожденного овала
            return
            
        self._current_shape_id = self.create_polygon(coords, **temp_shape_params, **specific_params)

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
        # Предполагаем, что FIGURE_LINE определена
        ask_fill = figure_type != "Линия" # Замените "Линия" на FIGURE_LINE
        
        if ask_fill:
            if messagebox.askyesno("Заливка фигуры", f"Залить {figure_type.lower()} выбранным цветом?", parent=self):
                fill_color = self.drawing_color

        # Предполагаем, что FIGURE_LINE, FIGURE_RECTANGLE, FIGURE_OVAL, FIGURE_TREE определены
        # Замените строки на соответствующие переменные констант
        if figure_type == "Линия": # FIGURE_LINE
            self.create_polygon([x1, y1, x2, y2], outline=self.drawing_color, fill="", width=2)
        elif figure_type == "Прямоугольник": # FIGURE_RECTANGLE
            poly_coords = [x1, y1, x2, y1, x2, y2, x1, y2, x1, y1]
            self.create_polygon(poly_coords, outline=self.drawing_color, fill=fill_color, width=2)
        elif figure_type == "Овал": # FIGURE_OVAL
            oval_coords = self._get_oval_points(x1, y1, x2, y2)
            if oval_coords: # Убедимся, что есть что рисовать
                self.create_polygon(oval_coords, outline=self.drawing_color, fill=fill_color, width=2)
        elif figure_type == "Елочка": # FIGURE_TREE
            self._draw_christmas_tree(x1, y1, x2, y2, self.drawing_color, fill_color)

    def _draw_christmas_tree(self, x1: int, y1: int, x2: int, y2: int, outline_color: str, fill_color: str):
        """Рисует елочку на холсте."""
        min_x, max_x = min(x1, x2), max(x1, x2)
        min_y, max_y = min(y1, y2), max(y1, y2)

        width = max_x - min_x
        height = max_y - min_y

        if width == 0 or height == 0: return

        trunk_width = width / 5
        trunk_height = height / 4
        trunk_x1 = min_x + (width - trunk_width) / 2
        trunk_y1 = max_y - trunk_height
        trunk_x2 = trunk_x1 + trunk_width
        trunk_y2 = max_y
        actual_trunk_fill = fill_color if fill_color else "#A0522D"
        
        trunk_coords = [trunk_x1, trunk_y1, trunk_x2, trunk_y1, 
                        trunk_x2, trunk_y2, trunk_x1, trunk_y2, 
                        trunk_x1, trunk_y1]
        self.create_polygon(trunk_coords, outline=outline_color, fill=actual_trunk_fill, width=2)

        crown_base_y = trunk_y1
        crown_segment_height = (crown_base_y - min_y) / 3

        if crown_segment_height <= 0: return # Нечего рисовать для кроны

        poly1_coords = [
            min_x, crown_base_y, 
            max_x, crown_base_y,
            min_x + width / 2, crown_base_y - crown_segment_height
        ]
        self.create_polygon(poly1_coords, outline=outline_color, fill=fill_color if fill_color else "", width=2)

        poly2_coords = [
            min_x + width / 6, crown_base_y - crown_segment_height * 0.8, 
            max_x - width / 6, crown_base_y - crown_segment_height * 0.8,
            min_x + width / 2, min_y + crown_segment_height * 1.2 
        ]
        self.create_polygon(poly2_coords, outline=outline_color, fill=fill_color if fill_color else "", width=2)

        poly3_coords = [
            min_x + width / 3, min_y + crown_segment_height * 1.5, 
            max_x - width / 3, min_y + crown_segment_height * 1.5,
            min_x + width / 2, min_y
        ]
        self.create_polygon(poly3_coords, outline=outline_color, fill=fill_color if fill_color else "", width=2)