# Диаграмма классов для app_rainbow.py

**Примечание:** Классы и методы в коде `app_rainbow.py` теперь содержат строки документации (docstrings), описывающие их назначение и параметры. Диаграмма ниже показывает структуру классов.

```mermaid
classDiagram
    class Errors {
        +staticmethod type_error(value, type_value)
    }
    class Model {
        -__colors_data: dict
        +colors_data: dict
        +__init__(colors_data: dict)
    }
    class ButtonColor {
        <<Tkinter Button>>
        - __label: Label
        - __entry: Entry
        - __color_name: str
        + color_code: str
        + __init__(parent: Tk, label: Label, entry: Entry, color_code: str, color_name: str)
        + show_color()
    }
    class Controller {
        - __model: Model
        - __view: View
        + __init__(model: Model, view: View)
        +staticmethod print_color(button: ButtonColor)
    }
    class View {
        - __label_name: str
        - __parent: Tk
        - __controller: Controller
        + __init__(parent: Tk, label_name: str)
        + create_buttons(dict_colors: dict)
        + set_controller(controller: Controller)
        - __set_color(button: ButtonColor)
    }
    class App {
        - __root: Tk
        + __init__()
        + mainloop()
    }

    Button --|> ButtonColor
    ButtonColor ..> Errors : uses
    Controller ..> Model : uses
    Controller ..> View : uses
    Controller ..> ButtonColor : uses
    View ..> Tk : uses
    View ..> Label : uses
    View ..> Entry : uses
    View ..> ButtonColor : uses
    View ..> Controller : uses
    View ..> Errors : uses
    App ..> Tk : uses
    App ..> Model : uses
    App ..> View : uses
    App ..> Controller : uses
```