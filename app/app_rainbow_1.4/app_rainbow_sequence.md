# Диаграмма последовательностей для приложения Rainbow (на основе MVC)

```mermaid
sequenceDiagram
    participant User as Пользователь
    participant App as Приложение
    participant Model as Модель
    participant View as Представление
    participant Controller as Контроллер
    participant ButtonColor as КнопкаЦвета
    participant Canvas as Холст

    %% Инициализация приложения
    User->>App: Запуск приложения (run())
    activate App
    App->>App: __init__(master: Tk)
    App->>Model: создание Model(colors)
    activate Model
    Model-->>App: экземпляр Model
    deactivate Model

    App->>View: создание View(master, title)
    activate View
    View->>View: создание основных фреймов
    View->>View: создание color_label, color_entry
    View->>Canvas: создание Canvas(parent, ...)
    activate Canvas
    Canvas-->>View: экземпляр Canvas
    deactivate Canvas
    View->>View: привязка событий мыши к Canvas.paint() и Canvas.reset_last_pos()
    View-->>App: экземпляр View
    deactivate View

    App->>Controller: создание Controller(model, view)
    activate Controller
    Controller-->>App: экземпляр Controller
    deactivate Controller

    App->>View: set_controller(controller)
    activate View
    View->>View: self.controller = controller
    View-->>App: контроллер установлен
    deactivate View

    Controller->>View: create_buttons(model.get_colors())
    activate View
    loop для каждого цвета в model.get_colors()
        View->>ButtonColor: создание ButtonColor(parent, color_hex, color_name, command=lambda...)
        activate ButtonColor
        ButtonColor-->>View: экземпляр ButtonColor
        deactivate ButtonColor
        View->>ButtonColor: button.config(command=lambda b=button: controller.handle_button_click(b))
    end
    View-->>Controller: кнопки созданы
    deactivate View

    %% Обработка нажатия кнопки цвета
    User->>ButtonColor: нажатие на кнопку
    activate ButtonColor
    ButtonColor->>Controller: handle_button_click(self) (через lambda)
    deactivate ButtonColor
    activate Controller
    Controller->>View: update_color_display(button_widget: ButtonColor)
    activate View
    View->>ButtonColor: button_widget.show_color(self.color_label, self.color_entry)
    activate ButtonColor
    ButtonColor->>View: (обновление Label.config, Entry.delete/insert/config)
    deactivate ButtonColor
    View-->>Controller: отображение цвета обновлено
    deactivate View

    Controller->>View: set_drawing_color(button_widget.color_hex)
    activate View
    View->>Canvas: set_drawing_color(color_hex)
    activate Canvas
    Canvas-->>View: цвет для рисования установлен
    deactivate Canvas
    View-->>Controller: цвет для рисования передан Холсту
    deactivate View
    deactivate Controller

    %% Рисование на холсте
    User->>Canvas: движение мыши с зажатой кнопкой (событие <B1-Motion>)
    activate Canvas
    Canvas->>Canvas: paint(event)
    Canvas->>Canvas: self.last_x, self.last_y = event.x, event.y
    Canvas-->>User: линия нарисована
    deactivate Canvas

    User->>Canvas: отпускание кнопки мыши (событие <ButtonRelease-1>)
    activate Canvas
    Canvas->>Canvas: reset_last_pos(event)
    Canvas->>Canvas: self.last_x, self.last_y = None, None
    Canvas-->>User: позиция сброшена
    deactivate Canvas