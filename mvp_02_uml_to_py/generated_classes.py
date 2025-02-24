class _SwitchCases:
    """class contains some methods which switch chars"""

    def __init__(self, line: str):
        """Constructor
**Args:**
line: исходная строка"""
        self.__line = line


    def upper(self):
        raise NotImplementedError()


    def lower(self):
        raise NotImplementedError()


    def title(self):
        raise NotImplementedError()



class _IsString:
    """class contains some methods which switch chars"""

    def __init__(self, line: str):
        self.__line = line


    def isupper(self):
        raise NotImplementedError()


    def islower(self):
        raise NotImplementedError()


    def istitle(self):
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



class _JustifyString1:
    __line: str = None

    def center(self, width: int, fill_char: str):
        raise NotImplementedError()


    def left_just(self, width: int, fill_char: str):
        raise NotImplementedError()


    def right_just(self, width: int, fill_char: str):
        raise NotImplementedError()

