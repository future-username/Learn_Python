```mermaid
sequenceDiagram
    participant User
    participant CalcApp as CalculatorApp
    participant EntryNorm as EntryNormalizer
    participant NumNorm as NumberNormalizer
    participant NumValid as NumberValidator
    
    User->>CalcApp: Ввод значений в поля
    User->>CalcApp: Нажатие кнопки "="
    activate CalcApp
    
    loop для каждого поля ввода
        CalcApp->>EntryNorm: normalize_entries(entry)
        activate EntryNorm
        EntryNorm->>NumNorm: normalize_number(value)
        activate NumNorm
        NumNorm-->>EntryNorm: нормализованное значение
        deactivate NumNorm
        EntryNorm-->>CalcApp: нормализованное значение
        deactivate EntryNorm
        
        CalcApp->>NumValid: is_number(normalized_value)
        activate NumValid
        
        alt значение не является числом
            NumValid-->>CalcApp: False
            deactivate NumValid
            CalcApp-->>User: Сообщение об ошибке
            CalcApp-->>User: Прерывание операции
        else значение является числом
            NumValid-->>CalcApp: True
            deactivate NumValid
            CalcApp->>CalcApp: Добавление значения в список
        end
    end
    
    alt все значения корректны
        CalcApp->>CalcApp: Вычисление суммы значений
        CalcApp->>CalcApp: Форматирование результата
        CalcApp-->>User: Отображение результата
    end
    
    deactivate CalcApp
```