```mermaid
classDiagram
    class NumberValidator {
        <<static>>
        +is_int_positive(value: str) bool
        +is_int_negative(value: str) bool
        +is_int(value: str) bool
        +is_float_positive(value: str) bool
        +is_float_negative(value: str) bool
        +is_float(value: str) bool
        +is_number(value: str) bool
    }
    
    class NumberNormalizer {
        <<static>>
        +normalize_number(value: str) str
    }
    
    class EntryNormalizer {
        <<static>>
        +normalize_entries(entry: tk.Entry) str
    }
    
    class CalculatorApp {
        -master
        -amount: int
        +sign: Literal["+", "-"]
        -list_entries: list[Entry]
        -result_plus: tk.Entry
        -list_values: list[str]
        +__init__(master, amount: int, sign: Literal["+", "-"])
        -get_values()  # Method get value from Entry and normalize them and check&show error
        +calculate_plus()
        +calculate_minus()
    }
    
    EntryNormalizer --> NumberNormalizer : использует
    CalculatorApp --> EntryNormalizer : использует
    CalculatorApp --> NumberValidator : использует
```