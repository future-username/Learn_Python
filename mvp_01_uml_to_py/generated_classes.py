from abc import ABC, abstractmethod

class _SwitchCases(ABC):
    def __init__(self, line: str):
        self.__line = line

    @abstractmethod
    def title(self) -> str:
        raise NotImplementedError()


from abc import ABC, abstractmethod

class _JustifyString(ABC):
    def __init__(self, line: str):
        self.__line = line

    @abstractmethod
    def right_just(self, width: int, fill_char: str) -> str:
        raise NotImplementedError()
