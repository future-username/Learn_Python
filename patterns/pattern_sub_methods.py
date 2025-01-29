from abc import ABC, abstractmethod


class _MyString(ABC):
    """
    Str with useful group methods
    """

    @abstractmethod
    def __init__(self, line: str):
        """

        :param line:
        """
        raise NotImplementedError()

    @abstractmethod
    @property
    def switch_cases(self) -> list:
        """
        Group of methods str, which changes upper cases and lower cases
        :return: group of useful methods, which objects
        """
        raise NotImplementedError()

    @abstractmethod
    @property
    def justifies(self) -> list:
        """
        getter, Group of methods str, which justify tabs
        :return: group of useful methods, which objects
        """
        raise (NotImplementedError())

    @abstractmethod
    @property
    def is_methods(self) -> list:
        """
        Group of methods str, which check str line
        :return: group of useful methods, which objects
        """
        raise NotImplementedError()

class _SwitchCases(ABC):
    """
    class contains only switch case methods of str
    """

    @abstractmethod
    def __init__(self, line: str):
        """

        :param line:
        """

    @abstractmethod
    def upper(self):
        """
        Return a copy of the string converted to uppercase.
        :return: upper str
        """
        raise NotImplementedError()

    @abstractmethod
    def lower(self):
        """
        Return a copy of B with all ASCII characters converted to lowercase.
        :return: lower str
        """

    @abstractmethod
    def title(self):
        """
        Return a titlecased version of B, i.e. ASCII words start with uppercase
        characters, all remaining cased characters have lowercase.
        :return: title str
        """


class SwitchCases(_SwitchCases):
    def __init__(self, line):
        self.__line = line

    def lower(self):
        return self.__line.lower()

    def title(self):
        return self.__line.title()

    def upper(self):
        return self.__line.upper()


class MyString(_MyString):
    def __init__(self, line):
        self.__line = line

    def is_methods(self):
        return ''

    def justifies(self):
        return ''

    @property
    def switch_cases(self) -> SwitchCases:
        return SwitchCases(self.__line)

    def __str__(self):
        return self.__line


line  = MyString('fdCV  kHVGHvhj         vGHV')
print(line.justifie)
print(line.switch_cases.title())
print(line)
