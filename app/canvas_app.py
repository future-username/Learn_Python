import tkinter as tk
from typing import Optional, Any

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

    def paint(self, event: tk.Event) -> None:
        """Обрабатывает событие движения мыши с зажатой левой кнопкой.

        Рисует линию от предыдущей позиции до текущей.

        Args:
            event: Событие мыши.
        """
        if self.old_x is not None and self.old_y is not None:
            self.create_line(self.old_x, self.old_y, event.x, event.y,
                               width=2, fill='black', capstyle=tk.ROUND,
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

class App(tk.Tk):
    """Главное окно приложения.

    Содержит виджет CanvasWidget.
    """
    def __init__(self) -> None:
        """Инициализирует главное окно приложения."""
        super().__init__()
        self.title("Приложение для рисования")
        self.geometry("400x300")

        self.canvas_widget: CanvasWidget = CanvasWidget(self)
        self.canvas_widget.pack(fill=tk.BOTH, expand=True)

if __name__ == '__main__':
    app = App()
    app.mainloop()