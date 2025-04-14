class _SwitchCases:
    def __init__(self, line: str):
        """
        Return line: исходная строка
        """
        self._line = line

    def upper(self) -> str:
        """
        Return copy of the string in upper case
        """
        raise NotImplementedError()

    def lower(self) -> str:
        raise NotImplementedError()

    def title(self) -> str:
        raise NotImplementedError()