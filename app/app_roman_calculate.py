# from tkinter import *
#
# numbers = [
#     ['I', 1],
#     ['II', 2],
#     ['III', 3],
#     ['IV', 4],
#     ['V', 5],
#     ['VI', 6],
#     ['VII', 7],
#     ['VIII', 8],
#     ['IX', 9],
#     ['X', 10],
#     ['XX', 20],
#     ['XXX', 30],
#     ['XL', 40],
#     ['L', 50],
#     ['LX', 60],
#     ['LXX', 70],
#     ['LXXX', 80],
#     ['XC', 90],
#     ['C', 100],
#     ['CC', 200],
#     ['CCC', 300],
#     ['CD', 400],
#     ['D', 500],
#     ['DC', 600],
#     ['DCC', 700],
#     ['DCCC', 800],
#     ['CM', 900],
# ]
#
# roman_units = [roman_number[0] for roman_number in numbers][:9]
# roman_dozens = [roman_number[0] for roman_number in numbers][9:18]
# roman_hundreds = [roman_number[0] for roman_number in numbers][18:]
#
#
# def is_rim_number(value: str) -> bool:
#     return value == ''.join(split_roman_number(value))
#
#
# def split_roman_number(value: str) -> list:
#     result = []
#     for list_numbers in (numbers[18:], numbers[9:18], numbers[:9]):
#         result_roman = ''
#         for roman_number, int_number in list_numbers:
#             if value.startswith(roman_number):
#                 result_roman = roman_number
#         value = value.removeprefix(result_roman)
#         result.append(result_roman)
#     return result
#
#
# def rim_to_int(value: str) -> int:
#     roman_numbers = split_roman_number(value)
#     return sum(int_number for roman_number, int_number in numbers if roman_number in roman_numbers)
#
#
# def int_to_rim(value: int) -> str:
#     result = ''
#     value = str(value)
#     for roman_number, int_number in numbers:
#         for index, number in enumerate(value):
#             number = f"{number}{'0' * (len(value) - 1 - index)}"
#             if int(number) == int_number:
#                 result = f'{roman_number}{result}'
#     return result
#
#
# def is_int_number(number: str) -> bool:
#     return number.isdigit()
#
#
# def main(widget_in: Entry, widget_out: Label) -> None:
#     if is_int_number(widget_in.get()):
#         result = int_to_rim(int(widget_in.get()))
#     elif is_rim_number(widget_in.get().upper()):
#         result = rim_to_int(widget_in.get().upper())
#     else:
#         result = 'Это не число'
#     widget_out.config(text=result)
#
#
# root = Tk()
# root.title('Convert Roman')
# entry = Entry()
# entry.pack(side=LEFT)
# button = Button(text='Convert', command=lambda: main(entry, label))
# button.pack(side=LEFT)
# label = Label()
# label.pack(side=LEFT)
#
# root.mainloop()


# from operator import add, sub
# from typing import List
#
# sign_labels = {
#     "+": add,
#     "-": sub,
# }
#
# numbers = [
#     ['I', 1],
#     ['II', 2],
#     ['III', 3],
#     ['IV', 4],
#     ['V', 5],
#     ['VI', 6],
#     ['VII', 7],
#     ['VIII', 8],
#     ['IX', 9],
#     ['X', 10],
#     ['XX', 20],
#     ['XXX', 30],
#     ['XL', 40],
#     ['L', 50],
#     ['LX', 60],
#     ['LXX', 70],
#     ['LXXX', 80],
#     ['XC', 90],
#     ['C', 100],
#     ['CC', 200],
#     ['CCC', 300],
#     ['CD', 400],
#     ['D', 500],
#     ['DC', 600],
#     ['DCC', 700],
#     ['DCCC', 800],
#     ['CM', 900],
# ]
#
# signs = ['+', '-']
#
# roman_units = [roman_number[0] for roman_number in numbers][:9]
# roman_dozens = [roman_number[0] for roman_number in numbers][9:18]
# roman_hundreds = [roman_number[0] for roman_number in numbers][18:]
#
#
# # class RomanNumber:
#
#
# # class RomanExample:
# # class App:
# def is_rim_number(value: str) -> bool:
#     return value == ''.join(split_roman_number(value))
#
#
# def split_roman_number(value: str) -> list:
#     result = []
#     for list_numbers in (numbers[18:], numbers[9:18], numbers[:9]):
#         result_roman = ''
#         for roman_number, int_number in list_numbers:
#             if value.startswith(roman_number):
#                 result_roman = roman_number
#         value = value.removeprefix(result_roman)
#         result.append(result_roman)
#     return result
#
#
# def int_to_rim(value: int) -> str:
#     result = ''
#     value = str(value)
#     for roman_number, int_number in numbers:
#         for index, number in enumerate(value):
#             number = f"{number}{'0' * (len(value) - 1 - index)}"
#             if int(number) == int_number:
#                 result = f'{roman_number}{result}'
#     return result
#
#
# def rim_to_int(value: str) -> int:
#     roman_numbers = split_roman_number(value)
#     return sum(int_number for roman_number, int_number in numbers if roman_number in roman_numbers)
#
#
# def get_example_as_list(value: str) -> list:
#     result = []
#     element = ''
#     for char in value.upper():
#         if char == '+' or char == '-':
#             result.append(element)
#             element = ''
#             result.append(char)
#         elif char != ' ':
#             element += char
#     result.append(element) if element else None
#     return result
#
#
# def is_rome_example(example: List[str]) -> bool:
#     count_plus = example.count(signs[0])
#     count_minus = example.count(signs[1])
#     is_one_sign = count_minus + count_plus == len(example) // 2
#     return all((is_rim_number(char) or char in signs) and example[-1].isalpha() and is_one_sign for char in example)
#
#
# def calculate(example: list) -> str:
#     result = 0
#     sign = ''
#     for element in example:
#         if is_rim_number(element) and sign:
#             result = sign_labels[sign](result, rim_to_int(element))
#         elif is_rim_number(element):
#             result = rim_to_int(element)
#         else:
#             sign = element
#     return f'-{int_to_rim(result)}' if '-' in str(result) else int_to_rim(result)
#
#
# def main() -> None:
#     example = input('Enter romane example:\t').strip().upper()
#     example = get_example_as_list(example)
#     if is_rome_example(example):
#         print(calculate(example))
#     else:
#         print('error, try again')
#         main()
#
#
# if __name__ == '__main__':
#     main()


from operator import add, sub
from typing import List, Union

sign_labels = {
    "+": add,
    "-": sub,
}

NUMBERS = [
    ['I', 1],
    ['II', 2],
    ['III', 3],
    ['IV', 4],
    ['V', 5],
    ['VI', 6],
    ['VII', 7],
    ['VIII', 8],
    ['IX', 9],
    ['X', 10],
    ['XX', 20],
    ['XXX', 30],
    ['XL', 40],
    ['L', 50],
    ['LX', 60],
    ['LXX', 70],
    ['LXXX', 80],
    ['XC', 90],
    ['C', 100],
    ['CC', 200],
    ['CCC', 300],
    ['CD', 400],
    ['D', 500],
    ['DC', 600],
    ['DCC', 700],
    ['DCCC', 800],
    ['CM', 900],
]

signs = ['+', '-']


class Errors:
    @staticmethod
    def type_error(value, type_value):
        raise TypeError(f'{value} this is not {type_value}')

    @staticmethod
    def value_error(value):
        raise ValueError(f"invalid literal for value_error(): '{value}'. Use only positive Romane number.")

    @staticmethod
    def number_error(value):
        raise ValueError(f"Number must be positive and can't be '0' number_error(): '{value}'")

    @staticmethod
    def romane_error(value):
        raise ValueError(f"Wrong romane number romane_error(): '{value}'")

    @staticmethod
    def calculate_error(value, expression):
        raise ValueError(f"Result calculate expression must be positive: '{expression} = {value}'")


class RomanNumber:
    def __init__(self, value: Union[str, int], numbers: List[List[Union[str, int]]]):
        self.__numbers = numbers
        self.number_roman = value
        self.number_int = self.__rim_to_int()

    @property
    def number_roman(self):
        return self.__number_roman

    @number_roman.setter
    def number_roman(self, value: Union[str, int]):
        if type(value) == int:
            self.__number_int = value
            self.__number_roman = self.__int_to_rim()
            return
        Errors.value_error(value) if type(value) != str else None
        value = value.upper()
        Errors.romane_error(value) if not self.__is_rim_number(value) else None

        self.__number_roman = value
        self.__number_int = self.__rim_to_int()

    @property
    def number_int(self):
        return self.__number_int

    @number_int.setter
    def number_int(self, value: int):
        Errors.value_error(value) if type(value) != int else None
        Errors.number_error(value) if not str(value).isdigit() and value == 0 else None

        self.__number_int = value
        self.__number_roman = self.__int_to_rim()

    def __is_rim_number(self, value=None) -> bool:
        value = self.number_roman if not value else value
        return value == ''.join(self.__split_roman_number(value))

    def __split_roman_number(self, value: str) -> list:
        result = []
        temp_number = value
        for list_numbers in (self.__numbers[18:], self.__numbers[9:18], self.__numbers[:9]):
            result_roman = ''
            for roman_number, int_number in list_numbers:
                if temp_number.startswith(roman_number):
                    result_roman = roman_number
            temp_number = temp_number.removeprefix(result_roman)
            result.append(result_roman)
        return result

    def __int_to_rim(self, value=0) -> str:
        result = ''
        temp_str_number = str(self.__number_int) if value == 0 else str(value)
        for roman_number, int_number in self.__numbers:
            for index, number in enumerate(temp_str_number):
                number = f"{number}{'0' * (len(temp_str_number) - 1 - index)}"
                if int(number) == int_number:
                    result = f'{roman_number}{result}'
        return result

    def __rim_to_int(self, value='') -> int:
        roman_numbers = self.__split_roman_number(self.number_roman) if not value else self.__split_roman_number(value)
        return sum(int_number for roman_number, int_number in self.__numbers if roman_number in roman_numbers)

    def __add__(self, roman_number: 'RomanNumber') -> 'RomanNumber':
        Errors.romane_error(roman_number) if not roman_number else None
        return RomanNumber(self.__number_int + roman_number.number_int, self.__numbers)

    def __sub__(self, roman_number: 'RomanNumber') -> 'RomanNumber':
        Errors.romane_error(roman_number) if not roman_number else None

        int_result = self.__number_int - roman_number.number_int
        error_params = f"-{self.__int_to_rim(abs(int_result))}", f'{self.number_roman} - {roman_number}'
        Errors.calculate_error(*error_params) if int_result < 0 else None
        romane_result = self.__int_to_rim(int_result)
        return RomanNumber(romane_result, self.__numbers)

    def __lt__(self, roman_number: 'RomanNumber') -> bool:
        Errors.romane_error(roman_number) if not roman_number else None
        return self.number_int < roman_number.number_int

    def __le__(self, roman_number: 'RomanNumber') -> bool:
        Errors.romane_error(roman_number) if not roman_number else None
        return self.number_int <= roman_number.number_int

    def __eq__(self, roman_number: 'RomanNumber') -> bool:
        Errors.romane_error(roman_number) if not roman_number else None
        return self.number_int == roman_number.number_int

    def __bool__(self) -> bool:
        return self.__is_rim_number()

    def __str__(self) -> str:
        return self.__number_roman

    def __int__(self) -> int:
        return self.__number_int


class RomanExample:
    def __init__(self, example: str):
        self.example = example

    @property
    def example(self):
        return self.__example

    @example.setter
    def example(self, value: str):
        Errors.type_error(value, str) if not isinstance(value, str) else None
        self.__example = value.replace(' ', '').upper()
        Errors.romane_error(value) if not self.__is_rome_example() else None

    def __get_example_as_list(self) -> list:
        result = []
        element = ''
        for char in self.__example.upper():
            if char == '+' or char == '-':
                result.append(element)
                element = ''
                result.append(char)
            elif char != ' ':
                element += char
        result.append(element) if element else None
        return result

    def __is_rome_example(self) -> bool:
        example = self.__get_example_as_list()
        count_plus = example.count(signs[0])
        count_minus = example.count(signs[1])
        is_one_sign = count_minus + count_plus == len(example) // 2
        last_char_true = len(example) >= 1 and example[-1].isalpha()

        result = len(example) >= 1
        for char in example:
            if not ((char in signs or RomanNumber(char, NUMBERS).number_roman) and last_char_true and is_one_sign):
                result = False
                break
        return result

    @staticmethod
    def __split_example(example: str) -> list:
        result = []
        example_number = ''
        for value in example:
            if value in sign_labels:
                result.extend([example_number, value])
                example_number = ''
            else:
                example_number += value
        result.append(example_number)
        return result

    def calculate(self) -> RomanNumber:
        result = None
        sign = ''
        for element in self.__split_example(self.__example):
            if element not in sign_labels and not sign:
                result = RomanNumber(element, NUMBERS)
            elif element in sign_labels:
                sign = element
            elif sign:
                result = sign_labels[sign](result, RomanNumber(element, NUMBERS))

        return result

    def __str__(self):
        return f'{self.example}={self.calculate()}'

    def __add__(self, value: "RomanExample") -> RomanNumber:
        return self.calculate() + value.calculate()


if __name__ == '__main__':
    example = input('Enter romane example:\t')
    print(RomanExample(example).calculate())
