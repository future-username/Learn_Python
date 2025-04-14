# Интерфейсы и абстрактные классы

from abc import ABC, abstractmethod


class DataProcessor(ABC):
    """Абстрактный класс для обработки данных."""
    
    @abstractmethod
    def process(self, data):
        """Абстрактный метод для обработки данных.
        
        Args:
            data: Данные для обработки
            
        Returns:
            Обработанные данные
        """
        pass


class DataValidator(ABC):
    """Абстрактный класс для валидации данных."""
    
    @abstractmethod
    def validate(self, data):
        """Абстрактный метод для валидации данных.
        
        Args:
            data: Данные для валидации
            
        Returns:
            bool: Результат валидации
        """
        pass