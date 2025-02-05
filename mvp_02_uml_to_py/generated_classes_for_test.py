class _SwitchCases:
    def __init__(self, line: str):
        self.__line = line

    def upper(self) -> str:
        raise NotImplementedError()

    def lower(self) -> str:
        raise NotImplementedError()

    def title(self) -> str:
        raise NotImplementedError()


class _IsString:
    def __init__(self, line: str):
        self.__line = line

    def isupper(self) -> bool:
        raise NotImplementedError()

    def islower(self) -> bool:
        raise NotImplementedError()

    def istitle(self) -> bool:
        raise NotImplementedError()


class _JustifyString:
    def __init__(self, line: str):
        self.__line = line

    def center(self, width: int, fill_char: str) -> str:
        raise NotImplementedError()

    def left_just(self, width: int, fill_char: str) -> str:
        raise NotImplementedError()

    def right_just(self, width: int, fill_char: str) -> str:
        raise NotImplementedError()
