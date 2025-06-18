import tkinter as tk
from tkinter import ttk
import math
from typing import Dict, Tuple, Any

# --- Constants ---
DEFAULT_WINDOW_TITLE = "Rainbow Star MVC Paint"
DEFAULT_WINDOW_GEOMETRY = "800x600"
DEFAULT_CANVAS_BG = "white"
DEFAULT_DRAWING_COLOR_HEX = "#000000"

# Словарь с заранее заданными координатами фигур (относительные, центр в (0, 0), радиус 1)
SHAPES_COORDINATES = {
    "star": [
        0.0, -1.0,    # Верхняя точка
        0.2245, -0.309,  # Правая верхняя внутренняя
        0.9511, -0.309,  # Правая верхняя внешняя
        0.3633, 0.118,   # Правая нижняя внутренняя
        0.5878, 0.809,   # Правая нижняя внешняя
        0.0, 0.382,      # Нижняя внутренняя
        -0.5878, 0.809,  # Левая нижняя внешняя
        -0.3633, 0.118,  # Левая нижняя внутренняя
        -0.9511, -0.309, # Левая верхняя внешняя
        -0.2245, -0.309, # Левая верхняя внутренняя
        0.0, -1.0        # Замыкаем звезду
    ],
    "circle": [
        # 36 точек для аппроксимации круга (каждые 10 градусов)
        *[x for i in range(36) for x in [math.cos(i * 10 * math.pi / 180), math.sin(i * 10 * math.pi / 180)]],
        1.0, 0.0  # Замыкаем круг
    ],
    "square": [
        -1.0, -1.0,  # Нижний левый угол
        1.0, -1.0,   # Нижний правый угол
        1.0, 1.0,    # Верхний правый угол
        -1.0, 1.0,   # Верхний левый угол
        -1.0, -1.0   # Замыкаем квадрат
    ],
    "tree": [
        0.0, -1.0,    # Вершина ёлки
        0.5, -0.8,    # Правая сторона верхнего яруса
        0.3, -0.6,    # Правая внутренняя точка верхнего яруса
        0.7, -0.4,    # Правая сторона среднего яруса
        0.5, -0.2,    # Правая внутренняя точка среднего яруса
        0.9, 0.0,     # Правая сторона нижнего яруса
        0.2, 0.0,     # Правая внутренняя точка нижнего яруса (ствол)
        0.2, 0.2,     # Правая сторона ствола
        -0.2, 0.2,    # Левая сторона ствола
        -0.2, 0.0,    # Левая внутренняя точка нижнего яруса (ствол)
        -0.9, 0.0,    # Левая сторона нижнего яруса
        -0.5, -0.2,   # Левая внутренняя точка среднего яруса
        -0.7, -0.4,   # Левая сторона среднего яруса
        -0.3, -0.6,   # Левая внутренняя точка верхнего яруса
        -0.5, -0.8,   # Левая сторона верхнего яруса
        0.0, -1.0     # Замыкаем в вершину
    ]
}

# --- Utility Functions ---
def get_text_color_for_bg(hex_color: str) -> str:
    """Определяет цвет текста (черный или белый) для лучшей читаемости на заданном фоне."""
    try:
        hex_color = hex_color.lstrip('#')
        if len(hex_color) != 6:
            return "black"  # По умолчанию, если hex некорректен
        r, g, b = int(hex_color[0:2], 16), int(hex_color[2:4], 16), int(hex_color[4:6], 16)
        brightness = (r * 299 + g * 587 + b * 114) / 1000
        return "black" if brightness > 128 else "white"
    except ValueError:
        return "black"  # По умолчанию при ошибке

class Model:
    def __init__(self, colors: Dict[str, str], figures: Dict[str, Any]):
        self._colors = colors
        self._figures = figures

    def get_colors(self) -> Dict[str, str]:
        return self._colors

    def get_color_name(self, hex_code: str) -> str:
        return self._colors.get(hex_code, "Unknown Color")

    def get_figures(self) -> Dict[str, Any]:
        return self._figures

    def get_figure_params(self, name: str) -> Tuple:
        return self._figures.get(name, ())

class ButtonColor(tk.Button):
    def __init__(self, master: tk.Widget, color_hex: str, color_name: str, command: callable, **kwargs):
        super().__init__(master, bg=color_hex, command=command, **kwargs)
        self.color_hex = color_hex
        self.color_name = color_name
        # Улучшение контрастности текста кнопки
        r, g, b = int(color_hex[1:3], 16), int(color_hex[3:5], 16), int(color_hex[5:7], 16)
        luminance = (0.299 * r + 0.587 * g + 0.114 * b) / 255
        text_color = "black" if luminance > 0.5 else "white"
        self.config(fg=text_color, activeforeground=text_color, relief=tk.RAISED, width=3)

class ButtonFigures(tk.Button):
    def __init__(self, master: tk.Widget, figure_name: str, figure_params: Tuple, command: callable, **kwargs):
        super().__init__(master, text=figure_name, command=command, **kwargs)
        self._figure_name = figure_name
        self._figure_params = figure_params
        self.config(relief=tk.RAISED)

class Canvas(tk.Canvas):
    """Холст для рисования фигур."""
    def __init__(self, master: tk.Widget, **kwargs):
        super().__init__(master, bg=kwargs.pop('bg', DEFAULT_CANVAS_BG), **kwargs)
        self.drawing_color: str = DEFAULT_DRAWING_COLOR_HEX
        self.current_shape: str = "star"  # Текущая выбранная фигура
        
        self._start_x: int | None = None
        self._start_y: int | None = None
        self._current_shape_id: int | None = None  # ID временной фигуры при перетаскивании
        self._shapes: dict[int, list[float]] = {}  # Словарь для хранения координат фигур {ID: координаты}

        self.bind("<ButtonPress-1>", self.on_press)
        self.bind("<B1-Motion>", self.on_drag)
        # self.bind("<ButtonRelease-1>", self.on_release)
        self.bind("<ButtonRelease-1>", self.on_drag)

    def set_drawing_color(self, color_hex: str):
        self.drawing_color = color_hex

    def set_shape(self, shape: str):
        """Устанавливает текущую фигуру для рисования."""
        self.current_shape = shape

    def on_press(self, event: tk.Event):
        self._start_x = event.x
        self._start_y = event.y

    def on_drag(self, event: tk.Event):
        print(event.__dict__, str(event.type.__repr__()).strip('<>').partition(':')[0])
        if self._start_x is None or self._start_y is None:
            return

        if self._current_shape_id and event.type != tk.EventType.ButtonRelease:
            self.delete(self._current_shape_id)
            self._current_shape_id = None

        # Вычисляем центр и радиус фигуры
        min_x, max_x = min(self._start_x, event.x), max(self._start_x, event.x)
        min_y, max_y = min(self._start_y, event.y), max(self._start_y, event.y)
        center_x = (min_x + max_x) / 2
        center_y = (min_y + max_y) / 2
        radius = min(max_x - min_x, max_y - min_y) / 2


        shape_points = []
        relative_points = SHAPES_COORDINATES[self.current_shape]
        for i in range(0, len(relative_points), 2):
            rel_x = relative_points[i]
            rel_y = relative_points[i + 1]
            abs_x = center_x + rel_x * radius
            abs_y = center_y + rel_y * radius
            shape_points.extend([abs_x, abs_y])

            # Рисуем фигуру как непрерывную линию, используя преобразованные точки
        self._current_shape_id = self.create_line(*shape_points, fill=self.drawing_color, width=2)

    # def on_release(self, event: tk.Event):
    #     if self._start_x is None or self._start_y is None:
    #         return

    #     min_x, max_x = min(self._start_x, event.x), max(self._start_x, event.x)
    #     min_y, max_y = min(self._start_y, event.y), max(self._start_y, event.y)
    #     center_x = (min_x + max_x) / 2
    #     center_y = (min_y + max_y) / 2
    #     radius = min(max_x - min_x, max_y - min_y) / 2

    #     shape_points = []
    #     relative_points = SHAPES_COORDINATES[self.current_shape]
    #     for i in range(0, len(relative_points), 2):
    #         rel_x = relative_points[i]
    #         rel_y = relative_points[i + 1]
    #         abs_x = center_x + rel_x * radius
    #         abs_y = center_y + rel_y * radius
    #         shape_points.extend([abs_x, abs_y])

    #     # Рисуем финальную фигуру как непрерывную линию, используя преобразованные точки
    #     self.create_line(*shape_points, fill=self.drawing_color, width=2)


class View:
    def __init__(self, master: tk.Tk, title: str):
        self.master = master
        self.master.title(title)
        self.master.geometry(DEFAULT_WINDOW_GEOMETRY)

        self._controller = None

        # Основные фреймы
        controls_frame = ttk.Frame(master, padding=10)
        controls_frame.pack(fill=tk.X)

        self.color_frame = ttk.LabelFrame(controls_frame, text="Color", padding=10)
        self.color_frame.pack(side=tk.LEFT, padx=5, fill=tk.X, expand=True)

        self.figure_frame = ttk.LabelFrame(controls_frame, text="Figure", padding=10)
        self.figure_frame.pack(side=tk.LEFT, padx=5, fill=tk.X, expand=True)

        # Виджеты для отображения информации о цвете
        self.color_label = ttk.Label(self.color_frame, text="Selected Color: None")
        self.color_label.pack(side=tk.LEFT, padx=(0, 5))
        self.color_entry = ttk.Entry(self.color_frame, width=10, state="readonly")
        self.color_entry.pack(side=tk.LEFT)

        # Виджет для отображения информации о фигуре
        self.figure_label = ttk.Label(self.figure_frame, text="Selected Figure: None")
        self.figure_label.pack(side=tk.LEFT)
        
        # Фрейм для кнопок выбора цвета и фигур
        self.buttons_frame = ttk.Frame(master, padding=(10,0,10,10))
        self.buttons_frame.pack(fill=tk.X)

        self.color_buttons_panel = ttk.LabelFrame(self.buttons_frame, text="Color Palette", padding=5)
        self.color_buttons_panel.pack(side=tk.LEFT, padx=(0,5), fill=tk.X, expand=True)

        self.figure_buttons_panel = ttk.LabelFrame(self.buttons_frame, text="Drawing Tools", padding=5)
        self.figure_buttons_panel.pack(side=tk.LEFT, fill=tk.X, expand=True)

        # Холст
        self.canvas = Canvas(master, width=600, height=400)
        self.canvas.pack(fill=tk.BOTH, expand=True, padx=10, pady=(0,10))

    def set_controller(self, controller):
        self._controller = controller

    def create_color_buttons(self, colors: Dict[str, str]):
        for color_hex, color_name in colors.items():
            button = ButtonColor(self.color_buttons_panel, color_hex, color_name,
                               lambda h=color_hex, n=color_name: self._controller.handle_color_button_click(h, n))
            button.pack(side=tk.LEFT, padx=2, pady=2)

    def create_figure_buttons(self, figures: Dict[str, Any]):
        for figure_name, figure_params in figures.items():
            button = ButtonFigures(self.figure_buttons_panel, figure_name, figure_params,
                                 lambda n=figure_name: self._controller.handle_figure_button_click(n))
            button.pack(side=tk.LEFT, padx=2, pady=2)

    def update_color_display(self, color_hex: str, color_name: str):
        self.color_label.config(text=f"Selected Color: {color_name}")
        self.color_entry.config(state=tk.NORMAL)
        self.color_entry.delete(0, tk.END)
        self.color_entry.insert(0, color_hex)
        self.color_entry.config(state="readonly")

    def update_figure_display(self, figure_name: str):
        self.figure_label.config(text=f"Selected Figure: {figure_name}")

    def set_drawing_color(self, color_hex: str):
        self.canvas.set_drawing_color(color_hex)

    def set_active_figure(self, figure_name: str):
        self.canvas.set_shape(figure_name)

    def mainloop(self):
        self.master.mainloop()

class Controller:
    def __init__(self, model: Model, view: View):
        self._model = model
        self._view = view
        self._view.set_controller(self)

    def handle_color_button_click(self, color_hex: str, color_name: str):
        self._view.set_drawing_color(color_hex)
        self._view.update_color_display(color_hex, color_name)

    def handle_figure_button_click(self, figure_name: str):
        self._view.set_active_figure(figure_name)
        self._view.update_figure_display(figure_name)

class App:
    def __init__(self, master: tk.Tk):
        self.master = master

        # Данные для модели
        default_colors = {
            "#FF0000": "Red", "#FFA500": "Orange", "#FFFF00": "Yellow",
            "#008000": "Green", "#0000FF": "Blue", "#4B0082": "Indigo",
            "#EE82EE": "Violet", "#000000": "Black", "#FFFFFF": "White"
        }
        default_figures = SHAPES_COORDINATES

        self.model = Model(colors=default_colors, figures=default_figures)
        self.view = View(master, title=DEFAULT_WINDOW_TITLE)
        self.controller = Controller(model=self.model, view=self.view)

        # Инициализация View данными из Model
        self._initialize_view_components()

    def _initialize_view_components(self):
        self.view.create_color_buttons(self.model.get_colors())
        self.view.create_figure_buttons(self.model.get_figures())
        
        # Установка начального цвета и фигуры
        initial_color_hex = "#000000"  # Black
        initial_color_name = self.model.get_color_name(initial_color_hex)
        self.controller.handle_color_button_click(initial_color_hex, initial_color_name)

        initial_figure = "star"
        self.controller.handle_figure_button_click(initial_figure)

    def run(self):
        self.view.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    app.run() 