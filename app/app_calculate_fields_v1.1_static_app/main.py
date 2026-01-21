import tkinter as tk
from tkinter import messagebox

class NumberValidator:
    """Статический класс для проверки корректности числовых значений"""
    
    @staticmethod
    def is_int_positive(value: str) -> bool:
        """Проверяет, является ли строка положительным целым числом"""
        try:
            num = int(value)
            return num > 0
        except ValueError:
            return False
    
    @staticmethod
    def is_int_negative(value: str) -> bool:
        """Проверяет, является ли строка отрицательным целым числом"""
        try:
            num = int(value)
            return num < 0
        except ValueError:
            return False
    
    @staticmethod
    def is_int(value: str) -> bool:
        """Проверяет, является ли строка целым числом"""
        try:
            int(value)
            return True
        except ValueError:
            return False
    
    @staticmethod
    def is_float_positive(value: str) -> bool:
        """Проверяет, является ли строка положительным дробным числом"""
        try:
            num = float(value)
            return num > 0 and num != int(num)
        except ValueError:
            return False
    
    @staticmethod
    def is_float_negative(value: str) -> bool:
        """Проверяет, является ли строка отрицательным дробным числом"""
        try:
            num = float(value)
            return num < 0 and num != int(num)
        except ValueError:
            return False
    
    @staticmethod
    def is_float(value: str) -> bool:
        """Проверяет, является ли строка дробным числом"""
        try:
            num = float(value)
            return num != int(num)
        except ValueError:
            return False
    
    @staticmethod
    def is_number(value: str) -> bool:
        """Проверяет, является ли строка числом (целым или дробным)"""
        try:
            float(value)
            return True
        except ValueError:
            return False


class NumberNormalizer:
    """Статический класс для нормализации строкового представления чисел"""
    
    @staticmethod
    def normalize_number(value: str) -> str:
        """Нормализует строковое представление числа (удаляет пробелы, заменяет запятые на точки)"""
        if not value:
            return "0"
        
        # Удаляем пробелы и заменяем запятые на точки
        value_clear = value.strip().replace(',', '.')
        
        # Если строка пустая после очистки, возвращаем "0"
        if not value_clear:
            return "0"
        
        return value_clear


class EntryNormalizer:
    """Статический класс для нормализации значений из полей ввода"""
    
    @staticmethod
    def normalize_entries(entry: tk.Entry) -> str:
        """Нормализует значение из поля ввода"""
        value = entry.get()
        return NumberNormalizer.normalize_number(value)


class CalculatorApp:
    """Основной класс приложения калькулятора"""
    
    def __init__(self, master):
        """Инициализация приложения"""
        self.master = master
        master.title("Калькулятор")
        master.geometry("300x150")
        master.resizable(False, False)
        
        # Создание UI элементов
        # Первое поле ввода
        self.first_plus = tk.Entry(master, width=10)
        self.first_plus.grid(row=0, column=0, padx=5, pady=20)
        
        # Метка "+"
        plus_label = tk.Label(master, text="+")
        plus_label.grid(row=0, column=1, padx=5, pady=20)
        
        # Второе поле ввода
        self.second_plus = tk.Entry(master, width=10)
        self.second_plus.grid(row=0, column=2, padx=5, pady=20)
        
        # Метка "="
        equals_label = tk.Label(master, text="=")
        equals_label.grid(row=0, column=3, padx=5, pady=20)
        
        # Поле результата
        self.result_plus = tk.Entry(master, width=10, state="readonly")
        self.result_plus.grid(row=0, column=4, padx=5, pady=20)
        
        # Кнопка вычисления
        calculate_button = tk.Button(master, text="Вычислить", command=self.calculate_plus)
        calculate_button.grid(row=1, column=0, columnspan=5, pady=10)
    
    def calculate_plus(self):
        """Метод для выполнения операции сложения"""
        # Нормализация введенных значений
        first_normalize = EntryNormalizer.normalize_entries(self.first_plus)
        second_normalize = EntryNormalizer.normalize_entries(self.second_plus)
        
        # Проверка корректности введенных значений
        if not NumberValidator.is_number(first_normalize):
            messagebox.showerror("Ошибка", "Первое значение не является числом")
            return
        
        if not NumberValidator.is_number(second_normalize):
            messagebox.showerror("Ошибка", "Второе значение не является числом")
            return
        
        # Вычисление результата
        result = float(first_normalize) + float(second_normalize)
        
        # Если результат - целое число, преобразуем его в int для отображения без десятичной части
        if result == int(result):
            result = int(result)
        
        # Вывод результата
        self.result_plus.config(state="normal")
        self.result_plus.delete(0, tk.END)
        self.result_plus.insert(0, str(result))
        self.result_plus.config(state="readonly")


if __name__ == "__main__":
    # Создание главного окна приложения
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()