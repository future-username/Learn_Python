# Диаграмма последовательности для калькулятора

```mermaid
sequenceDiagram
    participant User
    participant App as CalculatorApp
    participant EntryNorm as EntryNormalizer
    participant NumNorm as NumberNormalizer
    participant NumVal as NumberValidator
    
    User->>App: Запуск приложения
    App->>App: __init__(master)
    App->>App: Создание UI элементов
    User->>App: Ввод значений в поля
    User->>App: Нажатие кнопки "="
    App->>App: calculate_plus()
    App->>EntryNorm: normalize_entries(first_plus)
    EntryNorm->>NumNorm: normalize_number(value)
    NumNorm-->>EntryNorm: value_clear
    EntryNorm-->>App: first_normalize
    App->>EntryNorm: normalize_entries(second_plus)
    EntryNorm->>NumNorm: normalize_number(value)
    NumNorm-->>EntryNorm: value_clear
    EntryNorm-->>App: second_normalize
    App->>NumVal: is_number(first_normalize)
    NumVal-->>App: результат проверки
    App->>NumVal: is_number(second_normalize)
    NumVal-->>App: результат проверки
    App->>App: Вычисление и вывод результата
```

## Описание последовательности действий

1. Пользователь запускает приложение
2. Создается экземпляр CalculatorApp, который инициализирует интерфейс
3. Пользователь вводит значения в поля ввода
4. Пользователь нажимает кнопку "="
5. Вызывается метод calculate_plus()
6. Происходит нормализация введенных значений через EntryNormalizer
7. EntryNormalizer использует NumberNormalizer для очистки строк
8. Проверяется корректность значений через NumberValidator
9. Если значения корректны, выполняется сложение и результат выводится в поле результата
10. Если значения некорректны, выводится сообщение об ошибке