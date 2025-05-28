import tkinter as tk
from tkinter import ttk
from typing import Dict, Tuple, Any # Добавлено для корректной работы с типами

# Предполагается, что файл app_rainbow_mvc_interfaces.py находится в том же каталоге
# или доступен через PYTHONPATH
from app_rainbow_mvc_interfaces import (
    IModel, IButtonColor, IButtonFigures, ICanvas, 
    IView, IController, IApp, IEventHandler
)

class Model(IModel):
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
        # В диаграмме указано, что параметры фигуры - это кортеж.
        # Если фигура не найдена, возвращаем пустой кортеж.
        return self._figures.get(name, ())

class ButtonColor(tk.Button, IButtonColor):
    def __init__(self, master: tk.Widget, color_hex: str, color_name: str, command: callable, **kwargs):
        super().__init__(master, bg=color_hex, command=command, **kwargs)
        self.color_hex = color_hex
        self.color_name = color_name
        # Улучшение контрастности текста кнопки
        r, g, b = int(color_hex[1:3], 16), int(color_hex[3:5], 16), int(color_hex[5:7], 16)
        luminance = (0.299 * r + 0.587 * g + 0.114 * b) / 255
        text_color = "black" if luminance > 0.5 else "white"
        self.config(fg=text_color, activeforeground=text_color, relief=tk.RAISED, width=3)

    def show_color(self, label_widget: tk.Label, entry_widget: tk.Entry):
        label_widget.config(text=f"Selected Color: {self.color_name}")
        entry_widget.config(state=tk.NORMAL)
        entry_widget.delete(0, tk.END)
        entry_widget.insert(0, self.color_hex)
        entry_widget.config(state="readonly")

class ButtonFigures(tk.Button, IButtonFigures):
    def __init__(self, master: tk.Widget, figure_name: str, figure_params: Tuple, command: callable, **kwargs):
        super().__init__(master, text=figure_name, command=command, **kwargs)
        self._figure_name = figure_name
        self._figure_params = figure_params # Сохраняем параметры, хотя они не используются в show_figure
        self.config(relief=tk.RAISED)

    def get_figure_name(self) -> str:
        return self._figure_name

    def get_figure_params(self) -> Tuple:
        return self._figure_params

class Canvas(tk.Canvas, ICanvas, IEventHandler):
    def __init__(self, master: tk.Widget, **kwargs):
        super().__init__(master, bg="white", **kwargs)
        self.drawing_color: str = "#000000"  # Default color
        self.active_figure: str = "line"  # Default figure
        self.start_x: int | None = None
        self.start_y: int | None = None
        self.controller: IController | None = None # Для связи с контроллером, если потребуется

        self.bind("<Button-1>", self.on_press)
        self.bind("<B1-Motion>", self.on_drag)
        self.bind("<ButtonRelease-1>", self.on_release)

    def set_drawing_color(self, color_hex: str):
        self.drawing_color = color_hex

    def set_active_figure(self, figure_name: str):
        self.active_figure = figure_name

    def on_press(self, event):
        self.start_x = event.x
        self.start_y = event.y
        if self.active_figure == "freehand": # Начинаем рисовать сразу для freehand
            # Рисуем точку, чтобы было видно начало линии
            self.create_line(event.x, event.y, event.x + 1, event.y + 1, fill=self.drawing_color, width=2)

    def on_drag(self, event):
        if self.start_x is not None and self.start_y is not None and self.active_figure == "freehand":
            self.create_line(self.start_x, self.start_y, event.x, event.y, 
                             fill=self.drawing_color, width=2, capstyle=tk.ROUND)
            self.start_x = event.x
            self.start_y = event.y
        # Для других фигур рисование происходит в on_release или с предпросмотром (не реализовано)

    def on_release(self, event):
        if self.start_x is None or self.start_y is None: # Не было нажатия
            return

        end_x, end_y = event.x, event.y

        if self.active_figure == "line":
            self.create_line(self.start_x, self.start_y, end_x, end_y, fill=self.drawing_color, width=2)
        elif self.active_figure == "oval":
            self.create_oval(self.start_x, self.start_y, end_x, end_y, outline=self.drawing_color, width=2)
        elif self.active_figure == "rectangle":
            self.create_rectangle(self.start_x, self.start_y, end_x, end_y, outline=self.drawing_color, width=2)
        elif self.active_figure == "triangle":
            # Простой равнобедренный треугольник, основание горизонтально
            mid_x = (self.start_x + end_x) // 2
            # Точки: (левый нижний), (правый нижний), (верхний средний)
            # Если start_y > end_y, то рисуем вершиной вверх, иначе вершиной вниз
            if self.start_y > end_y: # Вершина вверху (end_y)
                 self.create_polygon(self.start_x, self.start_y, end_x, self.start_y, mid_x, end_y, 
                                   outline=self.drawing_color, fill='', width=2)
            else: # Вершина внизу (end_y)
                 self.create_polygon(self.start_x, self.start_y, end_x, self.start_y, mid_x, end_y, 
                                   outline=self.drawing_color, fill='', width=2)
        
        # Сброс начальных координат для всех фигур, кроме freehand (он сбрасывается в on_drag)
        if self.active_figure != "freehand":
            self.start_x = None
            self.start_y = None

class View(IView):
    def __init__(self, master: tk.Tk, title: str):
        self.master = master
        self.master.title(title)
        self.master.geometry("700x550") # Немного увеличим размер окна

        self._controller: IController | None = None

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

    def set_controller(self, controller: IController):
        self._controller = controller
        if isinstance(self.canvas, Canvas): # Убедимся, что это наш Canvas
            self.canvas.controller = controller 

    def create_color_buttons(self, colors: Dict[str, str]):
        for color_hex, color_name in colors.items():
            button = ButtonColor(self.color_buttons_panel, color_hex, color_name,
                                 # Используем lambda для передачи аргументов в обработчик
                                 lambda h=color_hex, n=color_name: self._controller.handle_color_button_click(h, n))
            button.pack(side=tk.LEFT, padx=2, pady=2)

    def create_figure_buttons(self, figures: Dict[str, Any]):
        for figure_name, figure_params in figures.items():
            button = ButtonFigures(self.figure_buttons_panel, figure_name, figure_params, 
                                   # Используем lambda для передачи аргументов в обработчик
                                   lambda n=figure_name: self._controller.handle_figure_button_click(n))
            button.pack(side=tk.LEFT, padx=2, pady=2)

    def update_color_display(self, color_hex: str, color_name: str):
        if isinstance(self.color_label, ttk.Label) and isinstance(self.color_entry, ttk.Entry):
            self.color_label.config(text=f"Selected Color: {color_name}")
            self.color_entry.config(state=tk.NORMAL)
            self.color_entry.delete(0, tk.END)
            self.color_entry.insert(0, color_hex)
            self.color_entry.config(state="readonly")

    def update_figure_display(self, figure_name: str):
        if isinstance(self.figure_label, ttk.Label):
            self.figure_label.config(text=f"Selected Figure: {figure_name}")

    def set_drawing_color(self, color_hex: str):
        if isinstance(self.canvas, Canvas):
            self.canvas.set_drawing_color(color_hex)

    def set_active_figure(self, figure_name: str):
        if isinstance(self.canvas, Canvas):
            self.canvas.set_active_figure(figure_name)

    def mainloop(self):
        self.master.mainloop()

class Controller(IController):
    def __init__(self, model: IModel, view: IView):
        self._model = model
        self._view = view
        self._view.set_controller(self)

    def handle_color_button_click(self, color_hex: str, color_name: str):
        self._view.set_drawing_color(color_hex)
        self._view.update_color_display(color_hex, color_name)

    def handle_figure_button_click(self, figure_name: str):
        # Параметры фигуры из модели не используются напрямую здесь, 
        # но могут быть полезны для более сложных фигур
        # figure_params = self._model.get_figure_params(figure_name)
        self._view.set_active_figure(figure_name)
        self._view.update_figure_display(figure_name)

class App(IApp):
    def __init__(self, master: tk.Tk):
        self.master = master

        # Данные для модели (можно вынести в конфигурацию или отдельные классы-поставщики)
        default_colors = {
            "#FF0000": "Red", "#FFA500": "Orange", "#FFFF00": "Yellow",
            "#008000": "Green", "#0000FF": "Blue", "#4B0082": "Indigo",
            "#EE82EE": "Violet", "#000000": "Black", "#FFFFFF": "White"
        }
        default_figures = {
            "freehand": (),
            "line": (),
            "oval": (),
            "rectangle": (),
            "triangle": ()
        }

        self.model = Model(colors=default_colors, figures=default_figures)
        self.view = View(master, title="Rainbow MVC Paint (New)")
        self.controller = Controller(model=self.model, view=self.view)

        # Инициализация View данными из Model
        self._initialize_view_components()

    def _initialize_view_components(self):
        self.view.create_color_buttons(self.model.get_colors())
        self.view.create_figure_buttons(self.model.get_figures())
        
        # Установка начального цвета и фигуры
        initial_color_hex = "#000000" # Black
        initial_color_name = self.model.get_color_name(initial_color_hex)
        self.controller.handle_color_button_click(initial_color_hex, initial_color_name)

        initial_figure = "line"
        self.controller.handle_figure_button_click(initial_figure)

    def run(self):
        self.view.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    app.run()