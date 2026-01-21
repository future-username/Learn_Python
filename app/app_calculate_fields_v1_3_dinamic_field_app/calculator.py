# import tkinter as tk
# from tkinter import messagebox
# from typing import Literal
#
#
# class NumberValidator:
#     """Валидатор для проверки чисел"""
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
#         """Проверка на число (целое или дробное)"""
#         try:
#             float(value)
#             return True
#         except ValueError:
#             return False
#
#
# class NumberNormalizer:
#     """Нормализатор для преобразования строки в число"""
#
#     @staticmethod
#     def normalize_number(value: str) -> str:
#         """Нормализует строку: удаляет пробелы, заменяет запятую на точку"""
#         if not value:
#             return "0"
#
#         # Удаление всех пробелов
#         value_clear = value.replace(" ", "")
#
#         # Замена запятой на точку
#         value_clear = value_clear.replace(",", ".")
#
#         # Если после очистки строка пустая, возвращаем "0"
#         if not value_clear:
#             return "0"
#
#         return value_clear
#
#
# class EntryNormalizer:
#     """Нормализатор для полей ввода"""
#
#     @staticmethod
#     def normalize_entries(entry: tk.Entry) -> str:
#         """Получает текст из поля ввода и нормализует его"""
#         value = entry.get()
#         return NumberNormalizer.normalize_number(value)
#
#
# class CalculatorApp:
#     """Класс калькулятора с двумя операциями: сложение и вычитание"""
#
#     def __init__(self, master, ammount: int = 10):
#         """Инициализация калькулятора
#
#         Args:
#             master: главное окно приложения
#             ammount: количество полей ввода (по умолчанию 10)
#         """
#         self.master = master
#         self.ammount = ammount
#
#         # Настройка главного окна
#         self.master.title("Калькулятор")
#         self.master.resizable(False, False)
#
#         # Инициализация списков для полей ввода
#         self.entry_fields_plus = []
#         self.entry_fields_minus = []
#
#         # Создание интерфейса для сложения
#         self._create_addition_interface()
#
#         # Создание интерфейса для вычитания
#         self._create_subtraction_interface()
#
#     def _create_addition_interface(self):
#         """Создание интерфейса для операции сложения"""
#         # Рамка для группировки элементов сложения
#         frame_plus = tk.Frame(self.master, pady=10, padx=10)
#         frame_plus.pack()
#
#         # Метка заголовка
#         tk.Label(frame_plus, text="Сложение:", font=("Arial", 12, "bold")).grid(
#             row=0, column=0, columnspan=self.ammount * 2, sticky="w", pady=(0, 5)
#         )
#
#         # Создание полей ввода и меток "+"
#         for i in range(self.ammount):
#             # Поле ввода
#             entry = tk.Entry(frame_plus, width=8)
#             entry.grid(row=1, column=i * 2, padx=2)
#             self.entry_fields_plus.append(entry)
#
#             # Метка "+" между полями (кроме последнего)
#             if i < self.ammount - 1:
#                 label = tk.Label(frame_plus, text="+", font=("Arial", 12))
#                 label.grid(row=1, column=i * 2 + 1, padx=2)
#
#         # Кнопка "=" и поле результата
#         btn_equal = tk.Button(frame_plus, text="=", width=3, command=self.calculate_plus)
#         btn_equal.grid(row=1, column=self.ammount * 2, padx=5)
#
#         self.result_plus = tk.Entry(frame_plus, width=12, state="readonly")
#         self.result_plus.grid(row=1, column=self.ammount * 2 + 1, padx=2)
#
#         # Метка для ошибок
#         self.error_label_plus = tk.Label(frame_plus, text="", fg="red", font=("Arial", 9))
#         self.error_label_plus.grid(row=2, column=0, columnspan=self.ammount * 2 + 2, pady=(5, 0))
#
#     def _create_subtraction_interface(self):
#         """Создание интерфейса для операции вычитания"""
#         # Рамка для группировки элементов вычитания
#         frame_minus = tk.Frame(self.master, pady=10, padx=10)
#         frame_minus.pack()
#
#         # Метка заголовка
#         tk.Label(frame_minus, text="Вычитание:", font=("Arial", 12, "bold")).grid(
#             row=0, column=0, columnspan=self.ammount * 2, sticky="w", pady=(0, 5)
#         )
#
#         # Создание полей ввода и меток "-"
#         for i in range(self.ammount):
#             # Поле ввода
#             entry = tk.Entry(frame_minus, width=8)
#             entry.grid(row=1, column=i * 2, padx=2)
#             self.entry_fields_minus.append(entry)
#
#             # Метка "-" между полями (кроме последнего)
#             if i < self.ammount - 1:
#                 label = tk.Label(frame_minus, text="-", font=("Arial", 12))
#                 label.grid(row=1, column=i * 2 + 1, padx=2)
#
#         # Кнопка "=" и поле результата
#         btn_equal = tk.Button(frame_minus, text="=", width=3, command=self.calculate_minus)
#         btn_equal.grid(row=1, column=self.ammount * 2, padx=5)
#
#         self.result_minus = tk.Entry(frame_minus, width=12, state="readonly")
#         self.result_minus.grid(row=1, column=self.ammount * 2 + 1, padx=2)
#
#         # Метка для ошибок
#         self.error_label_minus = tk.Label(frame_minus, text="", fg="red", font=("Arial", 9))
#         self.error_label_minus.grid(row=2, column=0, columnspan=self.ammount * 2 + 2, pady=(5, 0))
#
#     def calculate_plus(self):
#         """Вычисление суммы всех введенных значений"""
#         self.error_label_plus.config(text="")
#         values = []
#
#         # Обработка каждого поля ввода
#         for i, entry in enumerate(self.entry_fields_plus):
#             # Нормализация значения
#             normalized_value = EntryNormalizer.normalize_entries(entry)
#
#             # Валидация
#             if not NumberValidator.is_number(normalized_value):
#                 error_msg = f"Значение #{i + 1} не является числом"
#                 self.error_label_plus.config(text=error_msg)
#                 messagebox.showerror("Ошибка", error_msg)
#                 return
#
#             # Добавление числа в список
#             values.append(float(normalized_value))
#
#         # Вычисление результата
#         result = sum(values)
#
#         # Преобразование в целое, если результат целочисленный
#         if result == int(result):
#             result = int(result)
#
#         # Вывод результата
#         self.result_plus.config(state="normal")
#         self.result_plus.delete(0, tk.END)
#         self.result_plus.insert(0, str(result))
#         self.result_plus.config(state="readonly")
#
#     def calculate_minus(self):
#         """Вычисление разности: первое значение минус сумма остальных"""
#         self.error_label_minus.config(text="")
#         values = []
#
#         # Обработка каждого поля ввода
#         for i, entry in enumerate(self.entry_fields_minus):
#             # Нормализация значения
#             normalized_value = EntryNormalizer.normalize_entries(entry)
#
#             # Валидация
#             if not NumberValidator.is_number(normalized_value):
#                 error_msg = f"Значение #{i + 1} не является числом"
#                 self.error_label_minus.config(text=error_msg)
#                 messagebox.showerror("Ошибка", error_msg)
#                 return
#
#             # Добавление числа в список
#             values.append(float(normalized_value))
#
#         # Вычисление результата: первое значение минус сумма остальных
#         if len(values) > 0:
#             result = values[0] - sum(values[1:])
#         else:
#             result = 0
#
#         # Преобразование в целое, если результат целочисленный
#         if result == int(result):
#             result = int(result)
#
#         # Вывод результата
#         self.result_minus.config(state="normal")
#         self.result_minus.delete(0, tk.END)
#         self.result_minus.insert(0, str(result))
#         self.result_minus.config(state="readonly")
#
#
# def main():
#     """Главная функция запуска приложения"""
#     root = tk.Tk()
#     app = CalculatorApp(root, ammount=10)
#     root.mainloop()
#
#
# if __name__ == "__main__":
#     main()


# import tkinter as tk
# from typing import Literal
#
#
# # --- Вспомогательные классы (из диаграммы классов) ---
#
# class NumberNormalizer:
#     """Нормализатор чисел (удаление пробелов, замена запятых)."""
#
#     @staticmethod
#     def normalize_number(value: str) -> str:
#         # Диаграмма Часть 4/5: Удалить пробелы, заменить ',' на '.'
#         if not value:
#             return "0"
#
#         value_clear = value.replace(" ", "").replace(",", ".")
#
#         if not value_clear:
#             return "0"
#         return value_clear
#
#
# class NumberValidator:
#     """Валидатор чисел (проверка типов)."""
#
#     @staticmethod
#     def is_number(value: str) -> bool:
#         try:
#             float(value)
#             return True
#         except ValueError:
#             return False
#
#     # Дополнительные методы из диаграммы классов (для полноты картины)
#     @staticmethod
#     def is_int(value: str) -> bool:
#         try:
#             int(value)
#             return True
#         except ValueError:
#             return False
#
#     # Остальные методы (is_float, is_int_positive и т.д.) можно реализовать аналогично,
#     # но в основной логике используется is_number.
#
#
# class EntryNormalizer:
#     """Нормализатор для виджетов Entry."""
#
#     @staticmethod
#     def normalize_entries(entry: tk.Entry) -> str:
#         # Получаем текст из поля и отправляем в NumberNormalizer
#         text = entry.get()
#         return NumberNormalizer.normalize_number(text)
#
#
# # --- Основной класс приложения ---
#
# class CalculatorApp:
#     def __init__(self, master, amount: int, sign: Literal["+", "-"]):
#         self.master = master
#         self.amount = amount
#         self.sign = sign
#         self.entry_fields = []
#
#         # Создаем фрейм-контейнер для этой линии калькулятора,
#         # чтобы отделить "+" от "-"
#         self.frame = tk.Frame(master)
#         self.frame.pack(padx=10, pady=10, fill="x")
#
#         # --- Часть 2 и 3: Создание интерфейса ---
#         self._create_widgets()
#
#     def _create_widgets(self):
#         # 1. Цикл создания полей ввода (input fields)
#         for i in range(self.amount):
#             # Создание поля ввода
#             entry = tk.Entry(self.frame, width=5)
#             entry.pack(side=tk.LEFT)
#             self.entry_fields.append(entry)
#
#             # Если не последнее поле, добавляем метку знака (+ или -)
#             if i < self.amount - 1:
#                 lbl = tk.Label(self.frame, text=self.sign)
#                 lbl.pack(side=tk.LEFT, padx=2)
#
#         # 2. Метка "="
#         lbl_eq = tk.Label(self.frame, text="=")
#         lbl_eq.pack(side=tk.LEFT, padx=5)
#
#         # 3. Кнопка вычисления (Button)
#         # Выбираем обработчик в зависимости от знака
#         command = self.calculate_plus if self.sign == "+" else self.calculate_minus
#         self.btn_calc = tk.Button(self.frame, text="Вычислить", command=command)
#         self.btn_calc.pack(side=tk.LEFT, padx=5)
#
#         # 4. Поле результата (ResultField)
#         self.result_field = tk.Entry(self.frame, width=10, state="readonly")
#         self.result_field.pack(side=tk.LEFT, padx=5)
#
#         # 5. Метка ошибки (LabelError) - размещаем под строкой полей
#         # Для этого используем отдельный фрейм или pack в главном окне сразу под фреймом
#         self.label_error = tk.Label(self.master, text="", fg="red")
#         self.label_error.pack(anchor="w", padx=10)
#
#     def calculate_plus(self):
#         """Часть 4: Обработка операции сложения"""
#         values = []
#         self.label_error.config(text="")  # Очистка ошибок
#
#         for i, entry in enumerate(self.entry_fields):
#             # 1. Нормализация
#             normalized_val = EntryNormalizer.normalize_entries(entry)
#
#             # 2. Валидация
#             if NumberValidator.is_number(normalized_val):
#                 values.append(float(normalized_val))
#             else:
#                 # Ошибка
#                 self.label_error.config(text=f"Ошибка: Значение в поле #{i + 1} не является числом")
#                 return
#
#         # 3. Вычисление суммы
#         result = sum(values)
#
#         # 4. Форматирование и вывод
#         self._display_result(result)
#
#     def calculate_minus(self):
#         """Часть 5: Обработка операции вычитания"""
#         values = []
#         self.label_error.config(text="")
#
#         for i, entry in enumerate(self.entry_fields):
#             # 1. Нормализация
#             normalized_val = EntryNormalizer.normalize_entries(entry)
#
#             # 2. Валидация
#             if NumberValidator.is_number(normalized_val):
#                 values.append(float(normalized_val))
#             else:
#                 self.label_error.config(text=f"Ошибка: Значение в поле #{i + 1} не является числом")
#                 return
#
#         if not values:
#             self._display_result(0)
#             return
#
#         # 3. Вычисление: первое - сумма(остальные)
#         # result = values[0] - (values[1] + values[2] + ...)
#         first_val = values[0]
#         rest_sum = sum(values[1:])
#         result = first_val - rest_sum
#
#         # 4. Форматирование и вывод
#         self._display_result(result)
#
#     def _display_result(self, result):
#         """Общий метод вывода результата (целое или дробное)"""
#         # Проверка: Результат целое число? (например 30.0 == 30)
#         if result == int(result):
#             final_str = str(int(result))
#         else:
#             final_str = str(result)
#
#         # Обновление поля (ReadOnly требует смены состояния)
#         self.result_field.config(state="normal")
#         self.result_field.delete(0, tk.END)
#         self.result_field.insert(0, final_str)
#         self.result_field.config(state="readonly")
#
#
# # --- Часть 1: Инициализация приложения (Main) ---
#
# def main():
#     # User -> Main: Запуск приложения
#     root = tk.Tk()
#
#     # Main -> Window: Настройка окна
#     root.title("Калькулятор")
#     root.resizable(False, False)
#
#     # Main -> AppPlus: Создание калькулятора сложения
#     # Создаем метку-заголовок для красоты (опционально, но понятно по контексту)
#     tk.Label(root, text="Сложение (10 полей):", font=("Arial", 10, "bold")).pack(anchor="w", padx=10, pady=(10, 0))
#     app_plus = CalculatorApp(root, amount=10, sign="+")
#
#     # Разделитель
#     tk.Frame(root, height=2, bd=1, relief=tk.SUNKEN).pack(fill="x", padx=5, pady=5)
#
#     # Main -> AppMinus: Создание калькулятора вычитания
#     tk.Label(root, text="Вычитание (10 полей):", font=("Arial", 10, "bold")).pack(anchor="w", padx=10, pady=(5, 0))
#     app_minus = CalculatorApp(root, amount=10, sign="-")
#
#     # Main -> Window: Запуск цикла
#     root.mainloop()
#
#
# if __name__ == "__main__":
#     main()


# import tkinter as tk
# from tkinter import messagebox
# from typing import Literal
#
#
# # ============================================================
# #                NumberValidator
# # ============================================================
# class NumberValidator:
#     @staticmethod
#     def is_int_positive(value: str) -> bool:
#         try:
#             return int(value) >= 0 and "." not in value
#         except:
#             return False
#
#     @staticmethod
#     def is_int_negative(value: str) -> bool:
#         try:
#             return int(value) < 0 and "." not in value
#         except:
#             return False
#
#     @staticmethod
#     def is_int(value: str) -> bool:
#         try:
#             return "." not in value and int(value)
#         except:
#             return False
#
#     @staticmethod
#     def is_float_positive(value: str) -> bool:
#         try:
#             return float(value) >= 0
#         except:
#             return False
#
#     @staticmethod
#     def is_float_negative(value: str) -> bool:
#         try:
#             return float(value) < 0
#         except:
#             return False
#
#     @staticmethod
#     def is_float(value: str) -> bool:
#         try:
#             float(value)
#             return True
#         except:
#             return False
#
#     @staticmethod
#     def is_number(value: str) -> bool:
#         try:
#             float(value)
#             return True
#         except:
#             return False
#
#
# # ============================================================
# #                NumberNormalizer
# # ============================================================
# class NumberNormalizer:
#     @staticmethod
#     def normalize_number(value: str) -> str:
#         if not value.strip():
#             return "0"
#
#         value = value.strip().replace(" ", "")
#         value = value.replace(",", ".")
#
#         if value == "":
#             return "0"
#
#         return value
#
#
# # ============================================================
# #                EntryNormalizer
# # ============================================================
# class EntryNormalizer:
#     @staticmethod
#     def normalize_entries(entry: tk.Entry) -> str:
#         value = entry.get()
#         return NumberNormalizer.normalize_number(value)
#
#
# # ============================================================
# #                CalculatorApp
# # ============================================================
# class CalculatorApp:
#     def __init__(self, master, ammount: int, sign: Literal["+", "-"]):
#         self.master = master
#         self.ammount = ammount
#         self.sign = sign
#
#         self.list_entries: list[tk.Entry] = []
#         self.list_values: list[str] = []
#
#         # row offset depending on sign
#         self.start_row = 0 if sign == "+" else 3
#
#         # UI
#         self.create_ui()
#
#     # -------------------------------------------------------
#     #                  UI Creation
#     # -------------------------------------------------------
#     def create_ui(self):
#         row = self.start_row
#
#         # Header label
#         tk.Label(self.master, text=f"Операция: {self.sign}").grid(row=row, column=0, columnspan=10)
#         row += 1
#
#         # Create input fields
#         for i in range(self.ammount):
#             entry = tk.Entry(self.master, width=8)
#             entry.grid(row=row, column=i * 2)
#             self.list_entries.append(entry)
#
#             if i < self.ammount - 1:
#                 tk.Label(self.master, text=self.sign).grid(row=row, column=i * 2 + 1)
#
#         # Button "="
#         btn = tk.Button(
#             self.master,
#             text="=",
#             command=self.calculate_plus if self.sign == "+" else self.calculate_minus
#         )
#         btn.grid(row=row, column=self.ammount * 2)
#
#         # Result field
#         self.result_entry = tk.Entry(self.master, width=10)
#         self.result_entry.grid(row=row, column=self.ammount * 2 + 1)
#         self.result_entry.config(state="readonly")
#
#         # Error label
#         self.label_error = tk.Label(self.master, text="", fg="red")
#         row += 1
#         self.label_error.grid(row=row, column=0, columnspan=12)
#
#     # -------------------------------------------------------
#     #               VALUE EXTRACTION LOGIC
#     # -------------------------------------------------------
#     def get_values(self):
#         self.list_values.clear()
#
#         for i, entry in enumerate(self.list_entries):
#             normalized_value = EntryNormalizer.normalize_entries(entry)
#
#             if not NumberValidator.is_number(normalized_value):
#                 self.label_error.config(text=f"Значение №{i+1} не является числом")
#                 messagebox.showerror("Ошибка", f"Значение №{i+1} не является числом: {normalized_value}")
#                 return None
#
#             self.list_values.append(float(normalized_value))
#
#         self.label_error.config(text="")
#         return self.list_values
#
#     # -------------------------------------------------------
#     #                     OPERATIONS
#     # -------------------------------------------------------
#     def _write_result(self, value):
#         # Convert 26.0 → 26
#         if isinstance(value, float) and value.is_integer():
#             value = int(value)
#
#         self.result_entry.config(state="normal")
#         self.result_entry.delete(0, tk.END)
#         self.result_entry.insert(0, str(value))
#         self.result_entry.config(state="readonly")
#
#     def calculate_plus(self):
#         values = self.get_values()
#         if values is None:
#             return
#         result = sum(values)
#         self._write_result(result)
#
#     def calculate_minus(self):
#         values = self.get_values()
#         if values is None:
#             return
#         first = values[0]
#         total_rest = sum(values[1:])
#         result = first - total_rest
#         self._write_result(result)
#
#
# # ============================================================
# #                MAIN APPLICATION
# # ============================================================
# def main():
#     window = tk.Tk()
#     window.title("Калькулятор")
#     window.resizable(False, False)
#
#     # calculators
#     app_plus = CalculatorApp(window, ammount=10, sign="+")
#     app_minus = CalculatorApp(window, ammount=10, sign="-")
#
#     window.mainloop()
#
#
# if __name__ == "__main__":
#     main()


import tkinter as tk
from typing import Literal, List, Optional


# --- Классы утилит (согласно Class Diagram) ---

class NumberValidator:
    """
    Класс для проверки валидности чисел.
    """

    @staticmethod
    def is_number(value: str) -> bool:
        try:
            float(value)
            return True
        except ValueError:
            return False

    # Дополнительные методы из диаграммы (заглушки для полноты структуры)
    @staticmethod
    def is_int(value: str) -> bool:
        try:
            int(value)
            return True
        except ValueError:
            return False


class NumberNormalizer:
    """
    Класс для нормализации строкового представления числа.
    """

    @staticmethod
    def normalize_number(value: str) -> str:
        # Удаляем пробелы
        value_clear = value.strip()
        # Заменяем запятую на точку
        value_clear = value_clear.replace(',', '.')

        # Если значение пустое, возвращаем "0"
        if not value_clear:
            return "0"
        return value_clear


class EntryNormalizer:
    """
    Класс для извлечения и нормализации данных из поля ввода.
    """

    @staticmethod
    def normalize_entries(entry: tk.Entry) -> str:
        value = entry.get()
        return NumberNormalizer.normalize_number(value)


# --- Основной класс калькулятора (согласно Class Diagram и Sequence Diagram) ---

class CalculatorApp:
    def __init__(self, master: tk.Widget, amount: int, sign: Literal["+", "-"]):
        self.master = master
        self.amount = amount
        self.sign = sign
        self.list_entries: List[tk.Entry] = []
        self.list_values: List[float] = []

        # Создаем фрейм для группировки элементов этого калькулятора
        # Это позволяет разместить AppPlus и AppMinus независимо друг от друга
        self.frame = tk.Frame(master, pady=10)
        self.frame.pack()

        # Заголовок секции (для ясности)
        operation_name = "Сложение" if sign == "+" else "Вычитание"
        tk.Label(self.frame, text=f"Операция: {operation_name}", font=("Arial", 10, "bold")).pack(anchor="w")

        # Фрейм для строки ввода
        input_frame = tk.Frame(self.frame)
        input_frame.pack()

        # --- Часть 2 и 3: Создание интерфейса ---
        for i in range(self.amount):
            # Создание поля ввода
            entry = tk.Entry(input_frame, width=5)
            entry.pack(side=tk.LEFT, padx=2)
            self.list_entries.append(entry)

            # Создание метки знака (если не последнее поле)
            if i < self.amount - 1:
                lbl = tk.Label(input_frame, text=self.sign)
                lbl.pack(side=tk.LEFT)

        # Кнопка "="
        btn_command = self.calculate_plus if sign == "+" else self.calculate_minus
        self.btn = tk.Button(input_frame, text="=", command=btn_command)
        self.btn.pack(side=tk.LEFT, padx=5)

        # Поле результата (только чтение)
        self.result_field = tk.Entry(input_frame, width=10, state="readonly")
        self.result_field.pack(side=tk.LEFT)

        # Метка ошибки (размещение в следующей строке)
        self.label_error = tk.Label(self.frame, text="", fg="red")
        self.label_error.pack(anchor="w")

    def _get_values(self) -> bool:
        """
        Приватный метод для сбора, нормализации и валидации значений.
        Возвращает True, если все успешно, иначе False.
        """
        self.list_values.clear()
        self.label_error.config(text="")  # Очистка ошибки

        for i, entry in enumerate(self.list_entries):
            # Нормализация
            normalized_val = EntryNormalizer.normalize_entries(entry)

            # Валидация
            if NumberValidator.is_number(normalized_val):
                self.list_values.append(float(normalized_val))
            else:
                # Ошибка
                error_text = f"Значение в поле #{i + 1} не является числом"
                self.label_error.config(text=error_text)
                return False
        return True

    def _display_result(self, result: float):
        """
        Вспомогательный метод для отображения результата согласно диаграмме.
        """
        # Проверка: целое или дробное
        if result.is_integer():
            final_res = str(int(result))
        else:
            final_res = str(result)  # Или f"{result:.2f}" для округления

        # Обновление поля результата
        self.result_field.config(state="normal")  # Разрешить редактирование
        self.result_field.delete(0, tk.END)  # Очистить
        self.result_field.insert(0, final_res)  # Вставить
        self.result_field.config(state="readonly")  # Запретить редактирование

    def calculate_plus(self):
        """
        Часть 4: Обработка операции сложения
        """
        if not self._get_values():
            return

        # Логика: сумма всех значений
        result = sum(self.list_values)
        self._display_result(result)

    def calculate_minus(self):
        """
        Часть 5: Обработка операции вычитания
        """
        if not self._get_values():
            return

        # Логика: первое значение - сумма остальных
        if not self.list_values:
            result = 0.0
        else:
            first_val = self.list_values[0]
            rest_sum = sum(self.list_values[1:])
            result = first_val - rest_sum

        self._display_result(result)


# --- Часть 1: Инициализация приложения ---

def main():
    # Создание главного окна
    window = tk.Tk()
    window.title("Калькулятор")
    window.resizable(False, False)  # Запрет изменения размера

    # Создание экземпляра калькулятора сложения (window, количество=10)
    app_plus = CalculatorApp(window, amount=10, sign="+")

    # Создание экземпляра калькулятора вычитания (window, количество=10)
    app_minus = CalculatorApp(window, amount=10, sign="-")

    # Запуск цикла обработки событий
    window.mainloop()


if __name__ == "__main__":
    main()
