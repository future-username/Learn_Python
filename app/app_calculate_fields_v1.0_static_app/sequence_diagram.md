# Диаграмма последовательности для калькулятора

```mermaid
sequenceDiagram
    actor User
    participant Main
    participant Root
    participant App
    participant Entry
    participant Button
    participant EntryNormalizer
    participant NumberNormalizer
    participant NumberValidator
    participant Result
    participant MessageBox

    User->>Main: Запуск приложения
    Main->>Root: Создание Tk()
    Main->>App: CalculatorApp(root, ammount=10)
    
    activate App
    App->>App: self.master = master
    App->>App: self.ammount = 10
    App->>Root: title("Калькулятор")
    App->>Root: resizable(False, False)
    App->>App: self.entry_fields = []
    
    loop i = 0 to 9
        App->>Entry: Создание Entry(width=10)
        App->>Entry: grid(row=0, column=i*2)
        App->>App: entry_fields.append(entry)
        
        alt i < 9
            App->>Root: Создание Label("+")
        end
    end
    
    App->>Root: Создание Label("=")
    App->>Result: Создание Entry(readonly)
    App->>Button: Создание Button("Вычислить")
    deactivate App
    
    Main->>Root: mainloop()
    
    User->>Entry: Ввод чисел
    User->>Button: Нажатие кнопки
    Button->>App: calculate_plus()
    
    activate App
    App->>App: values = []
    
    loop Для каждого entry
        App->>EntryNormalizer: normalize_entries(entry)
        activate EntryNormalizer
        EntryNormalizer->>Entry: get()
        Entry-->>EntryNormalizer: Возврат строки
        EntryNormalizer->>NumberNormalizer: normalize_number(value)
        
        activate NumberNormalizer
        alt value пустая
            NumberNormalizer-->>EntryNormalizer: "0"
        else
            NumberNormalizer->>NumberNormalizer: strip()
            NumberNormalizer->>NumberNormalizer: replace(',', '.')
            alt result пустой
                NumberNormalizer-->>EntryNormalizer: "0"
            else
                NumberNormalizer-->>EntryNormalizer: normalized value
            end
        end
        deactivate NumberNormalizer
        
        EntryNormalizer-->>App: normalized value
        deactivate EntryNormalizer
        
        App->>NumberValidator: is_number(normalized_value)
        activate NumberValidator
        
        alt Успешная конвертация
            NumberValidator->>NumberValidator: float(value)
            NumberValidator-->>App: True
            deactivate NumberValidator
            App->>App: values.append(float(value))

        else ValueError
            NumberValidator-->>App: False
            App->>MessageBox: showerror()
            MessageBox-->>User: Окно ошибки
            App->>App: return
        end
    end
    
    App->>App: result = sum(values)
    
    alt result == int(result)
        App->>App: result = int(result)
    end
    
    App->>Result: config(state="normal")
    App->>Result: delete(0, END)
    App->>Result: insert(0, str(result))
    App->>Result: config(state="readonly")
    
    deactivate App
    Result-->>User: Отображение результата
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