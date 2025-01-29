напиши код на py который преобразует plantuml в py код вот plantuml
```plantuml
@startuml
skinparam classAttributeIconSize 0

interface _SwitchCases {
    __ Constructor __
    +__init__(line: str):
    """
    info constructor
    """
    __ Attributes __
    -__line: str
    __ Methods __
    +upper(): -> str
    """
    info upper
    """
    ..
    +lower(): str
    """
    info lower
    """
    ..
    +title(): str
    """
    info title
    """
}

interface _JustifyString {
    __ Constructor __
    +__init__(line: str):
    """
    info constructor
    """
    __ Attributes __
    -__line: str
    __ Methods __
    +center(width:int, fill_char:str): str
    """
    info center
    """
    ..
    +left_just(width:int, fill_char:str): str
    """
    info left_just
    """
    ..
    +right_just(width:int, fill_char:str): str
    """
    info right_just
    """
}

@enduml
```
код который должен получиться в результате и ты должен написать скрипт чтобы он такой же получился и скрипт должен сохранить этот код в файл .py:
```
from abc import ABC, abstractmethod


class _JustifyString(ABC):
    def __init__(self, line: str):
        """
        info constructor
        """
        self.__line = line

    @abstractmethod
    def center(self, width: int, fill_char: str) -> str:
        """
        info center
        """
        raise NotImplementedError()

    @abstractmethod
    def left_just(self, width: int, fill_char: str) -> str:
        """
        info left_just
        """
        raise NotImplementedError()
    
    @abstractmethod
    def right_just(self, width: int, fill_char: str) -> str:
        """
        info right_just
        """
        raise NotImplementedError()


class _SwitchCases(ABC):
    def __init__(self, line: str):
        """
        info constructor
        """
        self.__line = line

    @abstractmethod
    def upper(self) -> str:
        """
        info upper
        """
        raise NotImplementedError()

    @abstractmethod
    def lower(self) -> str:
        """
        info lower
        """
        raise NotImplementedError()
    
    @abstractmethod
    def title(self) -> str:
        """
        info title
        """
        raise NotImplementedError()
```