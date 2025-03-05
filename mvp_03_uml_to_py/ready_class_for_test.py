class _SwitchCases:
    """
    class contains some methods which switch chars
    """
    def __init__(self, line: str):
        self.__line = line

    def upper(self) -> str:
        raise NotImplementedError()

    def lower(self) -> str:
        raise NotImplementedError()

    def title1(self, value: str, number: int) -> str:
        raise NotImplementedError()

    def title2(self, value: str = 'string', number: int = 0) -> str:
        raise NotImplementedError()