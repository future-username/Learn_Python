# Калькулятор с графическим интерфейсом на Tkinter

import tkinter as tk
from tkinter import messagebox
import math
from my_module.calculator_core import Calculator
from my_module.calculator_interface import CalculatorProcessor, CalculatorValidator
from my_module.helpers import validate_input, format_output, log_operation


class CalculatorApp:
    """Класс для создания графического интерфейса калькулятора."""
    
    def __init__(self, root):
        """Инициализация графического интерфейса.
        
        Args:
            root: Корневой элемент Tkinter
        """
        self.root = root
        self.root.title("Калькулятор")
        self.root.geometry("300x500")
        self.root.resizable(False, False)
        
        # Инициализация ядра калькулятора
        self.calculator = Calculator()
        self.calculator.initialize()
        
        # Инициализация процессора и валидатора
        self.processor = CalculatorProcessor(self.calculator)
        self.validator = CalculatorValidator()
        
        # Переменная для хранения текущего выражения
        self.current_expression = ""
        
        # Создание элементов интерфейса
        self._create_widgets()
    
    def _create_widgets(self):
        """Создание элементов интерфейса."""
        # Поле для отображения выражения и результата
        self.display = tk.Entry(self.root, font=("Arial", 20), justify="right", bd=5)
        self.display.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")
        
        # Кнопки цифр и операций
        buttons = [
            ('MC', 1, 0), ('MR', 1, 1), ('MS', 1, 2), ('M+', 1, 3),
            ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('/', 2, 3),
            ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('*', 3, 3),
            ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('-', 4, 3),
            ('0', 5, 0), ('.', 5, 1), ('=', 5, 2), ('+', 5, 3),
            ('C', 6, 0), ('CE', 6, 1), ('(', 6, 2), (')', 6, 3),
            ('√', 7, 0), ('^2', 7, 1), ('^', 7, 2), ('%', 7, 3)
        ]
        
        for (text, row, col) in buttons:
            button = tk.Button(self.root, text=text, font=("Arial", 15), 
                             width=4, height=2, command=lambda t=text: self._on_button_click(t))
            button.grid(row=row, column=col, padx=5, pady=5)
        
        # Настройка растяжения строк и столбцов
        for i in range(8):
            self.root.grid_rowconfigure(i, weight=1)
        for i in range(4):
            self.root.grid_columnconfigure(i, weight=1)
    
    def _on_button_click(self, button_text):
        """Обработка нажатия кнопки.
        
        Args:
            button_text: Текст нажатой кнопки
        """
        if button_text == "=":
            self._calculate()
        elif button_text == "C":
            self._clear_all()
        elif button_text == "CE":
            self._clear_entry()
        # Обработка кнопок памяти
        elif button_text == "MC":
            self.calculator.memory_clear()
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, self.current_expression)
        elif button_text == "MR":
            memory_value = self.calculator.memory_recall()
            self.current_expression = str(memory_value)
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, self.current_expression)
        elif button_text == "MS":
            if self.current_expression:
                try:
                    result = self.processor.process(self.current_expression)
                    self.calculator.last_result = result
                    self.calculator.memory_store()
                except Exception as e:
                    messagebox.showerror("Ошибка", str(e))
            else:
                self.calculator.memory_store()
        elif button_text == "M+":
            if self.current_expression:
                try:
                    result = self.processor.process(self.current_expression)
                    self.calculator.memory += result
                    log_operation("добавление в память", True)
                except Exception as e:
                    messagebox.showerror("Ошибка", str(e))
        # Обработка научных операций
        elif button_text == "√":
            if self.current_expression:
                try:
                    result = self.processor.process(self.current_expression)
                    if result < 0:
                        messagebox.showerror("Ошибка", "Невозможно извлечь корень из отрицательного числа")
                    else:
                        import math
                        result = math.sqrt(result)
                        self.current_expression = str(result)
                        self.display.delete(0, tk.END)
                        self.display.insert(tk.END, self.current_expression)
                except Exception as e:
                    messagebox.showerror("Ошибка", str(e))
            else:
                self.current_expression += "math.sqrt("
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, self.current_expression)
        elif button_text == "^2":
            if self.current_expression:
                try:
                    result = self.processor.process(self.current_expression)
                    result = result ** 2
                    self.current_expression = str(result)
                    self.display.delete(0, tk.END)
                    self.display.insert(tk.END, self.current_expression)
                except Exception as e:
                    messagebox.showerror("Ошибка", str(e))
            else:
                messagebox.showerror("Ошибка", "Введите число для возведения в квадрат")
        elif button_text == "^":
            self.current_expression += "**"
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, self.current_expression)
        elif button_text == "%":
            if self.current_expression:
                try:
                    result = self.processor.process(self.current_expression)
                    result = result / 100
                    self.current_expression = str(result)
                    self.display.delete(0, tk.END)
                    self.display.insert(tk.END, self.current_expression)
                except Exception as e:
                    messagebox.showerror("Ошибка", str(e))
            else:
                messagebox.showerror("Ошибка", "Введите число для вычисления процента")
        else:
            self.current_expression += button_text
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, self.current_expression)
    
    def _calculate(self):
        """Вычисление результата выражения."""
        expression = self.current_expression
        
        # Проверка валидности выражения
        if not self.validator.validate(expression):
            messagebox.showerror("Ошибка", "Некорректное выражение")
            return
        
        try:
            # Вычисление результата
            result = self._process_expression(expression)
            
            # Форматирование и отображение результата
            formatted_result = format_output(result)
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, formatted_result)
            
            # Обновление текущего выражения
            self.current_expression = str(formatted_result)
            
            # Логирование операции
            log_operation("вычисление", True)
        except Exception as e:
            messagebox.showerror("Ошибка", str(e))
            log_operation("вычисление", False)
    
    def _process_expression(self, expression):
        """Обработка выражения с использованием Calculator.
        
        Args:
            expression: Строка с математическим выражением
            
        Returns:
            Результат вычисления
        """
        # Используем CalculatorProcessor для обработки данных
        try:
            return self.processor.process(expression)
        except Exception as e:
            raise ValueError(f"Ошибка при вычислении выражения: {str(e)}")
    
    def _clear_all(self):
        """Очистка всего выражения."""
        self.current_expression = ""
        self.display.delete(0, tk.END)
    
    def _clear_entry(self):
        """Удаление последнего символа."""
        self.current_expression = self.current_expression[:-1]
        self.display.delete(0, tk.END)
        self.display.insert(tk.END, self.current_expression)


def main():
    """Основная функция для запуска приложения."""
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()