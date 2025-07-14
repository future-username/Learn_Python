import tkinter as tk
from tkinter import colorchooser, messagebox
from typing import Dict, Tuple, Any, Optional, Callable, cast
from abc import ABCMeta
import math # Добавлен импорт math

# class TkinterABC(type(tk.Button), ABCMeta):
#     pass

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
    "Елочка": (),  # Добавляем новую фигуру
    "Звезда": ()  # Добавляем звезду
}

FIGURE_LINE = "Линия"
FIGURE_RECTANGLE = "Прямоугольник"
FIGURE_OVAL = "Овал"
FIGURE_TREE = "Елочка" # Новая константа для елочки
FIGURE_STAR = "Звезда" # Новая константа для звезды

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

    def _get_oval_points(self, x1: int, y1: int, x2: int, y2: int, segments: int = 36) -> list[float]:
        """Генерирует координаты точек для полигона, аппроксимирующего овал."""
        points = []
        # Нормализуем координаты
        rx1, ry1 = min(x1, x2), min(y1, y2)
        rx2, ry2 = max(x1, x2), max(y1, y2)

        center_x = (rx1 + rx2) / 2
        center_y = (ry1 + ry2) / 2
        radius_x = (rx2 - rx1) / 2
        radius_y = (ry2 - ry1) / 2

        if radius_x == 0 and radius_y == 0: # Точка
            return [rx1, ry1, rx1+1, ry1, rx1+1, ry1+1, rx1, ry1+1, rx1, ry1] # Маленький квадрат для точки
        if radius_x == 0 or radius_y == 0: # Линия (вертикальная или горизонтальная)
            # Возвращаем прямоугольник, который будет выглядеть как линия при width > 0
            return [rx1, ry1, rx2, ry1, rx2, ry2, rx1, ry2, rx1, ry1]

        for i in range(segments):
            angle = (2 * math.pi / segments) * i
            x = center_x + radius_x * math.cos(angle)
            y = center_y + radius_y * math.sin(angle)
            points.extend([x, y])
        # Замыкаем полигон, добавляя первую точку в конец, если она еще не там
        if points and (points[0] != points[-2] or points[1] != points[-1]):
             points.extend([points[0], points[1]])
        return points

    def _get_star_points(self, x1: int, y1: int, x2: int, y2: int, num_points: int = 100) -> list[float]:
        """Генерирует координаты точек для звезды."""
        points = []
        min_x, max_x = min(x1, x2), max(x1, x2)
        min_y, max_y = min(y1, y2), max(y1, y2)

        center_x = (min_x + max_x) / 2
        center_y = (min_y + max_y) / 2
        
        # Определяем внешний радиус как половину меньшей из сторон ограничивающего прямоугольника
        outer_radius = min(max_x - min_x, max_y - min_y) / 2
        if outer_radius == 0: # Если радиус 0, рисуем маленькую точку/квадрат
            return [center_x, center_y, center_x+1, center_y, center_x+1, center_y+1, center_x, center_y+1, center_x, center_y]
            
        inner_radius = outer_radius / 2.5 # Внутренний радиус для звезды

        for i in range(num_points * 2):
            angle = (math.pi / num_points) * i - (math.pi / 2) # Начинаем с верхней точки
            radius = outer_radius if i % 2 == 0 else inner_radius
            x = center_x + radius * math.cos(angle)
            y = center_y + radius * math.sin(angle)
            points.extend([x, y])
        
        # Замыкаем полигон
        if points:
            points.extend([points[0], points[1]])
        return points

    def set_drawing_color(self, color_hex: str):
        self.drawing_color = color_hex

    def set_active_figure(self, figure_name: str):
        self.active_figure = figure_name

    def on_press(self, event: tk.Event):
        self._start_x = event.x
        self._start_y = event.y
        # Для линий начинаем рисовать сразу (как временную линию)
        if self.active_figure == FIGURE_LINE:
            self._current_shape_id = self.create_line(
                self._start_x, self._start_y, event.x, event.y,
                fill=self.drawing_color,
                width=2,
                tags="temp_shape" # Тег для временной фигуры
            )

    def on_drag(self, event: tk.Event):
        if self._start_x is None or self._start_y is None:
            return

        if self._current_shape_id:
            self.delete(self._current_shape_id)
            self._current_shape_id = None

        temp_shape_params = {
            'tags': "temp_shape", # Тег для временной фигуры
            'width': 2,
            'fill': self.drawing_color  # Для линий используем fill вместо outline
        }
        
        active_fig = self.active_figure 

        coords: list[float] = []
        specific_params = {}

        # Координаты для полилиний различных фигур
        if active_fig == FIGURE_LINE:
            # Для линии просто передаем начальную и конечную точки
            self._current_shape_id = self.create_line(
                self._start_x, self._start_y, event.x, event.y, 
                **temp_shape_params
            )
            return
        elif active_fig == FIGURE_RECTANGLE:
            # Прямоугольник - это 4 линии
            coords = [
                self._start_x, self._start_y, event.x, self._start_y,
                event.x, self._start_y, event.x, event.y,
                event.x, event.y, self._start_x, event.y,
                self._start_x, event.y, self._start_x, self._start_y
            ]
        elif active_fig == FIGURE_OVAL:
            # Овал аппроксимируется полилинией
            points = self._get_oval_points(self._start_x, self._start_y, event.x, event.y)
            # Преобразуем список [x1, y1, x2, y2, ...] в формат для create_line
            coords = []
            for i in range(0, len(points)-2, 2):
                coords.extend([points[i], points[i+1], points[i+2], points[i+3]])
            # Добавляем соединение последней точки с первой
            if len(points) >= 4:
                coords.extend([points[-2], points[-1], points[0], points[1]])
        elif active_fig == FIGURE_TREE:
            # Для елочки во время перетаскивания рисуем ограничивающий прямоугольник
            coords = [
                self._start_x, self._start_y, event.x, self._start_y,
                event.x, self._start_y, event.x, event.y,
                event.x, event.y, self._start_x, event.y,
                self._start_x, event.y, self._start_x, self._start_y
            ]
        elif active_fig == FIGURE_STAR:
            # Для звезды во время перетаскивания рисуем ограничивающий прямоугольник
            # или можно использовать self._get_star_points для более точного временного отображения
            coords = [
                self._start_x, self._start_y, event.x, self._start_y,
                event.x, self._start_y, event.x, event.y,
                event.x, event.y, self._start_x, event.y,
                self._start_x, event.y, self._start_x, self._start_y
            ]
            # Альтернатива для временного отображения звезды:
            # star_points_temp = self._get_star_points(self._start_x, self._start_y, event.x, event.y)
            # if star_points_temp:
            #     for i in range(0, len(star_points_temp)-2, 2):
            #         coords.extend([star_points_temp[i], star_points_temp[i+1], star_points_temp[i+2], star_points_temp[i+3]])
        else:
            return

        if not coords:
            return
            
        # Все временные фигуры при перетаскивании рисуются как полилинии
        self._current_shape_id = self.create_line(coords, **temp_shape_params, **specific_params)

    def on_release(self, event: tk.Event):
        """Handle mouse button release event to finalize drawing."""
        if self._start_x is None or self._start_y is None:
            return
            
        # Delete the temporary shape
        if self._current_shape_id:
            self.delete(self._current_shape_id)
            self._current_shape_id = None
            
        # Notify controller to draw the final shape
        if self.controller:
            self.controller.handle_draw_shape_request(
                ((self._start_x, self._start_y), (event.x, event.y)),
                self.active_figure
            )
            
        # Reset starting coordinates
        self._start_x = None
        self._start_y = None

    def draw_shape(self, coordinates: Tuple[Tuple[int, int], Tuple[int, int]], figure_type: str):
        (x1, y1), (x2, y2) = coordinates
        fill_color = ""
        ask_fill = figure_type != FIGURE_LINE
        
        if ask_fill:
            if messagebox.askyesno("Заливка фигуры", f"Залить {figure_type.lower()} выбранным цветом?", parent=self):
                fill_color = self.drawing_color

        # Все фигуры рисуются как полилинии (последовательности соединенных отрезков)
        # с использованием метода create_line. Тег "shape" добавляется ко всем финальным фигурам.

        if figure_type == FIGURE_LINE:
            # Линия - это полилиния из двух точек (один сегмент).
            self.create_line(x1, y1, x2, y2, fill=self.drawing_color, width=2, tags="shape")
        elif figure_type == FIGURE_RECTANGLE:
            # Прямоугольник - это замкнутая полилиния из четырех сегментов.
            self.create_line(
                x1, y1, x2, y1, x2, y2, x1, y2, x1, y1,
                fill=self.drawing_color, width=2, tags="shape"
            )
            # Если нужна заливка, создаем дополнительный прямоугольник
            if fill_color:
                self.create_rectangle(x1, y1, x2, y2, outline="", fill=fill_color, tags="shape_fill")
        elif figure_type == FIGURE_OVAL:
            # Овал аппроксимируется полилинией.
            oval_coords = self._get_oval_points(x1, y1, x2, y2)
            if oval_coords:
                # Преобразуем список [x1, y1, x2, y2, ...] в формат для create_line
                line_coords = []
                for i in range(0, len(oval_coords)-2, 2):
                    line_coords.extend([oval_coords[i], oval_coords[i+1], oval_coords[i+2], oval_coords[i+3]])
                # Добавляем соединение последней точки с первой
                if len(oval_coords) >= 4:
                    line_coords.extend([oval_coords[-2], oval_coords[-1], oval_coords[0], oval_coords[1]])
                
                self.create_line(line_coords, fill=self.drawing_color, width=2, tags="shape")
                # Если нужна заливка, создаем дополнительный овал
                if fill_color:
                    min_x, min_y = min(x1, x2), min(y1, y2)
                    max_x, max_y = max(x1, x2), max(y1, y2)
                    self.create_oval(min_x, min_y, max_x, max_y, outline="", fill=fill_color, tags="shape_fill")
        elif figure_type == FIGURE_TREE:
            # Елочка состоит из нескольких полилиний (ствол, сегменты кроны).
            self._draw_christmas_tree(x1, y1, x2, y2, self.drawing_color, fill_color)
        elif figure_type == FIGURE_STAR:
            star_points = self._get_star_points(x1, y1, x2, y2)
            if star_points:
                # Рисуем контур звезды как полилинию
                line_coords_star = []
                for i in range(0, len(star_points)-2, 2):
                    line_coords_star.extend([star_points[i], star_points[i+1], star_points[i+2], star_points[i+3]])
                # Замыкаем контур, если он не замкнут (хотя _get_star_points уже должен это делать)
                if len(star_points) >=4 and (star_points[0] != star_points[-2] or star_points[1] != star_points[-1]):
                     line_coords_star.extend([star_points[-2], star_points[-1], star_points[0], star_points[1]])
                
                self.create_line(line_coords_star, fill=self.drawing_color, width=2, tags="shape star_outline")
                
                # Если нужна заливка, создаем дополнительный полигон
                if fill_color:
                    # self._get_star_points возвращает уже замкнутый список точек для полигона
                    self.create_polygon(star_points, outline="", fill=fill_color, tags="shape star_fill")

    def _draw_christmas_tree(self, x1: int, y1: int, x2: int, y2: int, outline_color: str, fill_color: str):
        """Рисует елочку на холсте, используя полилинии для каждого компонента."""
        min_x, max_x = min(x1, x2), max(x1, x2)
        min_y, max_y = min(y1, y2), max(y1, y2)

        width = max_x - min_x
        height = max_y - min_y

        if width == 0 or height == 0: return

        trunk_width = width / 5
        trunk_height = height / 4
        trunk_x1 = min_x + (width - trunk_width) / 2
        trunk_y1 = max_y - trunk_height
        trunk_x2 = trunk_x1 + trunk_width
        trunk_y2 = max_y
        actual_trunk_fill = fill_color if fill_color else "#A0522D" # Коричневый по умолчанию для ствола
        
        # Ствол - прямоугольная полилиния
        self.create_line(
            trunk_x1, trunk_y1, trunk_x2, trunk_y1, 
            trunk_x2, trunk_y1, trunk_x2, trunk_y2,
            trunk_x2, trunk_y2, trunk_x1, trunk_y2,
            trunk_x1, trunk_y2, trunk_x1, trunk_y1,
            fill=outline_color, width=2, tags="shape_component tree_trunk"
        )
        # Заливка ствола, если нужна
        if actual_trunk_fill:
            self.create_rectangle(
                trunk_x1, trunk_y1, trunk_x2, trunk_y2, 
                outline="", fill=actual_trunk_fill, tags="shape_component tree_trunk_fill"
            )

        crown_base_y = trunk_y1
        crown_segment_height = (crown_base_y - min_y) / 3

        if crown_segment_height <= 0: return

        # Сегменты кроны - треугольные полилинии
        crown_actual_fill = fill_color if fill_color else "" # Для кроны используем выбранный цвет или без заливки
        
        # Нижний сегмент кроны
        self.create_line(
            min_x, crown_base_y, max_x, crown_base_y,
            max_x, crown_base_y, min_x + width / 2, crown_base_y - crown_segment_height,
            min_x + width / 2, crown_base_y - crown_segment_height, min_x, crown_base_y,
            fill=outline_color, width=2, tags="shape_component tree_crown"
        )
        if crown_actual_fill:
            self.create_polygon(
                min_x, crown_base_y, max_x, crown_base_y,
                min_x + width / 2, crown_base_y - crown_segment_height,
                outline="", fill=crown_actual_fill, tags="shape_component tree_crown_fill"
            )

        # Средний сегмент кроны
        self.create_line(
            min_x + width / 6, crown_base_y - crown_segment_height * 0.8, 
            max_x - width / 6, crown_base_y - crown_segment_height * 0.8,
            max_x - width / 6, crown_base_y - crown_segment_height * 0.8,
            min_x + width / 2, min_y + crown_segment_height * 1.2,
            min_x + width / 2, min_y + crown_segment_height * 1.2,
            min_x + width / 6, crown_base_y - crown_segment_height * 0.8,
            fill=outline_color, width=2, tags="shape_component tree_crown"
        )
        if crown_actual_fill:
            self.create_polygon(
                min_x + width / 6, crown_base_y - crown_segment_height * 0.8, 
                max_x - width / 6, crown_base_y - crown_segment_height * 0.8,
                min_x + width / 2, min_y + crown_segment_height * 1.2,
                outline="", fill=crown_actual_fill, tags="shape_component tree_crown_fill"
            )

        # Верхний сегмент кроны
        self.create_line(
            min_x + width / 3, min_y + crown_segment_height * 1.5, 
            max_x - width / 3, min_y + crown_segment_height * 1.5,
            max_x - width / 3, min_y + crown_segment_height * 1.5,
            min_x + width / 2, min_y,
            min_x + width / 2, min_y,
            min_x + width / 3, min_y + crown_segment_height * 1.5,
            fill=outline_color, width=2, tags="shape_component tree_crown"
        )
        if crown_actual_fill:
            self.create_polygon(
                min_x + width / 3, min_y + crown_segment_height * 1.5, 
                max_x - width / 3, min_y + crown_segment_height * 1.5,
                min_x + width / 2, min_y,
                outline="", fill=crown_actual_fill, tags="shape_component tree_crown_fill"
            )

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
        else:
            self.handle_color_button_click(DEFAULT_DRAWING_COLOR_HEX, DEFAULT_DRAWING_COLOR_NAME)

        figures = self._model.get_figures()
        if figures:
            initial_figure_name = next(iter(figures))
            self.handle_figure_button_click(initial_figure_name)
        else:
            self.handle_figure_button_click(DEFAULT_ACTIVE_FIGURE)

    def handle_color_button_click(self, color_hex: str, color_name: str):
        self._view.update_color_display(color_hex, color_name)
        self._view.set_drawing_color(color_hex)

    def handle_figure_button_click(self, figure_name: str):
        self._view.update_figure_display(figure_name)
        if isinstance(self._view.canvas, Canvas):
            self._view.canvas.set_active_figure(figure_name)

    def handle_draw_shape_request(self, coordinates: Tuple[Tuple[int, int], Tuple[int, int]], figure_type: str):
        self._view.draw_shape_on_canvas(coordinates, figure_type)

# --- Application ---
class App(IApp):
    """Основной класс приложения, инициализирует MVC компоненты."""
    def __init__(self, root: tk.Tk):
        self.model = Model()
        self.view = View(root, DEFAULT_WINDOW_TITLE)
        self.controller = Controller(self.model, self.view)

    def run(self):
        self.view.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    app.run()