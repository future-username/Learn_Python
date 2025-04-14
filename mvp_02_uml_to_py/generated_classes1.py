class _SwitchCases:
    """
	class contains some methods which switch chars
	"""

    def __init__(self, line: str):
        """		
		Constructor
		

		**Args:**
			line: исходная строка
		"""
        self.__line = line


    def upper(self) -> str:
        """
		Return copy of the string in upper case
		"""
        raise NotImplementedError()


    def lower(self) -> str:
        """
		Return copy of the string in lower case
		"""
        raise NotImplementedError()


    def title(self) -> str:
        raise NotImplementedError()

