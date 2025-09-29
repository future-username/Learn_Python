from tkinter import *


class NumberValidator:
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
            return int(value) == float(value)
        except ValueError:
            return False

    @staticmethod
    def is_float_positive(value: str) -> bool:
        try:
            return float(value) > 0 and '.' in value
        except ValueError:
            return False

    @staticmethod
    def is_float_negative(value: str) -> bool:
        try:
            return float(value) < 0 and '.' in value
        except ValueError:
            return False

    @staticmethod
    def is_float(value: str) -> bool:
        try:
            return float(value) and '.' in value
        except ValueError:
            return False

    @staticmethod
    def is_number(value: str) -> bool:
        return NumberValidator.is_int(value) or NumberValidator.is_float(value) or value == "0" or value == "0.0"


class NumberNormalizer:
    @staticmethod
    def normalize_number(value: str) -> str:
        return value.replace(' ', '').replace(',', '.')


class EntryNormalizer:
    @staticmethod
    def normalize_entries(value: Entry) -> str:
        value_clear = NumberNormalizer.normalize_number(value.get())
        value.delete(0, END)
        value.insert(0, value_clear)
        return value_clear


class CalculatorApp:
    def __init__(self, master):
        self.master = master
        master.title("Simple Calculator")

        self.first_plus = Entry(master, width=20, bg="white")
        self.first_plus.grid(column=0, row=0, padx=5, pady=5)
        Label(master, text='+', fg="black").grid(column=1, row=0, padx=5, pady=5)
        self.second_plus = Entry(master, width=20, bg="white")
        self.second_plus.grid(column=2, row=0, padx=5, pady=5)
        Button(master, text="=", fg="black", command=self.calculate_plus).grid(column=3, row=0, padx=5, pady=5)
        self.result_plus = Entry(master, width=20, bg="white")
        self.result_plus.grid(column=4, row=0, padx=5, pady=5)

    def calculate_plus(self):
        first_normalize = EntryNormalizer.normalize_entries(self.first_plus)
        second_normalize = EntryNormalizer.normalize_entries(self.second_plus)

        self.result_plus.delete(0, END)
        try:
            if NumberValidator.is_number(first_normalize) and NumberValidator.is_number(second_normalize):
                self.result_plus.insert(0, float(first_normalize) + float(second_normalize))
            else:
                self.result_plus.insert(0, "Ошибка")
        except ValueError:
            self.result_plus.insert(0, "Ошибка")


if __name__ == '__main__':
    root = Tk()
    app = CalculatorApp(root)
    root.mainloop()