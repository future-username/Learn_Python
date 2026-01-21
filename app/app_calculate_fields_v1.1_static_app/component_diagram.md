# Диаграмма компонентов для калькулятора

```mermaid
flowchart TB
    subgraph UI["UI Components"]
        FirstEntry["first_plus: Entry"]
        SecondEntry["second_plus: Entry"]
        ResultEntry["result_plus: Entry"]
        CalcButton["Button '='"]
        PlusLabel["Label '+'"]
    end
    
    subgraph Validators["Validation Components"]
        NumValidator["NumberValidator"]
        NumNormalizer["NumberNormalizer"]
        EntryNormalizer["EntryNormalizer"]
    end
    
    subgraph Logic["Application Logic"]
        CalcApp["CalculatorApp"]
        CalcFunc["calculate_plus()"]
    end
    
    CalcApp --> UI
    CalcButton --> CalcFunc
    CalcFunc --> EntryNormalizer
    EntryNormalizer --> NumNormalizer
    CalcFunc --> NumValidator
    FirstEntry --> CalcFunc
    SecondEntry --> CalcFunc
    CalcFunc --> ResultEntry
```

## Описание компонентов

### UI Components
- **first_plus**: Поле ввода для первого операнда
- **second_plus**: Поле ввода для второго операнда
- **result_plus**: Поле вывода результата
- **CalcButton**: Кнопка "=" для выполнения операции
- **PlusLabel**: Метка "+" между полями ввода

### Validation Components
- **NumberValidator**: Компонент для проверки корректности числовых значений
- **NumberNormalizer**: Компонент для нормализации строкового представления чисел
- **EntryNormalizer**: Компонент для нормализации значений из полей ввода

### Application Logic
- **CalculatorApp**: Основной компонент приложения
- **calculate_plus()**: Функция для выполнения операции сложения