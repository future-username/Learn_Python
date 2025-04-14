# Заглушки для тестирования

from .interfaces import DataProcessor, DataValidator


class StubDataProcessor(DataProcessor):
    """Заглушка для класса обработки данных."""
    
    def process(self, data):
        """Реализация метода обработки данных для тестирования.
        
        Args:
            data: Данные для обработки
            
        Returns:
            Обработанные данные (без изменений для заглушки)
        """
        return data


class StubDataValidator(DataValidator):
    """Заглушка для класса валидации данных."""
    
    def validate(self, data):
        """Реализация метода валидации данных для тестирования.
        
        Args:
            data: Данные для валидации
            
        Returns:
            bool: Всегда возвращает True для заглушки
        """
        return True