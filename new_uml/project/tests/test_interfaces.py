# Тесты для интерфейсов

import unittest
from my_module.interfaces import DataProcessor, DataValidator
from my_module.stub import StubDataProcessor, StubDataValidator


class TestInterfaces(unittest.TestCase):
    """Тесты для интерфейсов."""
    
    def test_data_processor_implementation(self):
        """Тест реализации интерфейса DataProcessor."""
        processor = StubDataProcessor()
        self.assertTrue(isinstance(processor, DataProcessor))
        
        test_data = "test data"
        result = processor.process(test_data)
        self.assertEqual(result, test_data)
    
    def test_data_validator_implementation(self):
        """Тест реализации интерфейса DataValidator."""
        validator = StubDataValidator()
        self.assertTrue(isinstance(validator, DataValidator))
        
        test_data = "test data"
        result = validator.validate(test_data)
        self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()