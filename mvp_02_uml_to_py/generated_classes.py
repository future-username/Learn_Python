class _SwitchCases:
    def __init__(self, line: str):
        self.__line = line

    def upper(self, ):
        raise NotImplementedError()

    def lower(self, ):
        raise NotImplementedError()

    def title(self, ):
        raise NotImplementedError()

class _IsString:
    def __init__(self, line: str):
        self.__line = line

    def isupper(self, ):
        raise NotImplementedError()

    def islower(self, ):
        raise NotImplementedError()

    def istitle(self, ):
        raise NotImplementedError()

class _JustifyString:
    def __init__(self, line: str):
        self.__line = line

    def center(self, width: int, fill_char: str):
        raise NotImplementedError()

    def left_just(self, width: int, fill_char: str):
        raise NotImplementedError()

    def right_just(self, width: int, fill_char: str):
        raise NotImplementedError()