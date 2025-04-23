# Диаграмма последовательностей: Внутреннее взаимодействие классов Rainbow App

Эта диаграмма иллюстрирует взаимодействие между классами, определенными непосредственно в файле `app_rainbow.py` (строки 177-309), во время инициализации приложения и обработки нажатия кнопки. Импортированные классы (например, из `tkinter`) не показаны.

```mermaid
sequenceDiagram
    actor User
    participant App
    participant Model
    participant View
    participant Controller
    participant ButtonColor

    %% Инициализация приложения (внутренние классы)
    App->>Model: __init__(colors)
    activate Model
    Model-->>App: Экземпляр Model
    deactivate Model

    App->>View: __init__(root, 'Colors')
    activate View
    View-->>App: Экземпляр View
    deactivate View

    App->>Controller: __init__(model, view)
    activate Controller
    Controller->>View: create_buttons(model.colors_data)
    activate View
    loop для каждого цвета
        View->>ButtonColor: __init__(parent, label, entry, color_code, color_name)
        activate ButtonColor
        ButtonColor-->>View: Экземпляр ButtonColor
        deactivate ButtonColor
        View->>ButtonColor: config(command=lambda)
    end
    View-->>Controller: Кнопки созданы
    deactivate View
    Controller-->>App: Экземпляр Controller
    deactivate Controller

    App->>View: set_controller(controller)
    activate View
    View-->>App: Контроллер установлен
    deactivate View

    %% Обработка нажатия кнопки (внутренние классы)
    User->>ButtonColor: click()
    ButtonColor->>View: __set_color(self)
    activate View
    View->>Controller: print_color(button)
    activate Controller
    Controller->>ButtonColor: show_color()
    activate ButtonColor
    ButtonColor-->>Controller: Цвет отображен
    deactivate ButtonColor
    Controller-->>View: Обработка завершена
    deactivate Controller
    View-->>ButtonColor: Событие обработано
    deactivate View
```

## Описание диаграммы

Диаграмма показывает следующие шаги:

1.  **Инициализация**: `App` создает экземпляры `Model`, `View` и `Controller`. `Controller` затем поручает `View` создать кнопки (`ButtonColor`).
2.  **Создание кнопок**: `View` создает экземпляры `ButtonColor` для каждого цвета и настраивает их обработчики событий.
3.  **Установка контроллера**: `App` передает ссылку на `Controller` в `View`.
4.  **Нажатие кнопки**: `ButtonColor` вызывает метод `__set_color` в `View`. `View` делегирует обработку `Controller` (метод `print_color`). `Controller` вызывает метод `show_color` у соответствующего `ButtonColor` для обновления интерфейса.

Класс `Errors` не участвует в этих потоках и поэтому не показан на диаграмме.