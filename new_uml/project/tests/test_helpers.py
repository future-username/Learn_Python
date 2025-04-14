# Тесты для вспомогательных функций

import unittest
from my_module.helpers import validate_input, format_output, log_operation
from unittest.mock import patch
import io


class TestHelpers(unittest.TestCase):
    """Тесты для вспомогательных функций."""
    
    def test_validate_input(self):
        """Тест функции validate_input."""
        self.assertTrue(validate_input("test data"))
        self.assertTrue(validate_input(123))
        self.assertTrue(validate_input([1, 2, 3]))
        self.assertFalse(validate_input(None))
    
    def test_format_output(self):
        """Тест функции format_output."""
        test_data = "test data"
        result = format_output(test_data)
        self.assertEqual(result, test_data)
    
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_log_operation(self, mock_stdout):
        """Тест функции log_operation."""
        log_operation("test", True)
        self.assertEqual(mock_stdout.getvalue(), "Операция test: успешно\n")
        
        mock_stdout.truncate(0)
        mock_stdout.seek(0)
        
        log_operation("test", False)
        self.assertEqual(mock_stdout.getvalue(), "Операция test: неудачно\n")


if __name__ == '__main__':
    unittest.main()