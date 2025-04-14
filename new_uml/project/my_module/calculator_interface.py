# Интерфейсы для калькулятора

from .interfaces import DataProcessor, DataValidator


class CalculatorProcessor(DataProcessor):
    """Класс для обработки данных калькулятора."""
    
    def __init__(self, calculator):
        """Инициализация процессора калькулятора.
        
        Args:
            calculator: Экземпляр калькулятора
        """
        self.calculator = calculator
    
    def process(self, data):
        """Реализация абстрактного метода для обработки данных.
        
        Args:
            data: Данные для обработки (математическое выражение)
            
        Returns:
            Результат вычисления
        """
        return self.calculator.calculate(data)


class CalculatorValidator(DataValidator):
    """Класс для валидации данных калькулятора."""
    
    def validate(self, data):
        """Реализация абстрактного метода для валидации данных.
        
        Args:
            data: Данные для валидации (математическое выражение)
            
        Returns:
            bool: Результат валидации
        """
        if not data or not isinstance(data, str):
            return False
        
        try:
            # Проверяем, можно ли вычислить выражение
            eval(data)
            return True
        except:
            return False