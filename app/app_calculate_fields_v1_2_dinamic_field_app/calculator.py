# import tkinter as tk
# # from tkinter import messagebox
# #
# # class NumberValidator:
# #     """Статический класс для проверки корректности числовых значений"""
# #
# #     @staticmethod
# #     def is_int_positive(value: str) -> bool:
# #         """Проверяет, является ли строка положительным целым числом"""
# #         try:
# #             num = int(value)
# #             return num > 0
# #         except ValueError:
# #             return False
# #
# #     @staticmethod
# #     def is_int_negative(value: str) -> bool:
# #         """Проверяет, является ли строка отрицательным целым числом"""
# #         try:
# #             num = int(value)
# #             return num < 0
# #         except ValueError:
# #             return False
# #
# #     @staticmethod
# #     def is_int(value: str) -> bool:
# #         """Проверяет, является ли строка целым числом"""
# #         try:
# #             int(value)
# #             return True
# #         except ValueError:
# #             return False
# #
# #     @staticmethod
# #     def is_float_positive(value: str) -> bool:
# #         """Проверяет, является ли строка положительным дробным числом"""
# #         try:
# #             num = float(value)
# #             return num > 0 and num != int(num)
# #         except ValueError:
# #             return False
# #
# #     @staticmethod
# #     def is_float_negative(value: str) -> bool:
# #         """Проверяет, является ли строка отрицательным дробным числом"""
# #         try:
# #             num = float(value)
# #             return num < 0 and num != int(num)
# #         except ValueError:
# #             return False
# #
# #     @staticmethod
# #     def is_float(value: str) -> bool:
# #         """Проверяет, является ли строка дробным числом"""
# #         try:
# #             num = float(value)
# #             return num != int(num)
# #         except ValueError:
# #             return False
# #
# #     @staticmethod
# #     def is_number(value: str) -> bool:
# #         """Проверяет, является ли строка числом (целым или дробным)"""
# #         try:
# #             float(value)
# #             return True
# #         except ValueError:
# #             return False
# #
# #
# # class NumberNormalizer:
# #     """Статический класс для нормализации строкового представления чисел"""
# #
# #     @staticmethod
# #     def normalize_number(value: str) -> str:
# #         """Нормализует строковое представление числа (удаляет пробелы, заменяет запятые на точки)"""
# #         if not value:
# #             return "0"
# #
# #         # Удаляем пробелы и заменяем запятые на точки
# #         value_clear = value.strip().replace(',', '.')
# #
# #         # Если строка пустая после очистки, возвращаем "0"
# #         if not value_clear:
# #             return "0"
# #
# #         return value_clear
# #
# #
# # class EntryNormalizer:
# #     """Статический класс для нормализации значений из полей ввода"""
# #
# #     @staticmethod
# #     def normalize_entries(entry: tk.Entry) -> str:
# #         """Нормализует значение из поля ввода"""
# #         value = entry.get()
# #         return NumberNormalizer.normalize_number(value)
# #
# #
# # class CalculatorApp:
# #     """Основной класс приложения калькулятора"""
# #
# #     def __init__(self, master, ammount: int = 2):
# #         """Инициализация приложения"""
# #         self.master = master
# #         self.ammount = ammount  # Сохраняем количество полей
# #
# #         master.title("Калькулятор")
# #         # Адаптируем размер окна в зависимости от количества полей
# #         window_width = 100 + (ammount * 50)
# #         # master.geometry(f"{window_width}x150")
# #         master.resizable(False, False)
# #
# #         # Создаем список для хранения полей ввода
# #         self.entry_fields = []
# #
# #         # Создаем поля ввода и метки между ними
# #         for i in range(ammount):
# #             # Создаем поле ввода
# #             entry = tk.Entry(master, width=10)
# #             entry.grid(row=0, column=i*2, padx=5, pady=20)
# #             self.entry_fields.append(entry)
# #
# #             # Добавляем метку "+" между полями (кроме последнего)
# #             if i < ammount - 1:
# #                 plus_label = tk.Label(master, text="+")
# #                 plus_label.grid(row=0, column=i*2+1, padx=5, pady=20)
# #
# #         # Метка "="
# #         equals_label = tk.Label(master, text="=")
# #         equals_label.grid(row=0, column=ammount*2-1, padx=5, pady=20)
# #
# #         # Поле результата
# #         self.result_plus = tk.Entry(master, width=10, state="readonly")
# #         self.result_plus.grid(row=0, column=ammount*2, padx=5, pady=20)
# #
# #         # Кнопка вычисления
# #         calculate_button = tk.Button(master, text="Вычислить", command=self.calculate_plus)
# #         calculate_button.grid(row=1, column=0, columnspan=ammount*2+1, pady=10)
# #
# #     def calculate_plus(self):
# #         """Метод для выполнения операции сложения"""
# #         values = []
# #
# #         # Нормализация и проверка всех введенных значений
# #         for i, entry in enumerate(self.entry_fields):
# #             normalized_value = EntryNormalizer.normalize_entries(entry)
# #
# #             # Проверка корректности введенного значения
# #             if not NumberValidator.is_number(normalized_value):
# #                 messagebox.showerror("Ошибка", f"Значение #{i+1} не является числом")
# #                 return
# #
# #             values.append(float(normalized_value))
# #
# #         # Вычисление результата (сумма всех значений)
# #         result = sum(values)
# #
# #         # Если результат - целое число, преобразуем его в int для отображения без десятичной части
# #         if result == int(result):
# #             result = int(result)
# #
# #         # Вывод результата
# #         self.result_plus.config(state="normal")
# #         self.result_plus.delete(0, tk.END)
# #         self.result_plus.insert(0, str(result))
# #         self.result_plus.config(state="readonly")
# #
# #
# # if __name__ == "__main__":
# #     # Создание главного окна приложения
# #     root = tk.Tk()
# #     app = CalculatorApp(root, ammount=10)
# #     root.mainloop()

# import tkinter as tk
# from tkinter import messagebox
#
#
# class NumberValidator:
#     """Проверка корректности числовых значений"""
#
#     @staticmethod
#     def is_int_positive(value: str) -> bool:
#         try:
#             return int(value) > 0
#         except ValueError:
#             return False
#
#     @staticmethod
#     def is_int_negative(value: str) -> bool:
#         try:
#             return int(value) < 0
#         except ValueError:
#             return False
#
#     @staticmethod
#     def is_int(value: str) -> bool:
#         try:
#             int(value)
#             return True
#         except ValueError:
#             return False
#
#     @staticmethod
#     def is_float_positive(value: str) -> bool:
#         try:
#             return float(value) > 0
#         except ValueError:
#             return False
#
#     @staticmethod
#     def is_float_negative(value: str) -> bool:
#         try:
#             return float(value) < 0
#         except ValueError:
#             return False
#
#     @staticmethod
#     def is_float(value: str) -> bool:
#         try:
#             float(value)
#             return True
#         except ValueError:
#             return False
#
#     @staticmethod
#     def is_number(value: str) -> bool:
#         """Проверка, можно ли преобразовать значение в число (int или float)"""
#         try:
#             float(value)
#             return True
#         except ValueError:
#             return False
#
#
# class NumberNormalizer:
#     """Нормализатор числовых строк"""
#
#     @staticmethod
#     def normalize_number(value: str) -> str:
#         if not value:
#             return "0"
#         value_clear = value.strip().replace(",", ".").replace(" ", "")
#         if value_clear == "":
#             return "0"
#         return value_clear
#
#
# class EntryNormalizer:
#     """Нормализатор содержимого поля ввода"""
#
#     @staticmethod
#     def normalize_entries(entry: tk.Entry) -> str:
#         value = entry.get()
#         return NumberNormalizer.normalize_number(value)
#
#
# class CalculatorApp:
#     """Главный класс калькулятора"""
#
#     def __init__(self, master, ammount: int = 10):
#         self.master = master
#         self.ammount = ammount
#         self.entry_fields = []
#
#         master.title("Калькулятор")
#         master.resizable(False, False)
#
#         # Создание полей ввода
#         for i in range(ammount):
#             entry = tk.Entry(master, width=10)
#             entry.grid(row=0, column=i * 2, padx=2, pady=5)
#             self.entry_fields.append(entry)
#
#             if i < ammount - 1:
#                 label = tk.Label(master, text="+")
#                 label.grid(row=0, column=i * 2 + 1)
#
#         # Кнопка вычисления
#         btn_calc = tk.Button(master, text="=", command=self.calculate_plus)
#         btn_calc.grid(row=0, column=ammount * 2, padx=5)
#
#         # Поле результата
#         self.result_plus = tk.Entry(master, width=10, state="readonly")
#         self.result_plus.grid(row=0, column=ammount * 2 + 1, padx=5)
#
#         # Метка для вывода ошибок
#         self.label_error = tk.Label(master, text="", fg="red")
#         self.label_error.grid(row=1, column=0, columnspan=ammount * 2 + 2)
#
#     def calculate_plus(self):
#         """Обработчик вычисления суммы"""
#         self.label_error.config(text="")  # очистка ошибок
#         values = []
#
#         for i, entry in enumerate(self.entry_fields):
#             normalized = EntryNormalizer.normalize_entries(entry)
#             if not NumberValidator.is_number(normalized):
#                 error_text = f"Значение #{i+1} не является числом: {entry.get()!r}"
#                 self.label_error.config(text=error_text)
#                 messagebox.showerror("Ошибка ввода", error_text)
#                 return
#             values.append(float(normalized))
#
#         result = sum(values)
#
#         # если результат целый (30.0 → 30)
#         if result.is_integer():
#             result = int(result)
#
#         # обновление поля результата
#         self.result_plus.config(state="normal")
#         self.result_plus.delete(0, tk.END)
#         self.result_plus.insert(0, str(result))
#         self.result_plus.config(state="readonly")
#
#
# # Точка входа
# if __name__ == "__main__":
#     root = tk.Tk()
#     app = CalculatorApp(root, ammount=10)
#     root.mainloop()


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

        # 🟢 Изменено: всегда показываем с плавающей точкой (например, "20.0")
        result_str = f"{result:.10g}"  # ограничим до 10 значимых цифр

        # обновление поля результата
        self.result_plus.config(state="normal")
        self.result_plus.delete(0, tk.END)
        self.result_plus.insert(0, result_str)
        self.result_plus.config(state="readonly")


# Точка входа
if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root, ammount=10)
    app1 = CalculatorApp(root, ammount=7)
    root.mainloop()
