# Тесты для основной логики

import unittest
from my_module.core import Core


class TestCore(unittest.TestCase):
    """Тесты для класса Core."""
    
    def setUp(self):
        """Подготовка к тестам."""
        self.core = Core()
    
    def test_initialization(self):
        """Тест инициализации."""
        self.assertFalse(self.core.initialized)
        result = self.core.initialize()
        self.assertTrue(result)
        self.assertTrue(self.core.initialized)
    
    def test_process_data_without_initialization(self):
        """Тест обработки данных без инициализации."""
        with self.assertRaises(RuntimeError):
            self.core.process_data("test data")
    
    def test_process_data(self):
        """Тест обработки данных."""
        self.core.initialize()
        result = self.core.process_data("test data")
        self.assertEqual(result, "test data")


if __name__ == '__main__':
    unittest.main()