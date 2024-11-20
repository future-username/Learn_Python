# """
# На какой парттерн проектирования похожа реализация кода,
# в результате которой происходи группировка методов основного класса
# String на подгруппы методов.
# """
#
#
# class StringCheck:
#     def __init__(self, text: str):
#         self.__text = text
#
#     def is_lower(self):
#         return self.__text.islower()
#
#     def is_upper(self):
#         return self.__text.isupper()
#
#     def is_title(self):
#         return self.__text.istitle()
#
#
# class StringSwitchCase:
#     def __init__(self, text: str):
#         self.__text = text
#
#     def lower(self):
#         return self.__text.lower()
#
#     def upper(self):
#         return self.__text.upper()
#
#     def title(self):
#         return self.__text.title()
#
#
# class MyString:
#     def __init__(self, text: str):
#         self.__text = text
#         self.check = StringCheck(self.__text)
#         self.switch_case = StringSwitchCase(self.__text)
#         self.justify = self.__text.ljust()
#
#     @property
#     def check(self):
#         return StringCheck(self.__text)
#
#     @property
#     def switch_case(self):
#         return StringSwitchCase(self.__text)
#
#     @property
#     def justify(self):
#         return self.__text.ljust()
#
#
# line = MyString('AnY tExT.')
# print(line.switch_case.lower())
# print(line.check.is_lower())


from functools import wraps


"""
Парттерн Фасад: реализация кода в результате которой,
происходи группировка методов основного класса String на подгруппы методов.
"""


class StringCheck:
    def __init__(self, text: str):
        self.__text = text

    def is_lower(self):
        return self.__text.islower()

    def is_upper(self):
        return self.__text.isupper()

    def is_title(self):
        return self.__text.istitle()


class StringSwitchCase:
    def __init__(self, text: str):
        self.__text = text

    def lower(self):
        return self.__text.lower()

    def upper(self):
        return self.__text.upper()

    def title(self):
        return self.__text.title()


class StringJustify:
    def __init__(self, text: str):
        self.__text = text

    def center(self, width: int, fill_char: str = " ") -> str:
        return self.__text.center(width, fill_char)

    def left_just(self, width: int, fill_char: str = " ") -> str:
        return self.__text.ljust(width, fill_char)

    def right_just(self, width: int, fill_char: str = " ") -> str:
        return self.__text.rjust(width, fill_char)


class MyString:
    def __init__(self, text: str):
        self.__text = text
        self.check = StringCheck(self.__text)
        self.switch_case = StringSwitchCase(self.__text)
        self.justify = StringJustify(self.__text)


line = MyString('AnY tExT.')
print(line.switch_case.lower())
print(line.check.is_lower())
