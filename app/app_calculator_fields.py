# from tkinter import *
#
#
# def calculate_plus():
#     if first_plus.get() != '' and second_plus.get() != "" and \
#             first_plus.get().isnumeric() and second_plus.get().isnumeric():
#         result_plus.delete(0, END)
#         result_plus.insert(0, float(first_plus.get())+float(second_plus.get()))
#
#
# def calculate_minus():
#     if first_minus.get() != '' and second_minus.get() != "" and first_minus.get().isnumeric() and \
#             second_minus.get().isnumeric():
#         result_minus.delete(0, END)
#         result_minus.insert(0, float(first_minus.get())-float(second_minus.get()))
#
#
# def calculate_multiplication():
#     if first_multiplication.get() != '' and second_multiplication.get() != "" and \
#             first_multiplication.get().isnumeric() and second_multiplication.get().isnumeric():
#         result_multiplication.delete(0, END)
#         result_multiplication.insert(0, float(first_multiplication.get())*float(second_multiplication.get()))
#
#
# def calculate_division():
#     if first_division.get() != '' and second_division.get() != "" and second_division.get() != "0" and \
#             first_division.get().isnumeric() and second_division.get().isnumeric():
#         result_division.delete(0, END)
#         result_division.insert(0, float(first_division.get())/float(second_division.get()))
#
#
# root = Tk()
# root.title("Calculate example")
#
# sign_labels = ["+", "-", "/", "*", "**", "//", "%"]
# for n in range(len(sign_labels)):
#     Entry(root, width=10, bg="white").grid(column=0, row=n)
#     Label(root, text=sign_labels[n], fg="black").grid(column=1, row=n)
#     Entry(root, width=10, bg="white").grid(column=3, row=n)
#     Button(root, text="=", fg="black").grid(column=4, row=n)
#     Entry(root, width=10, bg="white").grid(column=5, row=n)
#
# root.mainloop()

#
# from tkinter import *
#
#
# def is_int_positive(value):
#     return value.isdigit()
#
#
# def is_int_negative(value):
#     return value.count('-') == 1 and value.removeprefix('-').isdigit()
#
#
# def is_int(value):
#     return is_int_positive(value) or is_int_negative(value)
#
#
# def is_float_positive(value):
#     return value.count('.') == 1 and value.replace('.', '').isdigit()
#
#
# def is_float_negative(value):
#     return value.count('.') == 1 and value.count('-') == 1 and value.replace('.', '').replace('-', '').isdigit()
#
#
# def is_float(value):
#     return is_float_positive(value) or is_float_negative(value)
#
#
# def is_number(value):
#     return is_int(value) or is_float(value)
#
#
# def normalize_number(value: str) -> str:
#     return value.replace(' ', '').replace(',', '.')
#
#
# def normalize_entries(entry_first: Entry, entry_second: Entry, entry_result: Entry) -> tuple:
#     first_normalize = normalize_number(entry_first.get())
#     entry_first.delete(0, END)
#     entry_first.insert(0, first_normalize)
#
#     second_normalize = normalize_number(entry_second.get())
#     entry_second.delete(0, END)
#     entry_second.insert(0, second_normalize)
#
#     entry_result.delete(0, END)
#     return first_normalize, second_normalize
#
#
# def calculate_plus():
#     first_normalize, second_normalize = normalize_entries(first_plus, second_plus, result_plus)
#
#     if is_number(first_normalize) and is_number(second_normalize):
#         result_plus.insert(0, float(first_normalize)+float(second_normalize))
#
#
# def calculate_minus():
#     first_normalize = normalize_number(first_minus.get())
#     first_minus.delete(0, END)
#     first_minus.insert(0, first_normalize)
#
#     second_normalize = normalize_number(second_minus.get())
#     second_minus.delete(0, END)
#     second_minus.insert(0, second_normalize)
#
#     result_minus.delete(0, END)
#
#     if is_number(first_normalize) and is_number(second_normalize):
#         result_minus.insert(0, float(first_normalize) - float(second_normalize))
# #
# #
# # def calculate_multiplication():
# #     if first_multiplication.get() != '' and second_multiplication.get() != "" and \
# #             first_multiplication.get().isnumeric() and second_multiplication.get().isnumeric():
# #         result_multiplication.delete(0, END)
# #         result_multiplication.insert(0, float(first_multiplication.get())*float(second_multiplication.get()))
# #
# #
# # def calculate_division():
# #     if first_division.get() != '' and second_division.get() != "" and second_division.get() != "0" and \
# #             first_division.get().isnumeric() and second_division.get().isnumeric():
# #         result_division.delete(0, END)
# #         result_division.insert(0, float(first_division.get())/float(second_division.get()))
#
#
# root = Tk()
# root.title("Calculate example")
#
# first_plus = Entry(root, width=10, bg="white")
# first_plus.grid(column=0, row=0)
# Label(root, text='+', fg="black").grid(column=1, row=0)
# second_plus = Entry(root, width=10, bg="white")
# second_plus.grid(column=3, row=0)
# Button(root, text="=", fg="black", command=calculate_plus).grid(column=4, row=0)
# result_plus = Entry(root, width=10, bg="white")
# result_plus.grid(column=5, row=0)
#
# first_minus = Entry(root, width=10, bg="white")
# first_minus.grid(column=0, row=1)
# Label(root, text='-', fg="black").grid(column=1, row=1)
# second_minus = Entry(root, width=10, bg="white")
# second_minus.grid(column=3, row=1)
# Button(root, text="=", fg="black", command=calculate_minus).grid(column=4, row=1)
# result_minus = Entry(root, width=10, bg="white")
# result_minus.grid(column=5, row=1)
#
#
# root.mainloop()


# from tkinter import *
#
# root = Tk()
# root.title("Calculate example")
#
# sign_labels = ["+", "-", "/", "*", "**", "//", "%"]
# for index, sign in enumerate(sign_labels):
#     Entry(root, width=10, bg="white").grid(column=0, row=index)
#     Label(root, text=sign, fg="black").grid(column=1, row=index)
#     Entry(root, width=10, bg="white").grid(column=3, row=index)
#     Button(root, text="=", fg="black").grid(column=4, row=index)
#     Entry(root, width=10, bg="white").grid(column=5, row=index)
#
# root.mainloop()


# from tkinter import *
# from operator import add, sub, truediv, mul, pow, floordiv, mod
#
# # sign_labels = ["+", "-", "/", "*", "**", "//", "%"]
# sign_labels = {
#     "+": add,
#     "-": sub,
#     "/": truediv,
#     "*": mul,
#     "**": pow,
#     "//": floordiv,
#     "%": mod
# }
# COUNT_FIELD = 3
#
#
# def is_int_positive(value):
#     return value.isdigit()
#
#
# def is_int_negative(value):
#     return value.count('-') == 1 and value.removeprefix('-').isdigit()
#
#
# def is_int(value):
#     return is_int_positive(value) or is_int_negative(value)
#
#
# def is_float_positive(value):
#     return value.count('.') == 1 and value.replace('.', '').isdigit()
#
#
# def is_float_negative(value):
#     return value.count('.') == 1 and value.count('-') == 1 and value.replace('.', '').replace('-', '').isdigit()
#
#
# def is_float(value):
#     return is_float_positive(value) or is_float_negative(value)
#
#
# def is_number(value: str) -> bool:
#     return is_int(value) or is_float(value)
#
#
# def normalize_number(value: str) -> str:
#     return value.replace(' ', '').replace(',', '.')
#
#
# # def normalize_entries(entry_first: Entry, entry_second: Entry, entry_result: Entry) -> tuple:
# #     first_normalize = normalize_number(entry_first.get())
# #     entry_first.delete(0, END)
# #     entry_first.insert(0, first_normalize)
# #
# #     second_normalize = normalize_number(entry_second.get())
# #     entry_second.delete(0, END)
# #     entry_second.insert(0, second_normalize)
# #
# #     entry_result.delete(0, END)
# #     return first_normalize, second_normalize
# #
# #
# # def calculate(first: Entry, second: Entry, result: Entry, sign) -> None:
# #     first_normalize, second_normalize = normalize_entries(first, second, result)
# #
# #     if is_number(first_normalize) and is_number(second_normalize) and sign == '+':
# #         result.insert(0, float(first_normalize) + float(second_normalize))
# #
# #     elif is_number(first_normalize) and is_number(second_normalize) and sign == '-':
# #         result.insert(0, float(first_normalize) - float(second_normalize))
# #
# #     elif is_number(first_normalize) and is_number(second_normalize) and sign == "*":
# #         result.insert(0, float(first_normalize) * float(second_normalize))
# #
# #     elif is_number(first_normalize) and is_number(second_normalize) and sign == "/":
# #         result.insert(0, float(first_normalize) / float(second_normalize))
# #
# #     elif is_number(first_normalize) and is_number(second_normalize) and sign == "**":
# #         result.insert(0, float(first_normalize) ** float(second_normalize))
# #     elif is_number(first_normalize) and is_number(second_normalize) and sign == "//":
# #         result.insert(0, float(first_normalize) // float(second_normalize))
# #     elif is_number(first_normalize) and is_number(second_normalize) and sign == "%":
# #         result.insert(0, float(first_normalize) % float(second_normalize))
#
#
# # def normalize_entries(entry_normalize: Entry, result) -> str:
# #     first_normalize = normalize_number(entry_normalize.get())
# #     entry_normalize.delete(0, END)
# #     entry_normalize.insert(0, first_normalize)
# #     result.delete(0, END)
# #     # return first_normalize
# # def calculate(fields: list, field_result: Entry, sign: str) -> None:
# #     field_result.delete(0, END)
# #     result = float(fields[0].get()) if is_number(fields[0].get()) else 0
# #
# #     for count, field in enumerate(fields):
# #         line_normalize = normalize_number(field.get())
# #
# #         field.delete(0, END)
# #         field.insert(0, line_normalize)
# #         if line_normalize and is_number(line_normalize) and sign == '+' and count > 0:
# #             result += float(line_normalize)
# #         elif line_normalize and is_number(line_normalize) and sign == '-' and count > 0:
# #             result -= float(line_normalize)
# #         elif line_normalize and is_number(line_normalize) and sign == '*' and count > 0:
# #             result *= float(line_normalize)
# #         elif line_normalize and is_number(line_normalize) and sign == '/' and count > 0:
# #             try:
# #                 result /= float(line_normalize)
# #             except ZeroDivisionError:
# #                 result = 0
# #         elif line_normalize and is_number(line_normalize) and sign == '//' and count > 0:
# #             try:
# #                 result //= float(line_normalize)
# #             except ZeroDivisionError:
# #                 result = 0
# #         elif line_normalize and is_number(line_normalize) and sign == '**' and count > 0:
# #             result **= float(line_normalize)
# #         elif line_normalize and is_number(line_normalize) and sign == '%' and count > 0:
# #             try:
# #                 result %= float(line_normalize)
# #             except ZeroDivisionError:
# #                 result = 0
# #
# #     field_result.insert(0, result)
#
#
# # def calculate(fields: list, field_result: Entry, sign: str) -> None:
# #     field_result.delete(0, END)
# #     result = float(fields[0].get()) if is_number(fields[0].get()) else 0
# #
# #     for count, field in enumerate(fields):
# #         line_normalize = normalize_number(field.get())
# #
# #         field.delete(0, END)
# #         field.insert(0, line_normalize)
# #         if line_normalize and is_number(line_normalize) and sign == '+' and count > 0:
# #             result += float(line_normalize)
# #         elif line_normalize and is_number(line_normalize) and sign == '-' and count > 0:
# #             result -= float(line_normalize)
# #         elif line_normalize and is_number(line_normalize) and sign == '*' and count > 0:
# #             result *= float(line_normalize)
# #         elif line_normalize and is_number(line_normalize) and sign == '/' and count > 0:
# #             try:
# #                 result /= float(line_normalize)
# #             except ZeroDivisionError:
# #                 result = 0
# #         elif line_normalize and is_number(line_normalize) and sign == '//' and count > 0:
# #             try:
# #                 result //= float(line_normalize)
# #             except ZeroDivisionError:
# #                 result = 0
# #         elif line_normalize and is_number(line_normalize) and sign == '**' and count > 0:
# #             result **= float(line_normalize)
# #         elif line_normalize and is_number(line_normalize) and sign == '%' and count > 0:
# #             try:
# #                 result %= float(line_normalize)
# #             except ZeroDivisionError:
# #                 result = 0
# #
# #     field_result.insert(0, result)
#
#
# def normalize_numbers(fields: list) -> None:
#     for field in fields:
#         line_normalize = normalize_number(field.get())
#         field.delete(0, END)
#         field.insert(0, line_normalize)
#
#
# def calculate(fields: list, field_result: Entry, sign: str) -> None:
#     result = float(fields[0].get())
#
#     for count, field in enumerate(fields):
#         line_normalize = normalize_number(field.get())
#
#         if count > 0:
#             result = sign_labels[sign](result, float(line_normalize))
#
#     field_result.insert(0, result)
#
#
# def check(fields: list) -> bool:
#     """
#     There is list only numbers
#
#     :param fields: list
#     :return: bool
#     """
#
#     true_numbers = 0
#     for index, field in enumerate(fields):
#         if is_number(field.get()) and index > 0:
#             field.config(bg='white')
#             true_numbers += 1
#         else:
#             field.config(bg='pink')
#     return true_numbers == len(fields)
#
#
# def main(fields: list, field_result: Entry, sign: str):
#     field_result.delete(0, END)
#     normalize_fields = [field for field in fields if field.get()]
#     normalize_numbers(normalize_fields)
#
#     if check(normalize_fields) and normalize_fields:
#         calculate(normalize_fields, field_result, sign)
#     else:
#         field_result.insert(0, 'ERROR')
#
#
# root = Tk()
# root.title("Calculate example")
#
# for row, sign_label in enumerate(sign_labels):
#     list_entry = []
#     for index in range(COUNT_FIELD):
#         entry = Entry(root, width=10, bg="white")
#         entry.grid(column=index * 2, row=row)
#         list_entry.append(entry)
#         result_entry = Entry(root, width=10, bg="white")
#         result_entry.grid(column=COUNT_FIELD * 2, row=row)
#         if index + 1 != COUNT_FIELD:
#             label = Label(root, text=sign_label, fg="black")
#             label.grid(column=index * 2 + 1, row=row)
#
#     get_result = lambda fields=list_entry, result=result_entry, sign=sign_label: main(fields, result, sign)
#     button = Button(root, text="=", fg="black", command=get_result)
#     button.grid(column=COUNT_FIELD * 2 - 1, row=row)
#
# root.mainloop()


from tkinter import *
from typing import Callable, Any
from functools import reduce

import json
import operator


class StringNumber:
    def __init__(self, value: str):
        self.__value = value

    def is_int_positive(self) -> bool:
        return self.__value.isdigit()

    def is_int_negative(self) -> bool:
        return self.__value.count('-') == 1 and self.__value.removeprefix('-').isdigit()

    def is_int(self) -> bool:
        return self.is_int_positive() or self.is_int_negative()

    def is_float_positive(self) -> bool:
        return self.__value.count('.') == 1 and self.__value.replace('.', '').isdigit()

    def is_float_negative(self) -> bool:
        return self.__value.count('.') == 1 and self.__value.count('-') == 1 \
            and self.__value.replace('.', '').replace('-', '').isdigit()

    def is_float(self) -> bool:
        return self.is_float_positive() or self.is_float_negative()

    def is_number(self) -> bool:
        return self.is_int() or self.is_float()

    def normalize_number(self) -> str:
        return self.__value.replace(' ', '').replace(',', '.')


class Errors:
    @staticmethod
    def type_error(value: Any, type_value: type):
        raise TypeError(f'{value} this is not {type_value}')


class MathExample:
    def __init__(self, parent: Tk, amount_field: int, sign_label: str, operator: Callable):
        """
        MathExample

        :param parent:
        :param amount_field:
        :param sign_label:
        :param operator:
        """
        self.__parent = parent if isinstance(parent, Tk) else Errors.type_error(parent, Tk)
        self.__amount_field = amount_field if isinstance(amount_field, int) else Errors.type_error(amount_field, int)
        self.__sign_label = sign_label if isinstance(sign_label, str) else Errors.type_error(sign_label, str)
        self.__operator = operator if isinstance(operator, Callable) else Errors.type_error(operator, Callable)

        self.__list_entries = []
        self.__result_entry = Entry(self.__parent, width=10, bg="white")

    def __normalize_numbers(self) -> None:
        self.__result_entry.delete(0, END)
        for field in self.__list_entries:
            line_normalize = StringNumber(field.get()).normalize_number()
            field.delete(0, END)
            field.insert(0, line_normalize)

    def __calculate(self) -> None:
        self.__normalize_numbers()
        numbers = (float(field.get()) for field in self.__list_entries)
        result = str(reduce(self.__operator, numbers)) if self.__list_entries and self.__check() else 'ERROR'
        self.__result_entry.insert(0, result)

    def __check(self) -> bool:
        """
        There is list only numbers

        :return: bool
        """

        true_numbers = 0
        for field in self.__list_entries:
            field.config(bg='white')

            check_zero_division = field.get() != '0' or self.__sign_label not in ("/", "//", "%")
            if StringNumber(field.get()).is_number() and check_zero_division:
                true_numbers += 1
            else:
                field.config(bg='pink')

        return true_numbers == len(self.__list_entries)

    def draw_line(self, row: int):
        row = row if isinstance(row, int) else Errors.type_error(row, int)

        for index in range(self.__amount_field):
            entry = Entry(self.__parent, width=10, bg="white")
            entry.grid(column=index * 2, row=row)
            self.__list_entries.append(entry)

            not_last_entry = index + 1 != self.__amount_field
            if not_last_entry:
                Label(self.__parent, text=self.__sign_label, fg="black").grid(column=index * 2 + 1, row=row)

        self.__result_entry.grid(column=self.__amount_field * 2, row=row)

        _ = Button(self.__parent, text="=", fg="black", command=self.__calculate)
        _.grid(column=self.__amount_field * 2 - 1, row=row)


class App:
    def __init__(self, title: str, amount_field: int, sign_labels: dict):
        self.__title = title if isinstance(title, str) else Errors.type_error(title, str)
        self.__amount_field = amount_field if isinstance(amount_field, int) else Errors.type_error(amount_field, int)
        self.__sign_labels = sign_labels if isinstance(sign_labels, dict) else Errors.type_error(sign_labels, dict)

        self.__root = Tk()
        self.__root.title(title)

        for row, sign_label in enumerate(sign_labels):
            sign_label_func = getattr(operator, self.__sign_labels[sign_label])
            MathExample(self.__root, self.__amount_field, sign_label, sign_label_func).draw_line(row)

    def draw(self):
        self.__root.mainloop()


if __name__ == '__main__':
    with open("app_calculator_filds.json", "r") as read_file:
        data = json.load(read_file)

    App(data['TITLE'], data['COUNT_FIELD'], data['SIGN_LABELS']).draw()
