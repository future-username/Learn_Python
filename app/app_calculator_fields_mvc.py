from tkinter import *
from typing import Callable, Any
from functools import reduce
import operator
import json


class Errors:
    @staticmethod
    def type_error(value: Any, type_value: type):
        raise TypeError(f'{value} this is not {type_value}')


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

    @property
    def result_entry(self) -> Entry:
        return self.__result_entry

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

    # def draw_line(self, row: int):
    #     row = row if isinstance(row, int) else Errors.type_error(row, int)
    #
    #     for index in range(self.__amount_field):
    #         entry = Entry(self.__parent, width=10, bg="white")
    #         entry.grid(column=index * 2, row=row)
    #         self.__list_entries.append(entry)
    #
    #         not_last_entry = index + 1 != self.__amount_field
    #         if not_last_entry:
    #             Label(self.__parent, text=self.__sign_label, fg="black").grid(column=index * 2 + 1, row=row)
    #
    #     self.__result_entry.grid(column=self.__amount_field * 2, row=row)
    #
    #     _ = Button(self.__parent, text="=", fg="black", command=self.__calculate)
    #     _.grid(column=self.__amount_field * 2 - 1, row=row)


class Model:
    def __init__(self):
        self.__values = []
        self.__answer = 0
        self.__sign_label = {"+": "add"}

    @property
    def values(self):
        return self.__values

    @values.setter
    def values(self, value):
        if isinstance(value, list):
            self.__values = value
        else:
            raise TypeError(f'{value} this is not dict')

    @property
    def sign_label(self):
        return self.__sign_label

    @sign_label.setter
    def sign_label(self, value):
        if isinstance(value, dict):
            self.__sign_label = value
        else:
            raise TypeError(f'{value} this is not dict')

    @property
    def answer(self):
        return self.__answer

    @answer.setter
    def answer(self, value):
        if isinstance(value, int):
            self.__answer = value
        else:
            raise TypeError(f'{value} this is not dict')


class View:
    def __init__(self, parent: Tk):
        """
        MathExample
        :param parent:
        """
        # self.__count_fields = count_fields
        # self.__sign_labels = sign_labels
        # self.controller = None
        self.__model: Model | None = None
        self.__parent = parent if isinstance(parent, Tk) else Errors.type_error(parent, Tk)

        # self.__sign_label_func = getattr(operator, self.__model.sign_label[self.__model.sign_label[0]])

        self.__list_entries = []
        self.__result_entry = Entry(self.__parent, width=10, bg="white")
        self.amount_field = 2

    @property
    def result_entry(self) -> Entry:
        return self.__result_entry

    @staticmethod
    def set_controller(controller):
        """
        Set the controller
        :param controller:
        :return:
        """
        # self.controller = controller
        controller.draw_view()

    def __normalize_numbers(self) -> None:
        self.__result_entry.delete(0, END)
        for field in self.__list_entries:
            line_normalize = StringNumber(field.get()).normalize_number()
            field.delete(0, END)
            field.insert(0, line_normalize)

    def __calculate(self) -> None:
        self.__normalize_numbers()
        numbers = (float(field.get()) for field in self.__list_entries)
        sign_label_func = getattr(operator, list(self.__model.sign_label.values())[0])
        result = str(reduce(sign_label_func, numbers)) if self.__list_entries and self.__check() else 'ERROR'

        self.__result_entry.insert(0, result)

        self.__model.values = list(float(field.get()) for field in self.__list_entries)
        self.__model.answer = result

    def __check(self) -> bool:
        """
        There is list only numbers
        :return: bool
        """
        true_numbers = 0
        for field in self.__list_entries:
            field.config(bg='white')

            check_zero_division = field.get() != '0' or self.__model.sign_label[0] not in ("/", "//", "%")
            if StringNumber(field.get()).is_number() and check_zero_division:
                true_numbers += 1
            else:
                field.config(bg='pink')

        return true_numbers == len(self.__list_entries)

    def draw_line(self, model, row: int):
        self.__model = model
        row = row if isinstance(row, int) else Errors.type_error(row, int)

        for index in range(self.amount_field):
            entry = Entry(self.__parent, width=10, bg="white")
            entry.grid(column=index * 2, row=row)
            self.__list_entries.append(entry)

            not_last_entry = index + 1 != self.amount_field
            if not_last_entry:
                Label(self.__parent, text=list(self.__model.sign_label.keys())[0],
                      fg="black").grid(column=index * 2 + 1, row=row)

        self.__result_entry.grid(column=self.amount_field * 2, row=row)
        _ = Button(self.__parent, text="=", fg="black", command=self.__calculate)
        _.grid(column=self.amount_field * 2 - 1, row=row)


class Controller:
    def __init__(self, model: Model, view: View, row: int):
        self.__model = model
        self.__view = view
        self.__row = row

    def draw_view(self):
        try:
            self.__view.draw_line(model=self.__model, row=self.__row)
        except Exception as e:
            raise e


class App(Tk):
    def __init__(self):
        super().__init__()
        with open("app_calculator_filds.json", "r") as read_file:
            data = json.load(read_file)

        self.title(data['TITLE'])
        model = Model()

        view = View(self)


        controller = Controller(model, view, row=0)

        view.set_controller(controller)


if __name__ == '__main__':
    App().mainloop()
