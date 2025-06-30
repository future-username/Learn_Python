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
        self.__colors = colors
        self.__figures = figures

    def get_colors(self) -> Dict[str, str]:
        return self.__colors

    def get_color_name(self, hex_code: str) -> str:
        return self.__colors.get(hex_code, "Unknown Color")

    def get_figures(self) -> Dict[str, Any]:
        return self.__figures

    def get_figure_params(self, name: str) -> Tuple:
        return self.__figures.get(name, ())

class ButtonColor(tk.Button):
    def __init__(self, master: tk.Widget, color_hex: str, color_name: str, command: callable, **kwargs):
        super().__init__(master, bg=color_hex, command=command, **kwargs)
        self.__color_hex = color_hex
        self.__color_name = color_name
        # Улучшение контрастности текста кнопки
        r, g, b = int(color_hex[1:3], 16), int(color_hex[3:5], 16), int(color_hex[5:7], 16)
        luminance = (0.299 * r + 0.587 * g + 0.114 * b) / 255
        text_color = "black" if luminance > 0.5 else "white"
        self.config(fg=text_color, activeforeground=text_color, relief=tk.RAISED, width=3)

    def show_color(self, label_widget, entry_widget):
        label_widget.config(text=f"Selected Color: {self.__color_name}")
        entry_widget.config(state=tk.NORMAL)
        entry_widget.delete(0, tk.END)
        entry_widget.insert(0, self.__color_hex)
        entry_widget.config(state="readonly")

class ButtonFigures(tk.Button):
    def __init__(self, master: tk.Widget, figure_name: str, figure_params: Tuple, command: callable, **kwargs):
        super().__init__(master, text=figure_name, command=command, **kwargs)
        self.__figure_name = figure_name
        self.__figure_params = figure_params
        self.config(relief=tk.RAISED)

    def get_figure_name(self) -> str:
        return self.__figure_name

    def get_figure_params(self) -> Tuple:
        return self.__figure_params

class Canvas(tk.Canvas):
    """Холст для рисования фигур."""
    def __init__(self, master: tk.Widget, **kwargs):
        super().__init__(master, bg=kwargs.pop('bg', DEFAULT_CANVAS_BG), **kwargs)
        self.__drawing_color: str = DEFAULT_DRAWING_COLOR_HEX
        self.__current_shape: str = "star"  # Текущая выбранная фигура
        self.__start_x: int | None = None
        self.__start_y: int | None = None
        self.__current_shape_id: int | None = None  # ID временной фигуры при перетаскивании
        self.__shapes: dict[int, list[float]] = {}  # Словарь для хранения координат фигур {ID: координаты}

        self.bind("<ButtonPress-1>", self.__on_press)
        self.bind("<B1-Motion>", self.__on_drag)
        self.bind("<ButtonRelease-1>", self.__on_drag)

    def set_drawing_color(self, color_hex: str):
        self.__drawing_color = color_hex

    def set_shape(self, shape: str):
        self.__current_shape = shape

    def __on_press(self, event: tk.Event):
        self.__start_x = event.x
        self.__start_y = event.y

    def __on_drag(self, event: tk.Event):
        if self.__start_x is None or self.__start_y is None:
            return

        if self.__current_shape_id and event.type != tk.EventType.ButtonRelease:
            self.delete(self.__current_shape_id)
            self.__current_shape_id = None

        min_x, max_x = min(self.__start_x, event.x), max(self.__start_x, event.x)
        min_y, max_y = min(self.__start_y, event.y), max(self.__start_y, event.y)
        center_x = (min_x + max_x) / 2
        center_y = (min_y + max_y) / 2
        radius = min(max_x - min_x, max_y - min_y) / 2

        shape_points = []
        relative_points = SHAPES_COORDINATES[self.__current_shape]
        for i in range(0, len(relative_points), 2):
            rel_x = relative_points[i]
            rel_y = relative_points[i + 1]
            abs_x = center_x + rel_x * radius
            abs_y = center_y + rel_y * radius
            shape_points.extend([abs_x, abs_y])

        self.__current_shape_id = self.create_line(*shape_points, fill=self.__drawing_color, width=2)

class View:
    def __init__(self, master: tk.Tk, title: str):
        self.__master = master
        self.__master.title(title)
        self.__master.geometry(DEFAULT_WINDOW_GEOMETRY)

        self.__controller = None

        controls_frame = ttk.Frame(self.__master, padding=10)
        controls_frame.pack(fill=tk.X)

        self.__color_frame = ttk.LabelFrame(controls_frame, text="Color", padding=10)
        self.__color_frame.pack(side=tk.LEFT, padx=5, fill=tk.X, expand=True)

        self.__figure_frame = ttk.LabelFrame(controls_frame, text="Figure", padding=10)
        self.__figure_frame.pack(side=tk.LEFT, padx=5, fill=tk.X, expand=True)

        self.__color_label = ttk.Label(self.__color_frame, text="Selected Color: None")
        self.__color_label.pack(side=tk.LEFT, padx=(0, 5))
        self.__color_entry = ttk.Entry(self.__color_frame, width=10, state="readonly")
        self.__color_entry.pack(side=tk.LEFT)

        self.__figure_label = ttk.Label(self.__figure_frame, text="Selected Figure: None")
        self.__figure_label.pack(side=tk.LEFT)
        
        self.__buttons_frame = ttk.Frame(self.__master, padding=(10,0,10,10))
        self.__buttons_frame.pack(fill=tk.X)

        self.__color_buttons_panel = ttk.LabelFrame(self.__buttons_frame, text="Color Palette", padding=5)
        self.__color_buttons_panel.pack(side=tk.LEFT, padx=(0,5), fill=tk.X, expand=True)

        self.__figure_buttons_panel = ttk.LabelFrame(self.__buttons_frame, text="Drawing Tools", padding=5)
        self.__figure_buttons_panel.pack(side=tk.LEFT, fill=tk.X, expand=True)

        self.__canvas = Canvas(self.__master, width=600, height=400)
        self.__canvas.pack(fill=tk.BOTH, expand=True, padx=10, pady=(0,10))

    def set_controller(self, controller):
        self.__controller = controller

    def create_color_buttons(self, colors: Dict[str, str]):
        for color_hex, color_name in colors.items():
            button = ButtonColor(self.__color_buttons_panel, color_hex, color_name,
                               lambda h=color_hex, n=color_name: self.__controller.handle_color_button_click(h, n))
            button.pack(side=tk.LEFT, padx=2, pady=2)

    def create_figure_buttons(self, figures: Dict[str, Any]):
        for figure_name, figure_params in figures.items():
            button = ButtonFigures(self.__figure_buttons_panel, figure_name, figure_params,
                                 lambda n=figure_name: self.__controller.handle_figure_button_click(n))
            button.pack(side=tk.LEFT, padx=2, pady=2)

    def update_color_display(self, color_hex: str, color_name: str):
        self.__color_label.config(text=f"Selected Color: {color_name}")
        self.__color_entry.config(state=tk.NORMAL)
        self.__color_entry.delete(0, tk.END)
        self.__color_entry.insert(0, color_hex)
        self.__color_entry.config(state="readonly")

    def update_figure_display(self, figure_name: str):
        self.__figure_label.config(text=f"Selected Figure: {figure_name}")

    def set_drawing_color(self, color_hex: str):
        self.__canvas.set_drawing_color(color_hex)

    def set_active_figure(self, figure_name: str):
        self.__canvas.set_shape(figure_name)

    def mainloop(self):
        self.__master.mainloop()

class Controller:
    def __init__(self, model: Model, view: View):
        self.__model = model
        self.__view = view
        self.__view.set_controller(self)

    def handle_color_button_click(self, color_hex: str, color_name: str):
        self.__view.set_drawing_color(color_hex)
        self.__view.update_color_display(color_hex, color_name)

    def handle_figure_button_click(self, figure_name: str):
        self.__view.set_active_figure(figure_name)
        self.__view.update_figure_display(figure_name)

class App:
    def __init__(self, master: tk.Tk):
        self.__master = master

        default_colors = {
            "#FF0000": "Red", "#FFA500": "Orange", "#FFFF00": "Yellow",
            "#008000": "Green", "#0000FF": "Blue", "#4B0082": "Indigo",
            "#EE82EE": "Violet", "#000000": "Black", "#FFFFFF": "White"
        }
        default_figures = SHAPES_COORDINATES

        self.__model = Model(colors=default_colors, figures=default_figures)
        self.__view = View(master, title=DEFAULT_WINDOW_TITLE)
        self.__controller = Controller(model=self.__model, view=self.__view)

        self.__initialize_view_components()

    def __initialize_view_components(self):
        self.__view.create_color_buttons(self.__model.get_colors())
        self.__view.create_figure_buttons(self.__model.get_figures())
        initial_color_hex = "#000000"  # Black
        initial_color_name = self.__model.get_color_name(initial_color_hex)
        self.__controller.handle_color_button_click(initial_color_hex, initial_color_name)
        initial_figure = "star"
        self.__controller.handle_figure_button_click(initial_figure)

    def run(self):
        self.__view.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    app.run() 