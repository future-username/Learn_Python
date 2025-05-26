import tkinter as tk
from tkinter import ttk
from app_rainbow_mvc_interfaces import IButtonColor, IButtonFigures, ICanvas, IController, IView, IApp, IEventHandler

class Model:
    def __init__(self, colors, figures):
        self.colors = colors
        self.figures = figures
    
    def get_colors(self):
        return self.colors
    
    def get_color_name(self, hex_code):
        return self.colors.get(hex_code, "Unknown Color")
    
    def get_figures(self):
        return self.figures
    
    def get_figure_params(self, name):
        return self.figures.get(name, ())

class ButtonColor(tk.Button, IButtonColor):
    def __init__(self, master, color_hex, color_name, command, **kwargs):
        tk.Button.__init__(self, master, bg=color_hex, command=command, **kwargs)
        self.color_hex = color_hex
        self.color_name = color_name
        
        # Улучшенная контрастность текста
        r, g, b = int(color_hex[1:3], 16), int(color_hex[3:5], 16), int(color_hex[5:7], 16)
        luminance = (0.299 * r + 0.587 * g + 0.114 * b) / 255
        text_color = "black" if luminance > 0.5 else "white"
        self.config(fg=text_color, activeforeground=text_color)
    
    def show_color(self, label_widget, entry_widget):
        label_widget.config(text=f"Selected Color: {self.color_name}")
        entry_widget.delete(0, tk.END)
        entry_widget.insert(0, self.color_hex)

class ButtonFigures(tk.Button, IButtonFigures):
    def __init__(self, master, figure_name, figure_params, command, **kwargs):
        tk.Button.__init__(self, master, text=figure_name, command=command, **kwargs)
        self.figure_name = figure_name
        self.figure_params = figure_params
    
    def get_figure_name(self):
        return self.figure_name
    
    def get_figure_params(self):
        return self.figure_params

class Canvas(tk.Canvas, ICanvas, IEventHandler):
    def __init__(self, master, **kwargs):
        tk.Canvas.__init__(self, master, **kwargs)
        self.drawing_color = "#000000"
        self.active_figure = "line"
        self.start_x = None
        self.start_y = None
        self.controller = None
        
        self.bind("<Button-1>", self.on_press)
        self.bind("<B1-Motion>", self.on_drag)
        self.bind("<ButtonRelease-1>", self.on_release)
    
    def set_drawing_color(self, color_hex):
        self.drawing_color = color_hex
    
    def set_active_figure(self, figure_name):
        self.active_figure = figure_name
    
    def on_press(self, event):
        self.start_x = event.x
        self.start_y = event.y
        
        if self.active_figure == "freehand":
            self.create_line(event.x, event.y, event.x+1, event.y+1, 
                           fill=self.drawing_color, width=2)
    
    def on_drag(self, event):
        if self.active_figure == "freehand" and self.start_x is not None:
            self.create_line(self.start_x, self.start_y, event.x, event.y, 
                            fill=self.drawing_color, width=2, capstyle=tk.ROUND)
            self.start_x = event.x
            self.start_y = event.y
    
    def on_release(self, event):
        if self.start_x is None or self.start_y is None:
            return
            
        if self.active_figure == "line":
            self.create_line(self.start_x, self.start_y, event.x, event.y,
                           fill=self.drawing_color, width=2)
        elif self.active_figure == "oval":
            self.create_oval(self.start_x, self.start_y, event.x, event.y,
                           outline=self.drawing_color, width=2)
        elif self.active_figure == "rectangle":
            self.create_rectangle(self.start_x, self.start_y, event.x, event.y,
                                outline=self.drawing_color, width=2)
        elif self.active_figure == "triangle":
            mid_x = (self.start_x + event.x) // 2
            self.create_polygon(self.start_x, event.y,  # bottom left
                              event.x, event.y,       # bottom right
                              mid_x, self.start_y,    # top middle
                              outline=self.drawing_color, fill="", width=2)
        
        # Сброс координат только для не-freehand фигур
        if self.active_figure != "freehand":
            self.start_x = None
            self.start_y = None

class View(IView):
    def __init__(self, master, title):
        self.master = master
        self.master.title(title)
        
        # Создание основных фреймов согласно диаграмме
        self.color_frame = ttk.LabelFrame(master, text="Colors", padding=10)
        self.color_frame.pack(fill=tk.X, padx=5, pady=5)
        
        self.figure_frame = ttk.LabelFrame(master, text="Figures", padding=10)
        self.figure_frame.pack(fill=tk.X, padx=5, pady=5)
        
        # Виджеты для отображения выбранного цвета
        self.color_label = ttk.Label(self.color_frame, text="Selected Color: Red")
        self.color_label.pack(side=tk.LEFT, padx=5)
        
        self.color_entry = ttk.Entry(self.color_frame, width=10, state="readonly")
        self.color_entry.pack(side=tk.LEFT, padx=5)
        
        # Виджет для отображения выбранной фигуры
        self.figure_label = ttk.Label(self.figure_frame, text="Selected Figure: line")
        self.figure_label.pack(side=tk.LEFT, padx=5)
        
        # Фрейм для кнопок
        self.buttons_frame = ttk.Frame(master)
        self.buttons_frame.pack(fill=tk.X, padx=5, pady=5)
        
        # Холст для рисования
        self.canvas = Canvas(master, bg="white", width=600, height=400)
        self.canvas.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        self.controller = None
    
    def set_controller(self, controller):
        self.controller = controller
        self.canvas.controller = controller
    
    def create_color_buttons(self, colors):
        color_buttons_frame = ttk.LabelFrame(self.buttons_frame, text="Color Palette", padding=5)
        color_buttons_frame.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)
        
        for hex_code, name in colors.items():
            btn = ButtonColor(
                color_buttons_frame,
                color_hex=hex_code,
                color_name=name,
                command=lambda h=hex_code, n=name: self.controller.handle_color_button_click(h, n),
                width=3,
                relief=tk.RAISED
            )
            btn.pack(side=tk.LEFT, padx=2, pady=2)
    
    def create_figure_buttons(self, figures):
        figure_buttons_frame = ttk.LabelFrame(self.buttons_frame, text="Drawing Tools", padding=5)
        figure_buttons_frame.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)
        
        for name in figures.keys():
            btn = ButtonFigures(
                figure_buttons_frame,
                figure_name=name,
                figure_params=figures[name],
                command=lambda n=name: self.controller.handle_figure_button_click(n),
                relief=tk.RAISED
            )
            btn.pack(side=tk.LEFT, padx=2, pady=2)
    
    def update_color_display(self, color_hex, color_name):
        self.color_label.config(text=f"Selected Color: {color_name}")
        self.color_entry.config(state="normal")
        self.color_entry.delete(0, tk.END)
        self.color_entry.insert(0, color_hex)
        self.color_entry.config(state="readonly")
    
    def update_figure_display(self, figure_name):
        self.figure_label.config(text=f"Selected Figure: {figure_name}")
    
    def set_drawing_color(self, color_hex):
        self.canvas.set_drawing_color(color_hex)
    
    def set_active_figure(self, figure_name):
        self.canvas.set_active_figure(figure_name)
    
    def mainloop(self):
        self.master.mainloop()

class Controller(IController):
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.view.set_controller(self)
    
    def handle_color_button_click(self, color_hex, color_name):
        self.view.set_drawing_color(color_hex)
        self.view.update_color_display(color_hex, color_name)
    
    def handle_figure_button_click(self, figure_name):
        self.view.set_active_figure(figure_name)
        self.view.update_figure_display(figure_name)

class App(IApp):
    def __init__(self, master):
        self.master = master
        
        # Определение данных модели согласно диаграмме
        colors = {
            "#FF0000": "Red",
            "#FF7F00": "Orange", 
            "#FFFF00": "Yellow",
            "#00FF00": "Green",
            "#0000FF": "Blue",
            "#4B0082": "Indigo",
            "#9400D3": "Violet"
        }
        
        figures = {
            "freehand": "Draw freehand",
            "line": "Draw a line",
            "oval": "Draw an oval", 
            "rectangle": "Draw a rectangle",
            "triangle": "Draw a triangle"
        }
        
        # Создание компонентов MVC согласно диаграмме
        self.model = Model(colors, figures)
        self.view = View(master, "Rainbow Paint App")
        self.controller = Controller(self.model, self.view)
        
        # Инициализация представления
        self._initialize_view()
    
    def _initialize_view(self):
        """Инициализация представления с данными по умолчанию"""
        self.view.create_color_buttons(self.model.get_colors())
        self.view.create_figure_buttons(self.model.get_figures())
        
        # Установка значений по умолчанию
        default_color_hex = "#FF0000"
        default_color_name = self.model.get_color_name(default_color_hex)
        self.view.update_color_display(default_color_hex, default_color_name)
        self.view.set_drawing_color(default_color_hex)
    
    def run(self):
        self.view.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    app.run()