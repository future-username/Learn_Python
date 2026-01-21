# import tkinter as tk
# from tkinter import messagebox
#
#
# class NumberValidator:
#     """Класс для валидации чисел"""
#
#     @staticmethod
#     def is_int_positive(value: str) -> bool:
#         """Проверка на положительное целое число"""
#         try:
#             num = int(value)
#             return num > 0
#         except ValueError:
#             return False
#
#     @staticmethod
#     def is_int_negative(value: str) -> bool:
#         """Проверка на отрицательное целое число"""
#         try:
#             num = int(value)
#             return num < 0
#         except ValueError:
#             return False
#
#     @staticmethod
#     def is_int(value: str) -> bool:
#         """Проверка на целое число"""
#         try:
#             int(value)
#             return True
#         except ValueError:
#             return False
#
#     @staticmethod
#     def is_float_positive(value: str) -> bool:
#         """Проверка на положительное дробное число"""
#         try:
#             num = float(value)
#             return num > 0
#         except ValueError:
#             return False
#
#     @staticmethod
#     def is_float_negative(value: str) -> bool:
#         """Проверка на отрицательное дробное число"""
#         try:
#             num = float(value)
#             return num < 0
#         except ValueError:
#             return False
#
#     @staticmethod
#     def is_float(value: str) -> bool:
#         """Проверка на дробное число"""
#         try:
#             float(value)
#             return True
#         except ValueError:
#             return False
#
#     @staticmethod
#     def is_number(value: str) -> bool:
#         """Проверка на любое число (целое или дробное)"""
#         return NumberValidator.is_float(value)
#
#
# class NumberNormalizer:
#     """Класс для нормализации чисел"""
#
#     @staticmethod
#     def normalize_number(value: str) -> str:
#         """Нормализация строки с числом (удаление пробелов и лишних символов)"""
#         # Удаляем пробелы
#         value_clear = value.strip()
#         # Заменяем запятую на точку для дробных чисел
#         value_clear = value_clear.replace(',', '.')
#         return value_clear
#
#
# class EntryNormalizer:
#     """Класс для нормализации значений из Entry"""
#
#     @staticmethod
#     def normalize_entries(entry: tk.Entry) -> str:
#         """Получение и нормализация значения из поля Entry"""
#         value = entry.get()
#         return NumberNormalizer.normalize_number(value)
#
#
# class CalculatorApp:
#     """Главный класс приложения калькулятора"""
#
#     def __init__(self, master, ammount: int = 2):
#         """
#         Инициализация приложения
#
#         Args:
#             master: родительское окно
#             ammount: количество полей для ввода (по умолчанию 2)
#         """
#         self.master = master
#         self.ammount = ammount
#         self.entry_fields = []
#
#         # Настройка главного окна
#         self.master.title("Калькулятор")
#         # self.master.geometry("400x300")
#         self.master.resizable(False, False)
#
#         # Создание UI
#         self._create_ui()
#
#     def _create_ui(self):
#         """Создание пользовательского интерфейса"""
#         # Заголовок
#         title_label = tk.Label(
#             self.master,
#             text="Калькулятор сложения",
#             font=("Arial", 16, "bold")
#         )
#         title_label.pack(pady=20)
#
#         # Фрейм для полей ввода
#         input_frame = tk.Frame(self.master)
#         input_frame.pack(pady=10)
#
#         # Создание полей ввода
#         for i in range(self.ammount):
#             label = tk.Label(
#                 input_frame,
#                 text=f"Число {i + 1}:",
#                 font=("Arial", 12)
#             )
#             label.grid(row=i, column=0, padx=10, pady=5, sticky="e")
#
#             entry = tk.Entry(
#                 input_frame,
#                 font=("Arial", 12),
#                 width=20
#             )
#             entry.grid(row=i, column=1, padx=10, pady=5)
#             self.entry_fields.append(entry)
#
#         # Кнопка вычисления
#         calc_button = tk.Button(
#             self.master,
#             text="=",
#             font=("Arial", 14, "bold"),
#             width=10,
#             command=self.calculate_plus,
#             bg="#4CAF50",
#             fg="white"
#         )
#         calc_button.pack(pady=15)
#
#         # Поле результата
#         result_frame = tk.Frame(self.master)
#         result_frame.pack(pady=10)
#
#         result_label = tk.Label(
#             result_frame,
#             text="Результат:",
#             font=("Arial", 12, "bold")
#         )
#         result_label.grid(row=0, column=0, padx=10, pady=5, sticky="e")
#
#         self.result_plus = tk.Entry(
#             result_frame,
#             font=("Arial", 12),
#             width=20,
#             state="readonly",
#             readonlybackground="white"
#         )
#         self.result_plus.grid(row=0, column=1, padx=10, pady=5)
#
#     def calculate_plus(self):
#         """Вычисление суммы введенных чисел"""
#         try:
#             numbers = []
#
#             # Нормализация и валидация всех полей
#             for i, entry in enumerate(self.entry_fields):
#                 normalized = EntryNormalizer.normalize_entries(entry)
#
#                 # Проверка на пустое значение
#                 if not normalized:
#                     messagebox.showerror(
#                         "Ошибка",
#                         f"Поле {i + 1} пустое. Введите число."
#                     )
#                     return
#
#                 # Валидация числа
#                 if not NumberValidator.is_number(normalized):
#                     messagebox.showerror(
#                         "Ошибка",
#                         f"Поле {i + 1} содержит некорректное значение: '{normalized}'\n"
#                         "Введите корректное число."
#                     )
#                     return
#
#                 numbers.append(float(normalized))
#
#             # Вычисление суммы
#             result = sum(numbers)
#
#             # Вывод результата
#             self.result_plus.config(state="normal")
#             self.result_plus.delete(0, tk.END)
#
#             # Форматирование результата (целое или дробное)
#             if result == int(result):
#                 self.result_plus.insert(0, str(int(result)))
#             else:
#                 self.result_plus.insert(0, f"{result:.6g}")
#
#             self.result_plus.config(state="readonly")
#
#         except Exception as e:
#             messagebox.showerror(
#                 "Ошибка",
#                 f"Произошла ошибка при вычислении: {str(e)}"
#             )
#
#
# def main():
#     """Точка входа в приложение"""
#     root = tk.Tk()
#     app = CalculatorApp(root, ammount=4)
#     root.mainloop()
#
#
# if __name__ == "__main__":
#     main()


# import tkinter as tk
# from tkinter import messagebox
#
#
# class NumberValidator:
#     """Статический класс для валидации чисел"""
#
#     @staticmethod
#     def is_int_positive(value: str) -> bool:
#         """Проверяет, является ли значение положительным целым числом"""
#         try:
#             num = int(value)
#             return num > 0
#         except ValueError:
#             return False
#
#     @staticmethod
#     def is_int_negative(value: str) -> bool:
#         """Проверяет, является ли значение отрицательным целым числом"""
#         try:
#             num = int(value)
#             return num < 0
#         except ValueError:
#             return False
#
#     @staticmethod
#     def is_int(value: str) -> bool:
#         """Проверяет, является ли значение целым числом"""
#         try:
#             int(value)
#             return True
#         except ValueError:
#             return False
#
#     @staticmethod
#     def is_float_positive(value: str) -> bool:
#         """Проверяет, является ли значение положительным дробным числом"""
#         try:
#             num = float(value)
#             return num > 0
#         except ValueError:
#             return False
#
#     @staticmethod
#     def is_float_negative(value: str) -> bool:
#         """Проверяет, является ли значение отрицательным дробным числом"""
#         try:
#             num = float(value)
#             return num < 0
#         except ValueError:
#             return False
#
#     @staticmethod
#     def is_float(value: str) -> bool:
#         """Проверяет, является ли значение дробным числом"""
#         try:
#             float(value)
#             return True
#         except ValueError:
#             return False
#
#     @staticmethod
#     def is_number(value: str) -> bool:
#         """Проверяет, является ли значение числом (целым или дробным)"""
#         try:
#             float(value)
#             return True
#         except ValueError:
#             return False
#
#
# class NumberNormalizer:
#     """Статический класс для нормализации чисел"""
#
#     @staticmethod
#     def normalize_number(value: str) -> str:
#         """
#         Нормализует строковое представление числа:
#         - Удаляет пробелы
#         - Заменяет запятую на точку
#         - Возвращает "0" для пустых значений
#         """
#         if not value:
#             return "0"
#
#         value_clear = value.strip()
#         value_clear = value_clear.replace(',', '.')
#
#         if not value_clear:
#             return "0"
#
#         return value_clear
#
#
# class EntryNormalizer:
#     """Статический класс для нормализации полей ввода"""
#
#     @staticmethod
#     def normalize_entries(entry: tk.Entry) -> str:
#         """
#         Получает значение из поля ввода и нормализует его
#         """
#         value = entry.get()
#         return NumberNormalizer.normalize_number(value)
#
#
# class CalculatorApp:
#     """Класс приложения калькулятора"""
#
#     def __init__(self, master, ammount: int = 10):
#         """
#         Инициализация калькулятора
#
#         Args:
#             master: родительское окно
#             ammount: количество полей для ввода
#         """
#         self.master = master
#         self.ammount = ammount
#         self.entry_fields = []
#
#         # Настройка окна
#         self.master.title("Калькулятор")
#         self.master.resizable(False, False)
#
#         # Создание полей ввода и меток "+"
#         for i in range(self.ammount):
#             entry = tk.Entry(master, width=10)
#             entry.grid(row=0, column=i * 2, padx=5, pady=20)
#             self.entry_fields.append(entry)
#
#             # Добавляем метку "+" между полями (кроме последнего)
#             if i < self.ammount - 1:
#                 plus_label = tk.Label(master, text="+")
#                 plus_label.grid(row=0, column=i * 2 + 1, padx=5, pady=20)
#
#         # Метка "="
#         equals_label = tk.Label(master, text="=")
#         equals_label.grid(row=0, column=self.ammount * 2, padx=5, pady=20)
#
#         # Поле результата (только для чтения)
#         self.result_plus = tk.Entry(master, width=15, state="readonly")
#         self.result_plus.grid(row=0, column=self.ammount * 2 + 1, padx=5, pady=20)
#
#         # Кнопка вычисления
#         calculate_button = tk.Button(master, text="Вычислить", command=self.calculate_plus)
#         calculate_button.grid(row=1, column=0, columnspan=self.ammount * 2 + 2, pady=10)
#
#     def calculate_plus(self):
#         """
#         Вычисляет сумму всех введенных значений
#         """
#         values = []
#
#         # Проходим по всем полям ввода
#         for i, entry in enumerate(self.entry_fields, start=1):
#             # Нормализуем значение
#             normalized_value = EntryNormalizer.normalize_entries(entry)
#
#             # Валидируем значение
#             if not NumberValidator.is_number(normalized_value):
#                 messagebox.showerror(
#                     "Ошибка",
#                     f"Значение #{i} не является числом: '{entry.get()}'"
#                 )
#                 return
#
#             # Добавляем в список
#             values.append(float(normalized_value))
#
#         # Вычисляем сумму
#         result = sum(values)
#
#         # Если результат целое число, преобразуем к int
#         if result == int(result):
#             result = int(result)
#
#         # Выводим результат
#         self.result_plus.config(state="normal")
#         self.result_plus.delete(0, tk.END)
#         self.result_plus.insert(0, str(result))
#         self.result_plus.config(state="readonly")
#
#
# def main():
#     """Главная функция запуска приложения"""
#     root = tk.Tk()
#     app = CalculatorApp(root, ammount=10)
#     app23 = CalculatorApp(root, ammount=10)
#     root.mainloop()
#
#
# if __name__ == "__main__":
#     main()


import tkinter as tk
from tkinter import messagebox


class NumberValidator:
    """Проверка корректности числовых значений"""

    @staticmethod
    def is_int_positive(value: str) -> bool:
        try:
            return int(value) > 0
        except ValueError:
            return False

    @staticmethod
    def is_int_negative(value: str) -> bool:
        try:
            return int(value) < 0
        except ValueError:
            return False

    @staticmethod
    def is_int(value: str) -> bool:
        try:
            int(value)
            return True
        except ValueError:
            return False

    @staticmethod
    def is_float_positive(value: str) -> bool:
        try:
            return float(value) > 0
        except ValueError:
            return False

    @staticmethod
    def is_float_negative(value: str) -> bool:
        try:
            return float(value) < 0
        except ValueError:
            return False

    @staticmethod
    def is_float(value: str) -> bool:
        try:
            float(value)
            return True
        except ValueError:
            return False

    @staticmethod
    def is_number(value: str) -> bool:
        """Проверка, можно ли преобразовать значение в число (int или float)"""
        try:
            float(value)
            return True
        except ValueError:
            return False


class NumberNormalizer:
    """Нормализатор числовых строк"""

    @staticmethod
    def normalize_number(value: str) -> str:
        if not value:
            return "0"
        value_clear = value.strip().replace(",", ".").replace(" ", "")
        if value_clear == "":
            return "0"
        return value_clear


class EntryNormalizer:
    """Нормализатор содержимого поля ввода"""

    @staticmethod
    def normalize_entries(entry: tk.Entry) -> str:
        value = entry.get()
        return NumberNormalizer.normalize_number(value)


class CalculatorApp:
    """Главный класс калькулятора"""

    def __init__(self, master, ammount: int = 10):
        self.master = master
        self.ammount = ammount
        self.entry_fields = []

        master.title("Калькулятор")
        master.resizable(False, False)

        # Создание полей ввода
        for i in range(ammount):
            entry = tk.Entry(master, width=10)
            entry.grid(row=0, column=i * 2, padx=2, pady=5)
            self.entry_fields.append(entry)

            if i < ammount - 1:
                label = tk.Label(master, text="+")
                label.grid(row=0, column=i * 2 + 1)

        # Кнопка вычисления
        btn_calc = tk.Button(master, text="=", command=self.calculate_plus)
        btn_calc.grid(row=0, column=ammount * 2, padx=5)

        # Поле результата
        self.result_plus = tk.Entry(master, width=10, state="readonly")
        self.result_plus.grid(row=0, column=ammount * 2 + 1, padx=5)

        # Метка для вывода ошибок
        self.label_error = tk.Label(master, text="", fg="red")
        self.label_error.grid(row=1, column=0, columnspan=ammount * 2 + 2)

    def calculate_plus(self):
        """Обработчик вычисления суммы"""
        self.label_error.config(text="")  # очистка ошибок
        values = []

        for i, entry in enumerate(self.entry_fields):
            normalized = EntryNormalizer.normalize_entries(entry)
            if not NumberValidator.is_number(normalized):
                error_text = f"Значение #{i+1} не является числом: {entry.get()!r}"
                self.label_error.config(text=error_text)
                messagebox.showerror("Ошибка ввода", error_text)
                return
            values.append(float(normalized))

        result = sum(values)

        # если результат целый (30.0 → 30)
        if result.is_integer():
            result = int(result)

        # обновление поля результата
        self.result_plus.config(state="normal")
        self.result_plus.delete(0, tk.END)
        self.result_plus.insert(0, str(result))
        self.result_plus.config(state="readonly")


# Точка входа
if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root, ammount=10)
    root.mainloop()

