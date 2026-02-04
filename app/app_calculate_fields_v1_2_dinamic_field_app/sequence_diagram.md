# Диаграмма последовательности для калькулятора

```mermaid
sequenceDiagram
    actor User as Пользователь
    participant Main as Главный модуль
    participant Window as Оконное приложение
    participant App as Класс калькулятора
    participant InputFields as Поля ввода
    participant Button as Кнопка вычисления
    participant Normalizer as Нормализатор ввода
    participant NumNorm as Нормализатор чисел
    participant Validator as Валидатор чисел
    participant ResultField as Поле результата
    participant LabelError as Вывод ошибки

    User->>Main: Запуск приложения
    Main->>Window: Создание главного окна
    Main->>App: Создание экземпляра калькулятора(window, количество=10)
    
    activate App
    App->>App: Сохранение ссылки на окно
    App->>App: Сохранение количества полей = 10
    App->>Window: Установка заголовка "Калькулятор"
    App->>Window: Запрет изменения размера окна
    App->>App: Инициализация списка полей ввода
    
    loop Для i от 0 до 9 (количество=10)
        App->>InputFields: Создание поля ввода
        App->>InputFields: Размещение поля в позиции i
        App->>App: Добавление поля в список
        
        alt i < 9 (не последнее поле)
            App->>Window: Создание метки "+"
            App->>Window: Размещение метки между полями
        end
    end

    App->>Button: Создание кнопки "=" с обработчиком calculateSum()
    App->>Button: Размещение кнопки в 1 строке после всех InputFields 
    App->>ResultField: Создание поля результата (только чтение)
    App->>ResultField: Размещение в конце 1 строки после Button
    App->>LabelError: Создание метки вывода ошибки
    App->>LabelError: Размещение во 2 строке
    deactivate App
    
    Main->>Window: Запуск цикла обработки событий
    
    Note over User,Window: Приложение ожидает действий пользователя
    
    User->>InputFields: Ввод значений: "5", "10.5", "  3,2  ", "-7", "15"...
    User->>Button: Клик по кнопке "="
    Button->>App: Вызов метода calculateSum()
    
    activate App
    App->>App: Инициализация пустого списка values
    
    loop Для каждого поля в списке полей ввода (10 полей)
        Note over App,InputFields: Обработка поля #(i+1)
        
        App->>Normalizer: normalizedValue = normalizeEntry(поле)
        activate Normalizer
        Normalizer->>InputFields: value = получитьТекст(поле)
        InputFields-->>Normalizer: Возврат текста, например: "  3,2  "
        Normalizer->>NumNorm: normalizeNumber(value)
        
        activate NumNorm
        alt Значение пустое
            NumNorm-->>Normalizer: return "0"
        else Значение не пустое
            NumNorm->>NumNorm: valueClear = удалитьПробелы(value)
            Note over NumNorm: "  3,2  " -> "3,2"
            NumNorm->>NumNorm: valueClear = заменить(',', '.')
            Note over NumNorm: "3,2" -> "3.2"
            
            alt valueClear пустая после очистки
                NumNorm-->>Normalizer: return "0"
            else valueClear не пустая
                NumNorm-->>Normalizer: return "3.2"
            end
        end
        deactivate NumNorm
        
        Normalizer-->>App: Возврат "3.2"
        deactivate Normalizer
        
        App->>Validator: isValid = isNumber(normalizedValue)
        activate Validator
        Validator->>Validator: Попытка преобразовать "3.2" в число
        
        alt Преобразование успешно
            Validator->>Validator: Число получено: 3.2
            Validator-->>App: return true
        else Ошибка преобразования (например "abc")
            Validator->>Validator: Обработка исключения
            Validator-->>App: return false
            App->>LabelError: Показать ошибку("Значение #{i+1} не является числом")
            LabelError-->>User: Отображение диалога ошибки
            App->>App: Выход из метода
        end
        deactivate Validator
        
        App->>App: Добавление числа 3.2 в список values
        Note over App: values = [5.0, 10.5, 3.2, -7.0, 15.0, ...]
    end
    
    App->>App: result = суммаВсехЗначений(values)
    Note over App: result = сумма([5.0, 10.5, 3.2, -7.0, 15.0, ...])
    Note over App: Например: result = 26.7
    
    alt Результат равен целому числу
        Note over App: Если 26.7 == 26 -> False
        App->>App: Результат остается дробным числом
    else Результат целое число
        Note over App: Если result = 30.0 == 30 -> True
        App->>App: result = преобразоватьВЦелое(result) = 30
    end
    
    App->>ResultField: Разрешить редактирование поля
    App->>ResultField: Очистить содержимое поля
    Note over ResultField: Удаление старого значения
    App->>ResultField: Вставить новое значение преобразованноеВСтроку(result)
    Note over ResultField: Вставка "26.7" или "30"
    App->>ResultField: Запретить редактирование поля
    
    deactivate App
    ResultField-->>User: Отображение результата: 26.7
```

## Описание последовательности действий

1. Пользователь запускает приложение
2. Создается экземпляр CalculatorApp, который инициализирует интерфейс
3. Пользователь вводит значения в поля ввода
4. Пользователь нажимает кнопку "= и вызывается метод calculate_plus()
5. Происходит нормализация введенных значений через EntryNormalizer
6. EntryNormalizer использует NumberNormalizer для очистки строк
7. Проверяется корректность значений через NumberValidator
8. Если значения корректны, выполняется сложение и результат выводится в поле результата
9. Если значения некорректны, выводится сообщение об ошибке