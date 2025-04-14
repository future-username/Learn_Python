# Тесты для модуля калькулятора

import unittest
from my_module.calculator_core import Calculator
from my_module.calculator_interface import CalculatorProcessor, CalculatorValidator
from unittest.mock import patch
import io


class TestCalculator(unittest.TestCase):
    """Тесты для класса Calculator."""
    
    def setUp(self):
        """Подготовка к тестам."""
        self.calculator = Calculator()
        self.calculator.initialize()
    
    def test_add(self):
        """Тест функции сложения."""
        result = self.calculator.add(2, 3)
        self.assertEqual(result, 5)
        
        result = self.calculator.add(-1, 1)
        self.assertEqual(result, 0)
        
        result = self.calculator.add(0.1, 0.2)
        self.assertAlmostEqual(result, 0.3, places=10)
    
    def test_subtract(self):
        """Тест функции вычитания."""
        result = self.calculator.subtract(5, 3)
        self.assertEqual(result, 2)
        
        result = self.calculator.subtract(1, 1)
        self.assertEqual(result, 0)
        
        result = self.calculator.subtract(0.3, 0.1)
        self.assertAlmostEqual(result, 0.2, places=10)
    
    def test_multiply(self):
        """Тест функции умножения."""
        result = self.calculator.multiply(2, 3)
        self.assertEqual(result, 6)
        
        result = self.calculator.multiply(0, 5)
        self.assertEqual(result, 0)
        
        result = self.calculator.multiply(-2, 3)
        self.assertEqual(result, -6)
    
    def test_divide(self):
        """Тест функции деления."""
        result = self.calculator.divide(6, 3)
        self.assertEqual(result, 2)
        
        result = self.calculator.divide(5, 2)
        self.assertEqual(result, 2.5)
        
        with self.assertRaises(ZeroDivisionError):
            self.calculator.divide(5, 0)
    
    def test_calculate(self):
        """Тест функции вычисления выражения."""
        result = self.calculator.calculate("2 + 3")
        self.assertEqual(result, 5)
        
        result = self.calculator.calculate("2 * (3 + 4)")
        self.assertEqual(result, 14)
        
        result = self.calculator.calculate("10 / 2")
        self.assertEqual(result, 5)
        
        with self.assertRaises(ValueError):
            self.calculator.calculate("2 + / 3")
    
    def test_memory_functions(self):
        """Тест функций работы с памятью."""
        # Сохраняем результат в память
        self.calculator.calculate("5 + 5")
        self.calculator.memory_store()
        self.assertEqual(self.calculator.memory, 10)
        
        # Получаем значение из памяти
        memory_value = self.calculator.memory_recall()
        self.assertEqual(memory_value, 10)
        
        # Очищаем память
        self.calculator.memory_clear()
        self.assertEqual(self.calculator.memory, 0)
    
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_logging(self, mock_stdout):
        """Тест логирования операций."""
        self.calculator.add(2, 3)
        self.assertIn("Операция сложение: успешно", mock_stdout.getvalue())
        
        mock_stdout.truncate(0)
        mock_stdout.seek(0)
        
        with self.assertRaises(ValueError):
            self.calculator.add(None, 3)
        self.assertIn("Операция сложение: неудачно", mock_stdout.getvalue())


class TestCalculatorInterfaces(unittest.TestCase):
    """Тесты для интерфейсов калькулятора."""
    
    def setUp(self):
        """Подготовка к тестам."""
        self.calculator = Calculator()
        self.calculator.initialize()
        self.processor = CalculatorProcessor(self.calculator)
        self.validator = CalculatorValidator()
    
    def test_processor(self):
        """Тест процессора калькулятора."""
        result = self.processor.process("2 + 3")
        self.assertEqual(result, 5)
        
        result = self.processor.process("10 - 5")
        self.assertEqual(result, 5)
    
    def test_validator(self):
        """Тест валидатора калькулятора."""
        self.assertTrue(self.validator.validate("2 + 3"))
        self.assertTrue(self.validator.validate("2 * (3 + 4)"))
        self.assertFalse(self.validator.validate("2 + / 3"))
        self.assertFalse(self.validator.validate(""))
        self.assertFalse(self.validator.validate(None))


if __name__ == '__main__':
    unittest.main()