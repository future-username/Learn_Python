# Диаграмма последовательности для калькулятора

## Часть 1: Инициализация приложения

```mermaid
sequenceDiagram
    actor User as Пользователь
    participant Main as Главный модуль
    participant Window as Оконное приложение
    participant AppPlus as Калькулятор сложения
    participant AppMinus as Калькулятор вычитания

    User->>Main: Запуск приложения
    Main->>Window: Создание главного окна
    Main->>Window: Установка заголовка "Калькулятор"
    Main->>Window: Запрет изменения размера окна
    
    Main->>AppPlus: Создание экземпляра калькулятора сложения(window, количество=10)
    activate AppPlus
    AppPlus->>AppPlus: Сохранение ссылки на окно
    AppPlus->>AppPlus: Сохранение количества полей = 10
    deactivate AppPlus
    
    Main->>AppMinus: Создание экземпляра калькулятора вычитания(window, количество=10)
    activate AppMinus
    AppMinus->>AppMinus: Сохранение ссылки на окно
    AppMinus->>AppMinus: Сохранение количества полей = 10
    deactivate AppMinus
    
    Main->>Window: Запуск цикла обработки событий
    
    Note over User,Window: Приложение ожидает действий пользователя
```

## Часть 2: Создание интерфейса для операции сложения

```mermaid
sequenceDiagram
    participant AppPlus as Калькулятор сложения
    participant Window as Оконное приложение
    participant InputFields as Поля ввода (сложение)
    participant Button as Кнопка вычисления (сложение)
    participant ResultField as Поле результата (сложение)
    participant LabelError as Вывод ошибки (сложение)

    activate AppPlus
    AppPlus->>AppPlus: Инициализация списка полей ввода для сложения
    
    loop Для i от 0 до 9 (количество=10)
        AppPlus->>InputFields: Создание поля ввода
        AppPlus->>InputFields: Размещение поля в позиции i
        AppPlus->>AppPlus: Добавление поля в список
        
        alt i < 9 (не последнее поле)
            AppPlus->>Window: Создание метки "+"
            AppPlus->>Window: Размещение метки между полями
        end
    end
    
    AppPlus->>Button: Создание кнопки "=" с обработчиком calculate_plus()
    AppPlus->>Button: Размещение кнопки в одной строке после всех InputFields 
    AppPlus->>ResultField: Создание поля результата (только чтение)
    AppPlus->>ResultField: Размещение в конце строки после Button
    AppPlus->>LabelError: Создание метки вывода ошибки
    AppPlus->>LabelError: Размещение в следующей строке
    deactivate AppPlus
```

## Часть 3: Создание интерфейса для операции вычитания

```mermaid
sequenceDiagram
    participant AppMinus as Калькулятор вычитания
    participant Window as Оконное приложение
    participant InputFieldsMinus as Поля ввода (вычитание)
    participant ButtonMinus as Кнопка вычисления (вычитание)
    participant ResultFieldMinus as Поле результата (вычитание)
    participant LabelErrorMinus as Вывод ошибки (вычитание)

    activate AppMinus
    AppMinus->>AppMinus: Инициализация списка полей ввода для вычитания
    
    loop Для i от 0 до 9 (количество=10)
        AppMinus->>InputFieldsMinus: Создание поля ввода
        AppMinus->>InputFieldsMinus: Размещение поля в позиции i
        AppMinus->>AppMinus: Добавление поля в список
        
        alt i < 9 (не последнее поле)
            AppMinus->>Window: Создание метки "-"
            AppMinus->>Window: Размещение метки между полями
        end
    end
    
    AppMinus->>ButtonMinus: Создание кнопки "=" с обработчиком calculate_minus()
    AppMinus->>ButtonMinus: Размещение кнопки в одной строке после всех InputFieldsMinus 
    AppMinus->>ResultFieldMinus: Создание поля результата (только чтение)
    AppMinus->>ResultFieldMinus: Размещение в конце строки после ButtonMinus
    AppMinus->>LabelErrorMinus: Создание метки вывода ошибки
    AppMinus->>LabelErrorMinus: Размещение в следующей строке
    deactivate AppMinus
```

## Часть 4: Обработка операции сложения

```mermaid
sequenceDiagram
    actor User as Пользователь
    participant InputFields as Поля ввода (сложение)
    participant Button as Кнопка вычисления (сложение)
    participant AppPlus as Калькулятор сложения
    participant Normalizer as Нормализатор ввода
    participant NumNorm as Нормализатор чисел
    participant Validator as Валидатор чисел
    participant ResultField as Поле результата (сложение)
    participant LabelError as Вывод ошибки (сложение)

    User->>InputFields: Ввод значений для сложения: "5", "10.5", "  3,2  ", "-7", "15"...
    User->>Button: Клик по кнопке "=" (сложение)
    Button->>AppPlus: Вызов метода calculate_plus()
    
    activate AppPlus
    AppPlus->>AppPlus: Инициализация пустого списка values
    
    loop Для каждого поля в списке полей ввода сложения (10 полей)
        Note over AppPlus,InputFields: Обработка поля #(i+1)
        
        AppPlus->>Normalizer: normalizedValue = normalizeEntry(поле)
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
        
        Normalizer-->>AppPlus: Возврат "3.2"
        deactivate Normalizer
        
        AppPlus->>Validator: isValid = isNumber(normalizedValue)
        activate Validator
        Validator->>Validator: Попытка преобразовать "3.2" в число
        
        alt Преобразование успешно
            Validator->>Validator: Число получено: 3.2
            Validator-->>AppPlus: return true
        else Ошибка преобразования (например "abc")
            Validator->>Validator: Обработка исключения
            Validator-->>AppPlus: return false
            AppPlus->>LabelError: Показать ошибку("Значение #{i+1} не является числом")
            LabelError-->>User: Отображение диалога ошибки
            AppPlus->>AppPlus: Выход из метода
        end
        deactivate Validator
        
        AppPlus->>AppPlus: Добавление числа 3.2 в список values
        Note over AppPlus: values = [5.0, 10.5, 3.2, -7.0, 15.0, ...]
    end
    
    AppPlus->>AppPlus: result = суммаВсехЗначений(values)
    Note over AppPlus: result = сумма([5.0, 10.5, 3.2, -7.0, 15.0, ...])
    Note over AppPlus: Например: result = 26.7
    
    alt Результат равен целому числу
        Note over AppPlus: Если 26.7 == 26 -> False
        AppPlus->>AppPlus: Результат остается дробным числом
    else Результат целое число
        Note over AppPlus: Если result = 30.0 == 30 -> True
        AppPlus->>AppPlus: result = преобразоватьВЦелое(result) = 30
    end
    
    AppPlus->>ResultField: Разрешить редактирование поля
    AppPlus->>ResultField: Очистить содержимое поля
    Note over ResultField: Удаление старого значения
    AppPlus->>ResultField: Вставить новое значение преобразованноеВСтроку(result)
    Note over ResultField: Вставка "26.7" или "30"
    AppPlus->>ResultField: Запретить редактирование поля
    
    deactivate AppPlus
    ResultField-->>User: Отображение результата сложения: 26.7
```

## Часть 5: Обработка операции вычитания

```mermaid
sequenceDiagram
    actor User as Пользователь
    participant InputFieldsMinus as Поля ввода (вычитание)
    participant ButtonMinus as Кнопка вычисления (вычитание)
    participant AppMinus as Калькулятор вычитания
    participant Normalizer as Нормализатор ввода
    participant NumNorm as Нормализатор чисел
    participant Validator as Валидатор чисел
    participant ResultFieldMinus as Поле результата (вычитание)
    participant LabelErrorMinus as Вывод ошибки (вычитание)

    User->>InputFieldsMinus: Ввод значений для вычитания: "100", "25.5", "  10,3  ", "5", "2.2"...
    User->>ButtonMinus: Клик по кнопке "=" (вычитание)
    ButtonMinus->>AppMinus: Вызов метода calculate_minus()
    
    activate AppMinus
    AppMinus->>AppMinus: Инициализация пустого списка values
    
    loop Для каждого поля в списке полей ввода вычитания (10 полей)
        Note over AppMinus,InputFieldsMinus: Обработка поля #(i+1)
        
        AppMinus->>Normalizer: normalizedValue = normalizeEntry(поле)
        activate Normalizer
        Normalizer->>InputFieldsMinus: value = получитьТекст(поле)
        InputFieldsMinus-->>Normalizer: Возврат текста, например: "  10,3  "
        Normalizer->>NumNorm: normalizeNumber(value)
        
        activate NumNorm
        alt Значение пустое
            NumNorm-->>Normalizer: return "0"
        else Значение не пустое
            NumNorm->>NumNorm: valueClear = удалитьПробелы(value)
            Note over NumNorm: "  10,3  " -> "10,3"
            NumNorm->>NumNorm: valueClear = заменить(',', '.')
            Note over NumNorm: "10,3" -> "10.3"
            
            alt valueClear пустая после очистки
                NumNorm-->>Normalizer: return "0"
            else valueClear не пустая
                NumNorm-->>Normalizer: return "10.3"
            end
        end
        deactivate NumNorm
        
        Normalizer-->>AppMinus: Возврат "10.3"
        deactivate Normalizer
        
        AppMinus->>Validator: isValid = isNumber(normalizedValue)
        activate Validator
        Validator->>Validator: Попытка преобразовать "10.3" в число
        
        alt Преобразование успешно
            Validator->>Validator: Число получено: 10.3
            Validator-->>AppMinus: return true
        else Ошибка преобразования (например "abc")
            Validator->>Validator: Обработка исключения
            Validator-->>AppMinus: return false
            AppMinus->>LabelErrorMinus: Показать ошибку("Значение #{i+1} не является числом")
            LabelErrorMinus-->>User: Отображение диалога ошибки
            AppMinus->>AppMinus: Выход из метода
        end
        deactivate Validator
        
        AppMinus->>AppMinus: Добавление числа 10.3 в список values
        Note over AppMinus: values = [100.0, 25.5, 10.3, 5.0, 2.2, ...]
    end
    
    AppMinus->>AppMinus: result = первоеЗначение - суммаОстальных(values)
    Note over AppMinus: result = values[0] - (values[1] + values[2] + ... + values[n])
    Note over AppMinus: Например: result = 100.0 - (25.5 + 10.3 + 5.0 + 2.2 + ...) = 57.0
    
    alt Результат равен целому числу
        Note over AppMinus: Если 57.0 == 57 -> True
        AppMinus->>AppMinus: result = преобразоватьВЦелое(result) = 57
    else Результат дробное число
        Note over AppMinus: Если result = 57.3 != 57
        AppMinus->>AppMinus: Результат остается дробным числом
    end
    
    AppMinus->>ResultFieldMinus: Разрешить редактирование поля
    AppMinus->>ResultFieldMinus: Очистить содержимое поля
    Note over ResultFieldMinus: Удаление старого значения
    AppMinus->>ResultFieldMinus: Вставить новое значение преобразованноеВСтроку(result)
    Note over ResultFieldMinus: Вставка "57" или "57.3"
    AppMinus->>ResultFieldMinus: Запретить редактирование поля
    
    deactivate AppMinus
    ResultFieldMinus-->>User: Отображение результата вычитания: 57
```

## Описание последовательности действий

### Инициализация (Часть 1)
1. Пользователь запускает приложение
2. Создается главное окно
3. **Создается первый экземпляр CalculatorApp для сложения** (AppPlus)
4. **Создается второй экземпляр CalculatorApp для вычитания** (AppMinus)
5. Настраиваются базовые параметры окна

### Создание интерфейса сложения (Часть 2)
1. **Экземпляр AppPlus** создает 10 полей ввода с метками "+" между ними
2. Добавляется кнопка "=" с обработчиком calculate_plus()
3. Создается поле результата и метка ошибки для сложения

### Создание интерфейса вычитания (Часть 3)
1. **Экземпляр AppMinus** создает 10 полей ввода с метками "-" между ними
2. Добавляется кнопка "=" с обработчиком calculate_minus()
3. Создается поле результата и метка ошибки для вычитания

### Обработка сложения (Часть 4)
1. Пользователь вводит значения в поля сложения и нажимает кнопку "="
2. **Экземпляр AppPlus** обрабатывает запрос через calculate_plus()
3. Происходит нормализация через EntryNormalizer и NumberNormalizer
4. Валидация значений через NumberValidator
5. Вычисление суммы всех значений
6. Вывод результата в поле результата сложения

### Обработка вычитания (Часть 5)
1. Пользователь вводит значения в поля вычитания и нажимает кнопку "="
2. **Экземпляр AppMinus** обрабатывает запрос через calculate_minus()
3. Происходит нормализация через EntryNormalizer и NumberNormalizer
4. Валидация значений через NumberValidator
5. Вычисление: первое значение минус сумма остальных
6. Вывод результата в поле результата вычитания