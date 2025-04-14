# Диаграмма последовательностей для процедурной версии app_rainbow.py

Эта диаграмма последовательностей описывает работу процедурной версии приложения Rainbow (строки 1-76 в файле app_rainbow.py).

```mermaid
sequenceDiagram
    actor User
    participant App as Tkinter App
    participant Buttons as Color Buttons
    participant Label as Color Name Label
    participant Entry as Color Code Entry
    
    Note over App: Инициализация приложения
    App->>App: Создание root = Tk()
    App->>App: root.title('Colors')
    App->>Label: Создание color_name = Label(text="Color name")
    Label->>App: Размещение с помощью pack()
    App->>Entry: Создание color_code = Entry(justify=CENTER)
    Entry->>Entry: insert(0, "Color code")
    Entry->>App: Размещение с помощью pack()
    
    App->>Buttons: Создание button_red с command=print_red
    App->>Buttons: Создание button_orange с command=print_orange
    App->>Buttons: Создание button_yellow с command=print_yellow
    App->>Buttons: Создание button_green с command=print_green
    App->>Buttons: Создание button_lightblue с command=print_lightblue
    App->>Buttons: Создание button_blue с command=print_blue
    App->>Buttons: Создание button_purple с command=print_purple
    
    Buttons->>App: Размещение всех кнопок с помощью pack(fill=X)
    
    App->>App: root.mainloop()
    
    Note over User, App: Взаимодействие с приложением
    
    User->>Buttons: Нажатие на кнопку red
    Buttons->>App: Вызов функции print_red()
    App->>Label: color_name.config(text="red", fg="red")
    App->>Entry: color_code.delete(0, END)
    App->>Entry: color_code.insert(0, "#ff0000")
    App->>Entry: color_code.config(bg="red")
    
    User->>Buttons: Нажатие на кнопку orange
    Buttons->>App: Вызов функции print_orange()
    App->>Label: color_name.config(text="Orange", fg="orange")
    App->>Entry: color_code.delete(0, END)
    App->>Entry: color_code.insert(0, "#ff7d00")
    App->>Entry: color_code.config(bg="orange")
    
    Note over User, App: Аналогично для других цветов
```

## Описание процедурной версии приложения

Процедурная версия приложения Rainbow имеет следующую структуру и последовательность работы:

1. **Инициализация приложения**:
   - Создается главное окно приложения с помощью `Tk()`
   - Устанавливается заголовок окна: "Colors"
   - Создаются виджеты:
     - Label для отображения названия цвета
     - Entry для отображения кода цвета
     - Семь кнопок для разных цветов (red, orange, yellow, green, lightblue, blue, purple)

2. **Функции обработки цветов**:
   - Для каждого цвета создана отдельная функция (print_red, print_orange и т.д.)
   - Каждая функция выполняет одинаковые действия, но с разными значениями цвета:
     - Изменяет текст и цвет текста в Label
     - Очищает поле Entry
     - Вставляет в поле Entry код цвета в формате HEX
     - Изменяет фоновый цвет поля Entry

3. **Взаимодействие с пользователем**:
   - При нажатии на кнопку вызывается соответствующая функция
   - Функция обновляет информацию о выбранном цвете в интерфейсе

4. **Особенности процедурного подхода**:
   - Код содержит много повторений (для каждого цвета своя функция с похожим кодом)
   - Отсутствует инкапсуляция данных
   - Глобальные переменные используются внутри функций
   - Нет разделения на модель, представление и контроллер

Эта версия приложения демонстрирует простой процедурный подход к программированию, где логика приложения реализована через набор функций, работающих с глобальными переменными.