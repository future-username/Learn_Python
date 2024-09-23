from tkinter import *
from typing import Any
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


class Model:
    def __init__(self):
        self.__values = []
        self.__values_numbers = []
        self.__answer = 0

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
    def answer(self):
        return self.__answer

    @answer.setter
    def answer(self, value):
        if isinstance(value, str):
            self.__answer = value
        else:
            raise TypeError(f'{value} this is not dict')

    def __normalize_numbers(self) -> None:
        for field in self.__values:
            line_normalize = StringNumber(str(field.get())).normalize_number()
            field.delete(0, END)
            field.insert(0, line_normalize)

    def calculate(self, sign) -> str:
        self.__normalize_numbers()
        if self.__values and self.__check(sign):
            self.__values_numbers = [float(value.get()) for value in self.__values]

        sign_label_func = getattr(operator, list(sign.values())[0])
        return str(reduce(sign_label_func, self.__values_numbers)) if self.__values and self.__check(sign) else 'ERROR'

    def __check(self, sign) -> bool:
        """
        There is list only numbers
        :return: bool
        """
        true_numbers = 0
        for field in self.__values:
            field.config(bg='white')
            check_zero_division = field.get() != 0 or sign.keys() not in ("/", "//", "%")
            if StringNumber(str(field.get())).is_number() and check_zero_division:
                true_numbers += 1
            else:
                field.config(bg='pink')

        return true_numbers == len(self.__values)


class View:
    def __init__(self, parent, sign, amount_field, row):
        self.__parent = parent if isinstance(parent, Tk) else Errors.type_error(parent, Tk)
        self.__list_values = []
        self.__result_entry = Entry(self.__parent, width=10, bg="white")
        self.amount_field = amount_field
        self.__row = row
        self.__sign = sign
        self.controller = None
        self.__draw_line()

    @property
    def result_entry(self) -> Entry:
        return self.__result_entry

    def set_controller(self, controller):
        """
        Set the controller
        :param controller:
        :return:
        """
        self.controller = controller
        # controller.draw_view()

    def calculate(self, model) -> None:
        self.__result_entry.delete(0, END)
        model.values = self.__list_values
        result = model.calculate(self.__sign)
        self.__result_entry.insert(0, result)
        model.answer = result

    def __draw_line(self):
        for index in range(self.amount_field):
            entry = Entry(self.__parent, width=10, bg="white")
            entry.grid(column=index * 2, row=self.__row)
            self.__list_values.append(entry)

            not_last_entry = index + 1 != self.amount_field
            if not_last_entry:
                Label(self.__parent, text=list(self.__sign.keys())[0],
                      fg="black").grid(column=index * 2 + 1, row=self.__row)

        self.__result_entry.grid(column=self.amount_field * 2, row=self.__row)

        _ = Button(self.__parent, text="=", fg="black", command=self.__check_controller)
        _.grid(column=self.amount_field * 2 - 1, row=self.__row)

    def __check_controller(self):
        if self.controller:
            self.controller.do_calculate()


class Controller:
    def __init__(self, model: Model, view: View):
        self.__model = model
        self.__view = view

    def do_calculate(self):
        try:
            self.__view.calculate(self.__model)
        except Exception as e:
            raise e


class App(Tk):
    def __init__(self):
        super().__init__()
        with open("app_calculator_filds.json", "r") as read_file:
            data = json.load(read_file)

        self.title(data['TITLE'])
        model = Model()

        view = View(parent=self, sign={"+": "add"}, amount_field=3,
                    row=0)  # todo like method command in Button (sign=operator(1, sign))
        view1 = View(parent=self, sign={"-": "sub"}, amount_field=3, row=1)

        controller = Controller(model, view)
        controller1 = Controller(model, view1)

        view.set_controller(controller)
        view1.set_controller(controller1)


if __name__ == '__main__':
    App().mainloop()
