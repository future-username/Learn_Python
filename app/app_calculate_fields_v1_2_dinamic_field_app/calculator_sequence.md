sequenceDiagram
    actor User as Пользователь
    participant Main as main
    participant Root as Tk (root)
    participant App as CalculatorApp
    participant Entry as Entry Fields
    participant Button as Calculate Button
    participant Normalizer as EntryNormalizer
    participant NumNorm as NumberNormalizer
    participant Validator as NumberValidator
    participant Result as Result Field
    participant MsgBox as MessageBox

    User->>Main: Запуск приложения
    Main->>Root: Создание Tk()
    Main->>App: CalculatorApp(root, ammount=10)
    
    App->>Root: Установка title("Калькулятор")
    App->>Root: Установка resizable(False, False)
    
    loop Для каждого поля (i = 0 до ammount)
        App->>Entry: Создание Entry(width=10)
        App->>Entry: grid(row=0, column=i*2)
        App->>App: Добавление в entry_fields[]
        
        alt i < ammount - 1
            App->>Root: Создание Label("+")
            App->>Root: grid(row=0, column=i*2+1)
        end
    end
    
    App->>Root: Создание Label("=")
    App->>Result: Создание Entry(state="readonly")
    App->>Button: Создание Button("Вычислить", command=calculate_plus)
    
    Main->>Root: mainloop()
    
    Note over User,Root: Приложение ожидает действий пользователя
    
    User->>Entry: Ввод чисел в поля
    User->>Button: Нажатие кнопки "Вычислить"
    Button->>App: calculate_plus()
    
    App->>App: Создание списка values[]
    
    loop Для каждого entry в entry_fields
        App->>Normalizer: normalize_entries(entry)
        Normalizer->>Entry: get()
        Entry-->>Normalizer: Возврат строки
        Normalizer->>NumNorm: normalize_number(value)
        NumNorm->>NumNorm: strip(), replace(',', '.')
        NumNorm-->>Normalizer: Нормализованная строка
        Normalizer-->>App: Нормализованное значение
        
        App->>Validator: is_number(normalized_value)
        Validator->>Validator: float(value)
        
        alt Значение не является числом
            Validator-->>App: False
            App->>MsgBox: showerror("Ошибка", "Значение #i не является числом")
            MsgBox-->>User: Показать ошибку
            App->>App: return (выход из метода)
        else Значение корректно
            Validator-->>App: True
            App->>App: Добавить float(value) в values[]
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
    
    Result-->>User: Отображение результата