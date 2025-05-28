from abc import ABC, abstractmethod
from typing import Dict, Tuple, Any
import tkinter as tk


class IModel(ABC):
    """Интерфейс для модели данных"""
    
    @abstractmethod
    def __init__(self, colors: Dict[str, str], figures: Dict[str, Any]):
        """Инициализация модели с цветами и фигурами"""
        pass
    
    @abstractmethod
    def get_colors(self) -> Dict[str, str]:
        """Получить словарь цветов"""
        pass
    
    @abstractmethod
    def get_color_name(self, hex_code: str) -> str:
        """Получить название цвета по hex коду"""
        pass
    
    @abstractmethod
    def get_figures(self) -> Dict[str, Any]:
        """Получить словарь фигур"""
        pass
    
    @abstractmethod
    def get_figure_params(self, name: str) -> Tuple:
        """Получить параметры фигуры по имени"""
        pass


class IButtonColor(ABC):
    """Интерфейс для кнопки цвета"""
    
    @abstractmethod
    def __init__(self, master: tk.Widget, color_hex: str, color_name: str, command: callable, **kwargs):
        """Инициализация кнопки цвета"""
        pass
    
    @abstractmethod
    def show_color(self, label_widget: tk.Widget, entry_widget: tk.Widget):
        """Отобразить информацию о цвете в виджетах"""
        pass


class IButtonFigures(ABC):
    """Интерфейс для кнопки фигуры"""
    
    @abstractmethod
    def __init__(self, master: tk.Widget, figure_name: str, figure_params: Tuple, command: callable, **kwargs):
        """Инициализация кнопки фигуры"""
        pass
    
    @abstractmethod
    def get_figure_name(self) -> str:
        """Получить название фигуры"""
        pass
    
    @abstractmethod
    def get_figure_params(self) -> Tuple:
        """Получить параметры фигуры"""
        pass


class ICanvas(ABC):
    """Интерфейс для холста рисования"""
    
    @abstractmethod
    def __init__(self, master: tk.Widget, **kwargs):
        """Инициализация холста"""
        pass
    
    @abstractmethod
    def set_drawing_color(self, color_hex: str):
        """Установить цвет рисования"""
        pass

    @abstractmethod
    def draw_shape(self, coordinates: tuple[tuple[int, int]]):
        """Нарисовать фигуру по координатам методом полилиний"""
        pass


class IView(ABC):
    """Интерфейс для представления (View)"""
    
    @abstractmethod
    def __init__(self, master: tk.Tk, title: str):
        """Инициализация представления"""
        pass
    
    @abstractmethod
    def set_controller(self, controller: 'IController'):
        """Установить контроллер"""
        pass
    
    @abstractmethod
    def create_color_buttons(self, colors: Dict[str, str]):
        """Создать кнопки цветов"""
        pass
    
    @abstractmethod
    def create_figure_buttons(self, figures: Dict[str, Any]):
        """Создать кнопки фигур"""
        pass
    
    @abstractmethod
    def update_color_display(self, color_hex: str, color_name: str):
        """Обновить отображение выбранного цвета"""
        pass
    
    @abstractmethod
    def update_figure_display(self, figure_name: str):
        """Обновить отображение выбранной фигуры"""
        pass
    
    @abstractmethod
    def set_drawing_color(self, color_hex: str):
        """Установить цвет рисования на холсте"""
        pass
    
    @abstractmethod
    def draw_shape_on_canvas(self, coordinates: Tuple):
        """Нарисовать фигуру на холсте по координатам"""
        pass

    @abstractmethod
    def mainloop(self):
        """Запустить главный цикл интерфейса"""
        pass


class IController(ABC):
    """Интерфейс для контроллера"""
    
    @abstractmethod
    def __init__(self, model: IModel, view: IView):
        """Инициализация контроллера"""
        pass
    
    @abstractmethod
    def handle_color_button_click(self, color_hex: str, color_name: str):
        """Обработать нажатие кнопки цвета"""
        pass
    
    @abstractmethod
    def handle_figure_button_click(self, figure_name: str):
        """Обработать нажатие кнопки фигуры"""
        pass

    @abstractmethod
    def handle_draw_shape_request(self, coordinates: Tuple):
        """Обработать запрос на рисование фигуры по координатам"""
        pass


class IApp(ABC):
    """Интерфейс для главного приложения"""
    
    @abstractmethod
    def __init__(self, master: tk.Tk):
        """Инициализация приложения"""
        pass
    
    @abstractmethod
    def run(self):
        """Запустить приложение"""
        pass


# Дополнительные интерфейсы для событий
class IEventHandler(ABC):
    """Интерфейс для обработчика событий"""
    
    @abstractmethod
    def on_press(self, event):
        """Обработать нажатие мыши"""
        pass
    
    @abstractmethod
    def on_drag(self, event):
        """Обработать перетаскивание мыши"""
        pass
    
    @abstractmethod
    def on_release(self, event):
        """Обработать отпускание мыши"""
        pass


class IDrawable(ABC):
    """Интерфейс для объектов, которые можно рисовать"""
    
    @abstractmethod
    def draw(self, canvas: tk.Canvas, start_x: int, start_y: int, end_x: int, end_y: int, color: str):
        """Нарисовать объект на холсте"""
        pass


class IColorProvider(ABC):
    """Интерфейс для поставщика цветов"""
    
    @abstractmethod
    def get_default_colors(self) -> Dict[str, str]:
        """Получить набор цветов по умолчанию"""
        pass
    
    @abstractmethod
    def validate_color(self, color_hex: str) -> bool:
        """Проверить корректность hex цвета"""
        pass


class IFigureProvider(ABC):
    """Интерфейс для поставщика фигур"""
    
    @abstractmethod
    def get_default_figures(self) -> Dict[str, Any]:
        """Получить набор фигур по умолчанию"""
        pass
    
    @abstractmethod
    def validate_figure(self, figure_name: str) -> bool:
        """Проверить корректность названия фигуры"""
        pass