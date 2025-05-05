import tkinter as tk
from tkinter import ttk

# Словарь цветов (Модель данных)
COLORS = {
    "#ff0000": "Красный",
    "#ff7d00": "Оранжевый",
    "#ffff00": "Желтый",
    "#00ff00": "Зеленый",
    "#007dff": "Голубой",
    "#0000ff": "Синий",
    "#7d00ff": "Фиолетовый"
}

class Model:
    """Модель данных приложения."""
    def __init__(self, colors):
        self.colors = colors

    def get_colors(self):
        return self.colors

    def get_color_name(self, hex_code):
        return self.colors.get(hex_code, "Неизвестный цвет")

class ButtonColor(tk.Button):
    """Специализированная кнопка для отображения цвета."""
    def __init__(self, master=None, color_hex="#ffffff", color_name="white", command=None, **kwargs):
        super().__init__(master, text=color_name, bg=color_hex, command=lambda: command(self), **kwargs)
        self.color_hex = color_hex
        self.color_name = color_name

    def show_color(self, label_widget, entry_widget):
        """Обновляет метку и поле ввода при нажатии кнопки."""
        label_widget.config(text=self.color_name, fg=self.color_hex)
        entry_widget.delete(0, tk.END)
        entry_widget.insert(0, self.color_hex)
        entry_widget.config(bg=self.color_hex)
        # Определяем цвет текста в поле ввода для лучшей читаемости
        try:
            r, g, b = tuple(int(self.color_hex.lstrip('#')[i:i+2], 16) for i in (0, 2, 4))
            brightness = (r * 299 + g * 587 + b * 114) / 1000
            text_color = "#000000" if brightness > 128 else "#ffffff"
            entry_widget.config(fg=text_color)
        except ValueError:
            entry_widget.config(fg="#000000") # По умолчанию черный текст

class View:
    """Представление (GUI) приложения."""
    def __init__(self, master, title="Радуга MVC с рисованием"):
        self.master = master
        self.master.title(title)
        self.master.geometry("400x450") # Увеличим размер окна

        # --- Верхняя часть для выбора цвета ---
        self.color_frame = tk.Frame(self.master)
        self.color_frame.pack(pady=10)

        self.color_label = tk.Label(self.color_frame, text="Название цвета", font=("Arial", 14))
        self.color_label.pack()

        self.color_entry = tk.Entry(self.color_frame, justify='center', font=("Arial", 12), width=15)
        self.color_entry.pack(pady=5)

        self.buttons_frame = tk.Frame(self.master)
        self.buttons_frame.pack(pady=5, fill=tk.X, padx=10)

        # --- Холст для рисования ---
        self.canvas = tk.Canvas(self.master, bg='white', width=380, height=250)
        self.canvas.pack(pady=10, padx=10)
        self.canvas.bind("<B1-Motion>", self.paint)
        self.drawing_color = "#000000" # Начальный цвет рисования - черный
        self.last_x, self.last_y = None, None

        self.controller = None

    def set_controller(self, controller):
        self.controller = controller

    def create_buttons(self, colors):
        """Создает кнопки для каждого цвета."""
        if not self.controller:
            print("Ошибка: Контроллер не установлен для View")
            return

        # Распределяем кнопки по рядам для лучшего вида
        row_frame = None
        buttons_per_row = 4
        for i, (hex_code, name) in enumerate(colors.items()):
            if i % buttons_per_row == 0:
                row_frame = tk.Frame(self.buttons_frame)
                row_frame.pack(fill=tk.X)
            button = ButtonColor(row_frame, color_hex=hex_code, color_name=name,
                                 command=self.controller.handle_button_click, width=10)
            # Используем pack с side=tk.LEFT и expand=True для равномерного распределения
            button.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=2, pady=2)

    def update_color_display(self, button_widget):
        """Обновляет отображение цвета и устанавливает цвет рисования."""
        button_widget.show_color(self.color_label, self.color_entry)
        self.set_drawing_color(button_widget.color_hex)

    def set_drawing_color(self, color_hex):
        """Устанавливает текущий цвет для рисования."""
        self.drawing_color = color_hex
        # Можно добавить визуальный индикатор текущего цвета рисования, если нужно

    def paint(self, event):
        """Обработчик события рисования на холсте."""
        x, y = event.x, event.y
        if self.last_x and self.last_y:
            self.canvas.create_line(self.last_x, self.last_y, x, y,
                                    fill=self.drawing_color, width=2, capstyle=tk.ROUND,
                                    smooth=tk.TRUE)
        self.last_x = x
        self.last_y = y

    # Сброс last_x, last_y при отпускании кнопки мыши
    def reset_last_pos(self, event=None):
        self.last_x, self.last_y = None, None

    def mainloop(self):
        # Добавляем сброс координат при отпускании ЛКМ
        self.master.bind("<ButtonRelease-1>", self.reset_last_pos)
        self.master.mainloop()

class Controller:
    """Контроллер, связывающий Модель и Представление."""
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.view.set_controller(self)
        self.view.create_buttons(self.model.get_colors())

    def handle_button_click(self, button_widget):
        """Обрабатывает нажатие кнопки цвета."""
        # Логика обновления View (включая цвет рисования) теперь полностью в View
        self.view.update_color_display(button_widget)

class App:
    """Основной класс приложения."""
    def __init__(self, master):
        self.master = master
        self.model = Model(COLORS)
        self.view = View(self.master)
        self.controller = Controller(self.model, self.view)

    def run(self):
        self.view.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    app.run()