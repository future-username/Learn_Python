```mermaid
sequenceDiagram
    participant User
    participant View
    participant Controller
    participant Model
    participant Canvas

    %% === Выбор цвета ===
    User->>View: Нажимает кнопку цвета
    View->>Controller: handle_color_button_click(hex, name)
    Controller->>View: set_drawing_color(hex)
    Controller->>View: update_color_display(hex, name)
    View->>Canvas: set_drawing_color(hex)

    %% === Выбор фигуры ===
    User->>View: Нажимает кнопку фигуры
    View->>Controller: handle_figure_button_click(name)
    Controller->>View: set_active_figure(name)
    Controller->>View: update_figure_display(name)
    View->>Canvas: set_shape(name)

    %% === Рисование на холсте ===
    User->>Canvas: Нажимает и перетаскивает мышь
    Canvas->>Canvas: __on_press(event)
    Canvas->>Canvas: __on_drag(event)
    Canvas->>Canvas: create_line(points, color)
