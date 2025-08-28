```mermaid
   classDiagram
    %% Направление для читаемости
    direction LR

    %% === Внешние базовые классы фреймворка ===
    class TkButton
    <<framework>> TkButton
    class TkCanvas
    <<framework>> TkCanvas

    %% === Модель ===
    class Model {
        +__init__(colors: Dict[str, str], figures: Dict[str, Any])
        -__colors: Dict[str, str]
        -__figures: Dict[str, Any]
        +get_colors() Dict[str, str]
        +get_color_name(hex_code: str) str
        +get_figures() Dict[str, Any]
        +get_figure_params(name: str) Tuple
    }

    %% === Представление ===
    class View {
        +__init__(master)
        -__master
        -__controller
        -__canvas: Canvas
        +set_controller(controller)
        +create_color_buttons(colors)
        +create_figure_buttons(figures)
        +update_color_display(color_hex, color_name)
        +update_figure_display(figure_name)
        +set_drawing_color(color_hex)
        +set_active_figure(figure_name)
        +mainloop()
    }

    class Canvas {
        +__init__(parent, width: int, height: int)
        -__drawing_color: str
        -__current_shape: str
        -__start_x: int
        -__start_y: int
        -__current_shape_id: int
        -__shapes: dict[int, list[float]]
        +set_drawing_color(color_hex: str)
        +set_shape(shape: str)
        -__on_press(event)
        -__on_drag(event)
    }

    class ButtonColor {
        +__init__(parent, color_hex: str, color_name: str)
        -__color_hex: str
        -__color_name: str
        +show_color(label_widget, entry_widget)
    }

    class ButtonFigures {
        +__init__(parent, figure_name: str, figure_params: Tuple)
        -__figure_name: str
        -__figure_params: Tuple
        +get_figure_name() str
        +get_figure_params() Tuple
    }

    %% === Контроллер ===
    class Controller {
        +__init__(model: Model, view: View)
        -__model: Model
        -__view: View
        +handle_color_button_click(color_hex, color_name)
        +handle_figure_button_click(figure_name)
    }

    %% === Приложение ===
    class App {
        +__init__(master)
        -__model: Model
        -__view: View
        -__controller: Controller
        +run()
        -__initialize_view_components()
    }

    %% === Вспомогательные функции ===
    class UtilityFunctions {
        <<static>>
        +get_text_color_for_bg(hex_color: str) str
    }

    %% === Наследование (треугольная стрелка) ===
    ButtonColor --|> TkButton
    ButtonFigures --|> TkButton
    Canvas --|> TkCanvas

    %% === Композиция: жёсткая "часть-целое" (закрашенный ромб) ===
    App "1" *-- "1" Model
    App "1" *-- "1" View
    App "1" *-- "1" Controller
    View "1" *-- "1" Canvas
    View "1" *-- "0..*" ButtonColor
    View "1" *-- "0..*" ButtonFigures

    %% === Агрегация: владение без жизненного цикла (полый ромб) ===
    Controller "1" o-- "1" Model
    Controller "1" o-- "1" View

    %% === Зависимость: пунктир (использование) ===
    Model ..> UtilityFunctions : uses
    View ..> Controller : set_controller
