from typing import SupportsIndex, LiteralString


class StringSwitchCase:
    def __init__(self, text: str):
        self.__text = text

    def lower(self):
        return self.__text.lower()

    def upper(self):
        return self.__text.upper()

    def title(self):
        return self.__text.title()

    def center(self: LiteralString,
               __width: SupportsIndex,
               __fillchar: LiteralString = " ") -> LiteralString:
        return self.__text.center()

