class _SwitchCases:
    def __init__(self, line: str):
        self._line = line

    @property
    def line(self) -> None:
        return self.line

    @line.setter
    def line(self, value: str):
        self._line = value

    def upper(self) -> str:
        """1Return copy of the string in upper case"""
        raise NotImplementedError()

    def lower(self) -> str:
        raise NotImplementedError()

    def title(self) -> str:
        raise NotImplementedError()