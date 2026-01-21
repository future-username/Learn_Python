# Диаграмма классов для калькулятора

```mermaid
classDiagram
    class NumberValidator {
        +is_int_positive(value: str) bool$
        +is_int_negative(value: str) bool$
        +is_int(value: str) bool$
        +is_float_positive(value: str) bool$
        +is_float_negative(value: str) bool$
        +is_float(value: str) bool$
        +is_number(value: str) bool$
    }
    
    class NumberNormalizer {
        +normalize_number(value: str) str$
    }
    
    class EntryNormalizer {
        +normalize_entries(value: Entry) str$
    }
    
    class CalculatorApp {
        -master
        -first_plus: Entry
        -second_plus: Entry
        -result_plus: Entry
        +__init__(master)
        +calculate_plus()
    }
    
    EntryNormalizer ..> NumberNormalizer : использует
    CalculatorApp ..> EntryNormalizer : использует
    CalculatorApp ..> NumberValidator : использует
```

## Описание классов

### NumberValidator
Статический класс для проверки корректности числовых значений. Содержит методы для проверки целых и дробных чисел, положительных и отрицательных значений.

### NumberNormalizer
Статический класс для нормализации строкового представления чисел. Удаляет пробелы и заменяет запятые на точки.

### EntryNormalizer
Статический класс для нормализации значений из полей ввода (Entry). Использует NumberNormalizer для обработки текста.

### CalculatorApp
Основной класс приложения. Создает пользовательский интерфейс и обрабатывает взаимодействие с пользователем.