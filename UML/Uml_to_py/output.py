from abc import ABC, abstractmethod


class _SwitchCases(ABC):
    def __init__(self, line: str):
        """info constructor"""
        self.__line = line

    @abstractmethod
    def upper(self) -> None:
        """info upper"""
        raise NotImplementedError()

    @abstractmethod
    def lower(self) -> str:
        """info lower"""
        raise NotImplementedError()

    @abstractmethod
    def title(self) -> str:
        """info title"""
        raise NotImplementedError()

class _JustifyString(ABC):
    def __init__(self, line: str):
        """info constructor"""
        self.__line = line

    @abstractmethod
    def center(self, width: int, fill_char: str) -> str:
        """info center"""
        raise NotImplementedError()

    @abstractmethod
    def left_just(self, width: int, fill_char: str) -> str:
        """info left_just"""
        raise NotImplementedError()

    @abstractmethod
    def right_just(self, width: int, fill_char: str) -> str:
        """info right_just"""
        raise NotImplementedError()

class _MyString(ABC):
    def __init__(self, number: str):
        """info constructor"""
        self.__number = number

        self.__number_234 = number

        self.__number_5454 = number

        self.__number_3745 = number

    @abstractmethod
    def name(self) -> None:
        """info name"""
        raise NotImplementedError()

    @abstractmethod
    def password(self) -> int:
        """info password"""
        raise NotImplementedError()

    @abstractmethod
    def title_234(self) -> str:
        """info title_234"""
        raise NotImplementedError()

    @abstractmethod
    def title_2346(self) -> list:
        """info title_2346"""
        raise NotImplementedError()
