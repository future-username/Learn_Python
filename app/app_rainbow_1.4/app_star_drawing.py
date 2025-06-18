# import tkinter as tk
# import math
# from tkinter import colorchooser

# # --- Constants ---
# DEFAULT_WINDOW_TITLE = "Drawing App"
# DEFAULT_WINDOW_GEOMETRY = "800x600"
# DEFAULT_CANVAS_BG = "white"
# DEFAULT_DRAWING_COLOR_HEX = "#000000"

# # Словарь с заранее заданными координатами фигур (относительные, центр в (0, 0), радиус 1)
# SHAPES_COORDINATES = {
#     "star": [
#         0.0, -1.0,    # Верхняя точка
#         0.2245, -0.309,  # Правая верхняя внутренняя
#         0.9511, -0.309,  # Правая верхняя внешняя
#         0.3633, 0.118,   # Правая нижняя внутренняя
#         0.5878, 0.809,   # Правая нижняя внешняя
#         0.0, 0.382,      # Нижняя внутренняя
#         -0.5878, 0.809,  # Левая нижняя внешняя
#         -0.3633, 0.118,  # Левая нижняя внутренняя
#         -0.9511, -0.309, # Левая верхняя внешняя
#         -0.2245, -0.309, # Левая верхняя внутренняя
#         0.0, -1.0        # Замыкаем звезду
#     ],
#     "circle": [
#         # 36 точек для аппроксимации круга (каждые 10 градусов)
#         *[x for i in range(36) for x in [math.cos(i * 10 * math.pi / 180), math.sin(i * 10 * math.pi / 180)]],
#         1.0, 0.0  # Замыкаем круг
#     ],
#     "square": [
#         -1.0, -1.0,  # Нижний левый угол
#         1.0, -1.0,   # Нижний правый угол
#         1.0, 1.0,    # Верхний правый угол
#         -1.0, 1.0,   # Верхний левый угол
#         -1.0, -1.0   # Замыкаем квадрат
#     ],
#     "tree": [
#     0.0, -1.0,    # Вершина ёлки
#     0.5, -0.8,    # Правая сторона верхнего яруса
#     0.3, -0.6,    # Правая внутренняя точка верхнего яруса
#     0.7, -0.4,    # Правая сторона среднего яруса
#     0.5, -0.2,    # Правая внутренняя точка среднего яруса
#     0.9, 0.0,     # Правая сторона нижнего яруса
#     0.2, 0.0,     # Правая внутренняя точка нижнего яруса (ствол)
#     0.2, 0.2,     # Правая сторона ствола
#     -0.2, 0.2,    # Левая сторона ствола
#     -0.2, 0.0,    # Левая внутренняя точка нижнего яруса (ствол)
#     -0.9, 0.0,    # Левая сторона нижнего яруса
#     -0.5, -0.2,   # Левая внутренняя точка среднего яруса
#     -0.7, -0.4,   # Левая сторона среднего яруса
#     -0.3, -0.6,   # Левая внутренняя точка верхнего яруса
#     -0.5, -0.8,   # Левая сторона верхнего яруса
#     0.0, -1.0     # Замыкаем в вершину
# ]
# }

# # --- Utility Functions ---
# def get_text_color_for_bg(hex_color: str) -> str:
#     """Определяет цвет текста (черный или белый) для лучшей читаемости на заданном фоне."""
#     try:
#         hex_color = hex_color.lstrip('#')
#         if len(hex_color) != 6:
#             return "black"  # По умолчанию, если hex некорректен
#         r, g, b = int(hex_color[0:2], 16), int(hex_color[2:4], 16), int(hex_color[4:6], 16)
#         brightness = (r * 299 + g * 587 + b * 114) / 1000
#         return "black" if brightness > 128 else "white"
#     except ValueError:
#         return "black"  # По умолчанию при ошибке

# class Canvas(tk.Canvas):
#     """Холст для рисования фигур."""
#     def __init__(self, master: tk.Widget, **kwargs):
#         super().__init__(master, bg=kwargs.pop('bg', DEFAULT_CANVAS_BG), **kwargs)
#         self.drawing_color: str = DEFAULT_DRAWING_COLOR_HEX
#         self.current_shape: str = "star"  # Текущая выбранная фигура
        
#         self._start_x: int | None = None
#         self._start_y: int | None = None
#         self._current_shape_id: int | None = None  # ID временной фигуры при перетаскивании
#         self._shapes: dict[int, list[float]] = {}  # Словарь для хранения координат фигур {ID: координаты}

#         self.bind("<ButtonPress-1>", self.on_press)
#         self.bind("<B1-Motion>", self.on_drag)
#         self.bind("<ButtonRelease-1>", self.on_release)

#     def set_drawing_color(self, color_hex: str):
#         self.drawing_color = color_hex

#     def set_shape(self, shape: str):
#         """Устанавливает текущую фигуру для рисования."""
#         self.current_shape = shape

#     def on_press(self, event: tk.Event):
#         self._start_x = event.x
#         self._start_y = event.y

#     def on_drag(self, event: tk.Event):
#         if self._start_x is None or self._start_y is None:
#             return

#         if self._current_shape_id:
#             self.delete(self._current_shape_id)
#             self._current_shape_id = None

#         # Вычисляем центр и радиус фигуры
#         min_x, max_x = min(self._start_x, event.x), max(self._start_x, event.x)
#         min_y, max_y = min(self._start_y, event.y), max(self._start_y, event.y)
#         center_x = (min_x + max_x) / 2
#         center_y = (min_y + max_y) / 2
#         radius = min(max_x - min_x, max_y - min_y) / 2

#         if radius == 0:
#             shape_points = [center_x, center_y, center_x+1, center_y, center_x+1, center_y+1, center_x, center_y+1, center_x, center_y]
#         else:
#             # Масштабируем и смещаем относительные координаты выбранной фигуры
#             shape_points = []
#             relative_points = SHAPES_COORDINATES[self.current_shape]
#             for i in range(0, len(relative_points), 2):
#                 rel_x = relative_points[i]
#                 rel_y = relative_points[i + 1]
#                 abs_x = center_x + rel_x * radius
#                 abs_y = center_y + rel_y * radius
#                 shape_points.extend([abs_x, abs_y])

#         if shape_points:
#             # Рисуем фигуру как непрерывную линию, используя преобразованные точки
#             self._current_shape_id = self.create_line(
#                 *shape_points,
#                 fill=self.drawing_color,
#                 width=2,
#                 tags="temp_shape"
#             )

#     def on_release(self, event: tk.Event):
#         if self._start_x is None or self._start_y is None:
#             return

#         if self._current_shape_id:
#             self.delete(self._current_shape_id)
#             self._current_shape_id = None

#         # Вычисляем центр и радиус фигуры
#         min_x, max_x = min(self._start_x, event.x), max(self._start_x, event.x)
#         min_y, max_y = min(self._start_y, event.y), max(self._start_y, event.y)
#         center_x = (min_x + max_x) / 2
#         center_y = (min_y + max_y) / 2
#         radius = min(max_x - min_x, max_y - min_y) / 2

#         if radius == 0:
#             shape_points = [center_x, center_y, center_x+1, center_y, center_x+1, center_y+1, center_x, center_y+1, center_x, center_y]
#         else:
#             # Масштабируем и смещаем относительные координаты выбранной фигуры
#             shape_points = []
#             relative_points = SHAPES_COORDINATES[self.current_shape]
#             for i in range(0, len(relative_points), 2):
#                 rel_x = relative_points[i]
#                 rel_y = relative_points[i + 1]
#                 abs_x = center_x + rel_x * radius
#                 abs_y = center_y + rel_y * radius
#                 shape_points.extend([abs_x, abs_y])

#         if shape_points:
#             # Рисуем финальную фигуру как непрерывную линию, используя преобразованные точки
#             shape_id = self.create_line(
#                 *shape_points,
#                 fill=self.drawing_color,
#                 width=2
#             )
#             # Сохраняем координаты в словарь
#             self._shapes[shape_id] = shape_points.copy()

#         self._start_x = None
#         self._start_y = None

#     def get_shapes(self) -> dict[int, list[float]]:
#         """Возвращает словарь с координатами всех фигур."""
#         return self._shapes

# class App:
#     """Основное приложение Tkinter для рисования фигур."""
#     def __init__(self, root: tk.Tk):
#         self.root = root
#         self.root.title(DEFAULT_WINDOW_TITLE)
#         self.root.geometry(DEFAULT_WINDOW_GEOMETRY)

#         self.canvas = Canvas(self.root, bg=DEFAULT_CANVAS_BG)
#         self.canvas.pack(fill=tk.BOTH, expand=True)

#         self.color_frame = tk.Frame(self.root)
#         self.color_frame.pack(side=tk.BOTTOM, fill=tk.X)

#         self.color_label = tk.Label(self.color_frame, text=f"Цвет: Черный")
#         self.color_label.pack(side=tk.LEFT, padx=5, pady=5)

#         self.color_entry = tk.Entry(self.color_frame, width=10)
#         self.color_entry.insert(0, DEFAULT_DRAWING_COLOR_HEX)
#         self.color_entry.config(bg=DEFAULT_DRAWING_COLOR_HEX, fg=get_text_color_for_bg(DEFAULT_DRAWING_COLOR_HEX))
#         self.color_entry.pack(side=tk.LEFT, padx=5, pady=5)

#         choose_color_button = tk.Button(self.color_frame, text="Выбрать цвет", command=self._choose_color)
#         choose_color_button.pack(side=tk.LEFT, padx=5, pady=5)

#         # Добавляем выпадающий список для выбора фигуры
#         self.shape_var = tk.StringVar(value="star")
#         shape_label = tk.Label(self.color_frame, text="Фигура:")
#         shape_label.pack(side=tk.LEFT, padx=5, pady=5)
#         shape_menu = tk.OptionMenu(self.color_frame, self.shape_var, *SHAPES_COORDINATES.keys(), command=self._set_shape)
#         shape_menu.pack(side=tk.LEFT, padx=5, pady=5)

#         # Добавляем кнопку для вывода словаря с координатами фигур
#         print_shapes_button = tk.Button(self.color_frame, text="Вывести координаты фигур", command=self._print_shapes)
#         print_shapes_button.pack(side=tk.LEFT, padx=5, pady=5)

#     def _choose_color(self):
#         color_code = colorchooser.askcolor(title="Выберите цвет")[1]
#         if color_code:
#             self.canvas.set_drawing_color(color_code)
#             self.color_entry.delete(0, tk.END)
#             self.color_entry.insert(0, color_code)
#             self.color_entry.config(bg=color_code, fg=get_text_color_for_bg(color_code))
#             self.color_label.config(text=f"Цвет: {color_code}")  # Обновляем метку с HEX кодом

#     def _set_shape(self, shape: str):
#         """Устанавливает текущую фигуру для рисования."""
#         self.canvas.set_shape(shape)

#     def _print_shapes(self):
#         """Выводит словарь с координатами фигур в консоль."""
#         shapes = self.canvas.get_shapes()
#         print("Координаты фигур:")
#         for shape_id, coords in shapes.items():
#             print(f"Фигура {shape_id}: {coords}")

#     def run(self):
#         self.root.mainloop()

# if __name__ == "__main__":
#     root = tk.Tk()
#     app = App(root)
#     app.run()

import tkinter as tk
import math
from tkinter import colorchooser

# --- Constants ---
DEFAULT_WINDOW_TITLE = "Drawing App"
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

class Controller:
    """Заглушка для класса Controller, так как его функциональность не определена."""
    pass

class Canvas(tk.Canvas):
    """Холст для рисования фигур."""
    def __init__(self, master: tk.Widget, **kwargs):
        super().__init__(master, bg=kwargs.pop('bg', DEFAULT_CANVAS_BG), **kwargs)
        self.drawing_color: str = DEFAULT_DRAWING_COLOR_HEX
        self._start_x: int | None = None
        self._start_y: int | None = None
        self._last_x: int | None = None
        self._last_y: int | None = None
        self._current_shape_id: int | None = None  # ID временной фигуры при перетаскивании
        self.controller: Controller = Controller()  # Заглушка для контроллера
        self.current_shape: str = "star"  # Текущая выбранная фигура

        self.bind("<ButtonPress-1>", self._on_press)
        self.bind("<B1-Motion>", self._on_drag)
        self.bind("<ButtonRelease-1>", self._on_release)

    def set_drawing_color(self, color_hex: str):
        self.drawing_color = color_hex

    def draw_shape(self, coordinates: list[float]):
        """Рисует фигуру с заданными абсолютными координатами."""
        if coordinates:
            self.create_line(
                *coordinates,
                fill=self.drawing_color,
                width=2
            )

    def _on_press(self, event: tk.Event):
        self._start_x = event.x
        self._start_y = event.y

    def _on_drag(self, event: tk.Event):
        if self._start_x is None or self._start_y is None:
            return

        if self._current_shape_id:
            self.delete(self._current_shape_id)
            self._current_shape_id = None

        self._last_x = event.x
        self._last_y = event.y

        # Вычисляем центр и радиус фигуры
        min_x, max_x = min(self._start_x, self._last_x), max(self._start_x, self._last_x)
        min_y, max_y = min(self._start_y, self._last_y), max(self._start_y, self._last_y)
        center_x = (min_x + max_x) / 2
        center_y = (min_y + max_y) / 2
        radius = min(max_x - min_x, max_y - min_y) / 2

        if radius == 0:
            shape_points = [center_x, center_y, center_x+1, center_y, center_x+1, center_y+1, center_x, center_y+1, center_x, center_y]
        else:
            # Масштабируем и смещаем относительные координаты выбранной фигуры
            shape_points = []
            relative_points = SHAPES_COORDINATES[self.current_shape]
            for i in range(0, len(relative_points), 2):
                rel_x = relative_points[i]
                rel_y = relative_points[i + 1]
                abs_x = center_x + rel_x * radius
                abs_y = center_y + rel_y * radius
                shape_points.extend([abs_x, abs_y])

        if shape_points:
            # Рисуем временную фигуру
            self._current_shape_id = self.create_line(
                *shape_points,
                fill=self.drawing_color,
                width=2,
                tags="temp_shape"
            )

    def _on_release(self, event: tk.Event):
        if self._start_x is None or self._start_y is None:
            return

        if self._current_shape_id:
            self.delete(self._current_shape_id)
            self._current_shape_id = None

        self._last_x = event.x
        self._last_y = event.y

        # Вычисляем центр и радиус фигуры
        min_x, max_x = min(self._start_x, self._last_x), max(self._start_x, self._last_x)
        min_y, max_y = min(self._start_y, self._last_y), max(self._start_y, self._last_y)
        center_x = (min_x + max_x) / 2
        center_y = (min_y + max_y) / 2
        radius = min(max_x - min_x, max_y - min_y) / 2

        if radius == 0:
            shape_points = [center_x, center_y, center_x+1, center_y, center_x+1, center_y+1, center_x, center_y+1, center_x, center_y]
        else:
            # Масштабируем и смещаем относительные координаты выбранной фигуры
            shape_points = []
            relative_points = SHAPES_COORDINATES[self.current_shape]
            for i in range(0, len(relative_points), 2):
                rel_x = relative_points[i]
                rel_y = relative_points[i + 1]
                abs_x = center_x + rel_x * radius
                abs_y = center_y + rel_y * radius
                shape_points.extend([abs_x, abs_y])

        if shape_points:
            # Рисуем финальную фигуру с помощью метода draw_shape
            self.draw_shape(shape_points)

        self._start_x = None
        self._start_y = None
        self._last_x = None
        self._last_y = None

class App:
    """Основное приложение Tkinter для рисования фигур."""
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title(DEFAULT_WINDOW_TITLE)
        self.root.geometry(DEFAULT_WINDOW_GEOMETRY)

        self.canvas = Canvas(self.root, bg=DEFAULT_CANVAS_BG)
        self.canvas.pack(fill=tk.BOTH, expand=True)

        self.color_frame = tk.Frame(self.root)
        self.color_frame.pack(side=tk.BOTTOM, fill=tk.X)

        self.color_label = tk.Label(self.color_frame, text=f"Цвет: Черный")
        self.color_label.pack(side=tk.LEFT, padx=5, pady=5)

        self.color_entry = tk.Entry(self.color_frame, width=10)
        self.color_entry.insert(0, DEFAULT_DRAWING_COLOR_HEX)
        self.color_entry.config(bg=DEFAULT_DRAWING_COLOR_HEX, fg=get_text_color_for_bg(DEFAULT_DRAWING_COLOR_HEX))
        self.color_entry.pack(side=tk.LEFT, padx=5, pady=5)

        choose_color_button = tk.Button(self.color_frame, text="Выбрать цвет", command=self._choose_color)
        choose_color_button.pack(side=tk.LEFT, padx=5, pady=5)

        # Добавляем выпадающий список для выбора фигуры
        self.shape_var = tk.StringVar(value="star")
        shape_label = tk.Label(self.color_frame, text="Фигура:")
        shape_label.pack(side=tk.LEFT, padx=5, pady=5)
        shape_menu = tk.OptionMenu(self.color_frame, self.shape_var, *SHAPES_COORDINATES.keys(), command=self._set_shape)
        shape_menu.pack(side=tk.LEFT, padx=5, pady=5)

    def _choose_color(self):
        color_code = colorchooser.askcolor(title="Выберите цвет")[1]
        if color_code:
            self.canvas.set_drawing_color(color_code)
            self.color_entry.delete(0, tk.END)
            self.color_entry.insert(0, color_code)
            self.color_entry.config(bg=color_code, fg=get_text_color_for_bg(color_code))
            self.color_label.config(text=f"Цвет: {color_code}")  # Обновляем метку с HEX кодом

    def _set_shape(self, shape: str):
        """Устанавливает текущую фигуру для рисования."""
        self.canvas.current_shape = shape

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    app.run()