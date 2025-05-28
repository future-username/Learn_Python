import tkinter as tk
from tkinter import colorchooser, messagebox
from typing import Dict, Tuple, Any, Optional, Callable, cast

# Предполагается, что файл app_rainbow_mvc_interfaces.py находится в том же каталоге
# или доступен через PYTHONPATH.
# Убираем точку для прямого импорта, если скрипт запускается из той же директории
from app_rainbow_mvc_interfaces import (
    IModel, IButtonColor, IButtonFigures, ICanvas,
    IView, IController, IApp, IEventHandler
)

# --- Constants ---
DEFAULT_WINDOW_TITLE = "Rainbow MVC App"
DEFAULT_WINDOW_GEOMETRY = "800x600"
DEFAULT_CANVAS_BG = "white"
DEFAULT_DRAWING_COLOR_NAME = "Черный"
DEFAULT_DRAWING_COLOR_HEX = "#000000"
DEFAULT_ACTIVE_FIGURE = "Линия"

DEFAULT_COLORS: Dict[str, str] = {
    "Красный": "#FF0000",
    "Оранжевый": "#FFA500",
    "Желтый": "#FFFF00",
    "Зеленый": "#00FF00",
    "Голубой": "#00FFFF",
    "Синий": "#0000FF",
    "Фиолетовый": "#800080",
    "Черный": "#000000",
    "Белый": "#FFFFFF",
    "Серый": "#808080",
}

DEFAULT_FIGURES: Dict[str, Any] = {
    "Линия": (),
    "Прямоугольник": (),
    "Овал": (),
    "Елочка": ()  # Добавляем новую фигуру
}

FIGURE_LINE = "Линия"
FIGURE_RECTANGLE = "Прямоугольник"
FIGURE_OVAL = "Овал"
FIGURE_TREE = "Елочка" # Новая константа для елочки

# --- Utility Functions ---
def get_text_color_for_bg(hex_color: str) -> str:
    """Определяет цвет текста (черный или белый) для лучшей читаемости на заданном фоне."""
    try:
        hex_color = hex_color.lstrip('#')
        if len(hex_color) != 6:
            return "black" # По умолчанию, если hex некорректен
        r, g, b = int(hex_color[0:2], 16), int(hex_color[2:4], 16), int(hex_color[4:6], 16)
        # Формула для расчета воспринимаемой яркости
        brightness = (r * 299 + g * 587 + b * 114) / 1000
        return "black" if brightness > 128 else "white"
    except ValueError:
        return "black" # По умолчанию при ошибке

# --- Model ---
class Model(IModel):
    """Модель данных приложения, хранит информацию о цветах и фигурах."""
    def __init__(self, colors: Optional[Dict[str, str]] = None, figures: Optional[Dict[str, Any]] = None):
        self._colors = colors if colors is not None else DEFAULT_COLORS.copy()
        self._figures = figures if figures is not None else DEFAULT_FIGURES.copy()

    def get_colors(self) -> Dict[str, str]:
        return self._colors

    def get_color_name(self, hex_code: str) -> str:
        for name, code in self._colors.items():
            if code.lower() == hex_code.lower():
                return name
        return "Неизвестный цвет"

    def get_figures(self) -> Dict[str, Any]:
        return self._figures

    def get_figure_params(self, name: str) -> Tuple:
        # В текущей реализации параметры фигур не используются, но интерфейс их предусматривает
        return self._figures.get(name, ())

# --- View Components ---
class CustomButton(tk.Button):
    """Базовый класс для кастомных кнопок с общей стилизацией."""
    def __init__(self, master: tk.Widget, **kwargs):
        super().__init__(master, relief=tk.RAISED, borderwidth=2, **kwargs)

class ButtonColor(CustomButton, IButtonColor):
    """Кнопка для выбора цвета."""
    def __init__(self, master: tk.Widget, color_hex: str, color_name: str, command: Callable[[str, str], None], **kwargs):
        super().__init__(master, text=color_name, bg=color_hex, 
                         command=lambda ch=color_hex, cn=color_name: command(ch, cn), **kwargs)
        self.color_hex = color_hex
        self.color_name = color_name
        self.config(fg=get_text_color_for_bg(color_hex))

    def show_color(self, label_widget: tk.Label, entry_widget: tk.Entry):
        """Обновляет виджеты для отображения информации о выбранном цвете."""
        label_widget.config(text=f"Цвет: {self.color_name}")
        entry_widget.delete(0, tk.END)
        entry_widget.insert(0, self.color_hex)
        entry_widget.config(bg=self.color_hex, fg=get_text_color_for_bg(self.color_hex))

class ButtonFigures(CustomButton, IButtonFigures):
    """Кнопка для выбора фигуры."""
    def __init__(self, master: tk.Widget, figure_name: str, figure_params: Tuple, command: Callable[[str], None], **kwargs):
        super().__init__(master, text=figure_name, command=lambda fn=figure_name: command(fn), **kwargs)
        self._figure_name = figure_name
        self._figure_params = figure_params

    def get_figure_name(self) -> str:
        return self._figure_name

    def get_figure_params(self) -> Tuple:
        return self._figure_params

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

        if self._current_shape_id: # Удаляем предыдущую временную фигуру
            self.delete(self._current_shape_id)
            self._current_shape_id = None

        if self.active_figure == FIGURE_LINE:
            self._current_shape_id = self.create_line(
                self._start_x, self._start_y, event.x, event.y, 
                fill=self.drawing_color, width=2, tags="temp_shape"
            )
        elif self.active_figure == FIGURE_RECTANGLE:
            self._current_shape_id = self.create_rectangle(
                self._start_x, self._start_y, event.x, event.y, 
                outline=self.drawing_color, width=2, tags="temp_shape"
            )
        elif self.active_figure == FIGURE_OVAL:
            self._current_shape_id = self.create_oval(
                self._start_x, self._start_y, event.x, event.y, 
                outline=self.drawing_color, width=2, tags="temp_shape"
            )
        elif self.active_figure == FIGURE_TREE:
            # Временное отображение елочки - можно просто рамку или упрощенную форму
            # Для простоты пока оставим как прямоугольник, но потом можно улучшить
            self._current_shape_id = self.create_rectangle(
                 self._start_x, self._start_y, event.x, event.y,
                 outline=self.drawing_color, dash=(4, 2), tags="temp_shape"
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

# --- View ---
class View(IView):
    """Представление (GUI) приложения."""
    def __init__(self, master: tk.Tk, title: str):
        self.master = master
        self.master.title(title)
        self.master.geometry(DEFAULT_WINDOW_GEOMETRY)
        self._controller: Optional[IController] = None

        self._setup_ui()

    def _setup_ui(self):
        """Инициализация и размещение элементов интерфейса."""
        # --- Frames ---
        main_controls_frame = tk.Frame(self.master, bd=2, relief=tk.GROOVE, padx=5, pady=5)
        main_controls_frame.pack(side=tk.LEFT, fill=tk.Y, padx=5, pady=5)

        self.canvas_frame = tk.Frame(self.master, bd=2, relief=tk.SUNKEN)
        self.canvas_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=5, pady=5)

        # --- Color Controls ---
        self.color_controls_frame = tk.LabelFrame(main_controls_frame, text="Цвета", padx=10, pady=10)
        self.color_controls_frame.pack(fill=tk.X, padx=5, pady=(0,10))
        
        self.color_buttons_frame = tk.Frame(self.color_controls_frame) # Отдельный фрейм для кнопок
        self.color_buttons_frame.pack(fill=tk.X)

        color_display_subframe = tk.Frame(self.color_controls_frame)
        color_display_subframe.pack(fill=tk.X, pady=(10,0))
        self.color_label = tk.Label(color_display_subframe, text="Цвет: ")
        self.color_label.pack(side=tk.LEFT, padx=(0,5))
        self.color_entry = tk.Entry(color_display_subframe, width=10, relief=tk.SUNKEN, bd=1)
        self.color_entry.pack(side=tk.LEFT)

        # --- Figure Controls ---
        self.figure_controls_frame = tk.LabelFrame(main_controls_frame, text="Фигуры", padx=10, pady=10)
        self.figure_controls_frame.pack(fill=tk.X, padx=5, pady=5)

        self.figure_buttons_frame = tk.Frame(self.figure_controls_frame) # Отдельный фрейм для кнопок
        self.figure_buttons_frame.pack(fill=tk.X)

        self.figure_label = tk.Label(self.figure_controls_frame, text=f"Фигура: {DEFAULT_ACTIVE_FIGURE}")
        self.figure_label.pack(fill=tk.X, pady=(10,0))

        # --- Canvas ---
        self.canvas = Canvas(self.canvas_frame, width=600, height=550) # controller будет установлен позже
        self.canvas.pack(fill=tk.BOTH, expand=True)

    def set_controller(self, controller: 'IController'):
        self._controller = controller
        # Важно: передаем контроллер холсту ПОСЛЕ его создания и ПОСЛЕ создания контроллера
        if isinstance(self.canvas, Canvas):
            self.canvas.controller = controller

    def create_color_buttons(self, colors: Dict[str, str]):
        if not self._controller:
            # print("Warning: Controller not set in View before creating color buttons.")
            return
        # Очищаем старые кнопки, если они есть (для возможного динамического обновления)
        for widget in self.color_buttons_frame.winfo_children():
            widget.destroy()
            
        for i, (name, hex_code) in enumerate(colors.items()):
            btn = ButtonColor(self.color_buttons_frame, color_hex=hex_code, color_name=name,
                              command=cast(Callable[[str, str], None], self._controller.handle_color_button_click),
                              width=10)
            # Размещаем кнопки в 2 колонки для компактности
            btn.grid(row=i // 2, column=i % 2, padx=2, pady=2, sticky=tk.EW)
        self.color_buttons_frame.columnconfigure((0,1), weight=1) # Растягивание колонок

    def create_figure_buttons(self, figures: Dict[str, Any]):
        if not self._controller:
            # print("Warning: Controller not set in View before creating figure buttons.")
            return
        for widget in self.figure_buttons_frame.winfo_children():
            widget.destroy()

        for i, (name, params) in enumerate(figures.items()):
            btn = ButtonFigures(self.figure_buttons_frame, figure_name=name, figure_params=params,
                                command=cast(Callable[[str], None], self._controller.handle_figure_button_click),
                                width=10)
            btn.grid(row=i // 1, column=i % 1, padx=2, pady=2, sticky=tk.EW) # В одну колонку
        self.figure_buttons_frame.columnconfigure(0, weight=1)

    def update_color_display(self, color_hex: str, color_name: str):
        self.color_label.config(text=f"Цвет: {color_name}")
        self.color_entry.delete(0, tk.END)
        self.color_entry.insert(0, color_hex)
        self.color_entry.config(bg=color_hex, fg=get_text_color_for_bg(color_hex))

    def update_figure_display(self, figure_name: str):
        self.figure_label.config(text=f"Фигура: {figure_name}")

    def set_drawing_color(self, color_hex: str):
        if isinstance(self.canvas, Canvas):
            self.canvas.set_drawing_color(color_hex)

    def draw_shape_on_canvas(self, coordinates: Tuple[Tuple[int, int], Tuple[int, int]], figure_type: str):
        if isinstance(self.canvas, Canvas):
            self.canvas.draw_shape(coordinates, figure_type)

    def mainloop(self):
        self.master.mainloop()

# --- Controller ---
class Controller(IController):
    """Контроллер, связывающий модель и представление."""
    def __init__(self, model: IModel, view: IView):
        self._model = model
        self._view = view
        self._view.set_controller(self) # Устанавливаем ссылку на контроллер в представлении
        
        # Инициализация UI компонентами из модели
        self._view.create_color_buttons(self._model.get_colors())
        self._view.create_figure_buttons(self._model.get_figures())
        
        # Установка начального состояния (первый цвет и фигура из списков)
        colors = self._model.get_colors()
        if colors:
            initial_color_name = next(iter(colors))
            initial_color_hex = colors[initial_color_name]
            self.handle_color_button_click(initial_color_hex, initial_color_name)
        else: # Обработка случая пустых цветов
            self.handle_color_button_click(DEFAULT_DRAWING_COLOR_HEX, DEFAULT_DRAWING_COLOR_NAME)

        figures = self._model.get_figures()
        if figures:
            initial_figure_name = next(iter(figures))
            self.handle_figure_button_click(initial_figure_name)
        else: # Обработка случая пустых фигур
            self.handle_figure_button_click(DEFAULT_ACTIVE_FIGURE)

    def handle_color_button_click(self, color_hex: str, color_name: str):
        self._view.update_color_display(color_hex, color_name)
        self._view.set_drawing_color(color_hex)

    def handle_figure_button_click(self, figure_name: str):
        self._view.update_figure_display(figure_name)
        if isinstance(self._view.canvas, Canvas): # Убедимся, что это наш Canvas
            self._view.canvas.set_active_figure(figure_name)

    def handle_draw_shape_request(self, 
                                  coordinates: Tuple[Tuple[int, int], Tuple[int, int]], 
                                  figure_type: str):
        # В будущем здесь может быть логика сохранения фигуры в модели
        # print(f"Controller: Запрос на рисование {figure_type} с координатами {coordinates}")
        self._view.draw_shape_on_canvas(coordinates, figure_type)

# --- Application ---
class App(IApp):
    """Главный класс приложения."""
    def __init__(self, master: tk.Tk):
        self.master = master
        self.model = Model()  # Используем цвета и фигуры по умолчанию
        self.view = View(master, DEFAULT_WINDOW_TITLE)
        # Контроллер создается после модели и представления
        self.controller = Controller(self.model, self.view)

    def run(self):
        """Запускает главный цикл приложения."""
        self.view.mainloop()

# --- Entry Point ---
if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    try:
        app.run()
    except Exception as e:
        messagebox.showerror("Критическая ошибка", f"Произошла непредвиденная ошибка: {e}")
        # Здесь можно добавить логирование ошибки
        # import traceback
        # traceback.print_exc()