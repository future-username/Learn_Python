import tkinter as tk
from typing import Optional, Any

colors = {
    "red": "#ff0000",
    "orange": "#ff7d00",
    "yellow": "#ffff00",
    "green": "#00ff00",
    "lightblue": "#007dff",
    "blue": "#0000ff",
    "purple": "#7d00ff"
}

class CanvasWidget(tk.Canvas):
    """Виджет холста для рисования.

    Позволяет пользователю рисовать линии на холсте с помощью мыши.
    """
    def __init__(self, parent: tk.Misc, **kwargs: Any) -> None:
        """Инициализирует CanvasWidget.

        Args:
            parent: Родительский виджет.
            **kwargs: Дополнительные аргументы для tk.Canvas.
        """
        super().__init__(parent, bg='white', **kwargs)
        self.bind("<B1-Motion>", self.paint)
        self.bind("<ButtonRelease-1>", self.reset)
        self.old_x: Optional[int] = None
        self.old_y: Optional[int] = None
        self.line_color = "black"

    def paint(self, event: tk.Event) -> None:
        """Обрабатывает событие движения мыши с зажатой левой кнопкой.

        Рисует линию от предыдущей позиции до текущей.

        Args:
            event: Событие мыши.
        """
        if self.old_x is not None and self.old_y is not None:
            self.create_line(self.old_x, self.old_y, event.x, event.y,
                               width=2, fill=self.line_color, capstyle=tk.ROUND,
                               smooth=tk.TRUE, splinesteps=36)
        self.old_x = event.x
        self.old_y = event.y

    def reset(self, event: tk.Event) -> None:
        """Обрабатывает событие отпускания левой кнопки мыши.

        Сбрасывает предыдущие координаты.

        Args:
            event: Событие мыши.
        """
        self.old_x = None
        self.old_y = None

    def set_color(self, color: str) -> None:
        """Устанавливает цвет линии.

        Args:
            color: Цвет линии.
        """
        self.line_color = color

class App(tk.Tk):
    """Главное окно приложения.

    Содержит виджет CanvasWidget и кнопки выбора цвета.
    """
    def __init__(self, colors_data: dict) -> None:
        """Инициализирует главное окно приложения.

        Args:
            colors_data: Словарь с данными цветов.
        """
        super().__init__()
        self.title("Приложение для рисования")
        self.geometry("400x300")

        self.canvas_widget: CanvasWidget = CanvasWidget(self)
        self.canvas_widget.pack(fill=tk.BOTH, expand=True)

        self.create_color_buttons(colors_data)

    def create_color_buttons(self, colors_data: dict) -> None:
        """Создает кнопки для выбора цвета.

        Args:
            colors_data: Словарь с данными цветов.
        """
        for color_name, color_code in colors_data.items():
            button = tk.Button(self, text=color_name, bg=color_code,
                               command=lambda c=color_name: self.canvas_widget.set_color(c))
            button.pack(fill=tk.X)

if __name__ == '__main__':
    app = App(colors)
    app.mainloop()