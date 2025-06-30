# Полная диаграмма классов для app_rainbow_mvc.py

```mermaid
classDiagram
    class Model {
        -colors: dict
        -figures: dict
        -__init__(colors, figures)
        -get_colors() dict
        -get_color_name(hex_code) str
        -get_figures() dict
        -get_figure_params(name) tuple
    }

    class ButtonColor {
        <<tk.Button>>
        -color_hex: str
        -color_name: str
        -__init__(master, color_hex, color_name, command, **kwargs)
        -show_color(label_widget, entry_widget)
    }

    class ButtonFigures {
        <<tk.Button>>
        -figure_name: str
        -figure_params: tuple
        -__init__(master, figure_name, figure_params, command, **kwargs)
        -get_figure_name() str
        -get_figure_params() tuple
    }

    class View {
        -master: tk.Tk
        -color_frame: tk.Frame
        -figure_frame: tk.Frame
        -color_label: tk.Label
        -color_entry: tk.Entry
        -figure_label: tk.Label
        -buttons_frame: tk.Frame
        -canvas: Canvas
        -controller: Controller
        -__init__(master, title)
        -set_controller(controller)
        -create_color_buttons(colors)
        -create_figure_buttons(figures)
        -update_color_display(color_hex, color_name)
        -update_figure_display(figure_name)
        -set_drawing_color(color_hex)
        -draw_shape_on_canvas(coordinates)
        -mainloop()
    }

    class Canvas {
        <<tk.Canvas>>
        -drawing_color: str
        -start_x: int
        -start_y: int
        -last_x: int
        -last_y: int
        -controller: Controller
        -__init__(master, **kwargs)
        -set_drawing_color(color_hex)
        -draw_shape(coordinates)
        -on_press(event)
        -on_drag(event)
        -on_release(event)
    }

    class Controller {
        -model: Model
        -view: View
        -__init__(model, view)
        -handle_color_button_click(color_hex, color_name)
        -handle_figure_button_click(figure_name)
        -handle_draw_shape_request(coordinates)
    }

    class App {
        -master: tk.Tk
        -model: Model
        -view: View
        -controller: Controller
        -__init__(master)
        -run()
    }

    tk.Button <|-- ButtonColor
    tk.Button <|-- ButtonFigures
    App o-- Model
    App o-- View
    App o-- Controller
    Controller o-- Model
    Controller o-- View
    View o-- Controller
    View *-- ButtonColor : creates >
    View *-- ButtonFigures : creates >
    View *-- Canvas : creates >
    tk.Canvas <|-- Canvas
    View *-- tk.Label : creates >
    View *-- tk.Entry : creates >
    View *-- tk.Frame : creates >

    note for ButtonColor "Отображает информацию о цвете при нажатии"
    note for ButtonFigures "Устанавливает активную фигуру для рисования"
    note for View "Управляет всеми элементами интерфейса"