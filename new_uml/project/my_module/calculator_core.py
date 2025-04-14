# Модуль с основной логикой калькулятора

from .core import Core
from .helpers import validate_input, format_output, log_operation


class Calculator(Core):
    """Класс калькулятора, расширяющий базовый класс Core."""
    
    def __init__(self):
        """Инициализация калькулятора."""
        super().__init__()
        self.last_result = 0
        self.memory = 0
    
    def add(self, a, b):
        """Сложение двух чисел.
        
        Args:
            a: Первое число
            b: Второе число
            
        Returns:
            float: Результат сложения
        """
        if not validate_input(a) or not validate_input(b):
            log_operation("сложение", False)
            raise ValueError("Некорректные аргументы для операции сложения")
        
        result = a + b
        self.last_result = result
        log_operation("сложение", True)
        return format_output(result)
    
    def subtract(self, a, b):
        """Вычитание двух чисел.
        
        Args:
            a: Первое число
            b: Второе число
            
        Returns:
            float: Результат вычитания
        """
        if not validate_input(a) or not validate_input(b):
            log_operation("вычитание", False)
            raise ValueError("Некорректные аргументы для операции вычитания")
        
        result = a - b
        self.last_result = result
        log_operation("вычитание", True)
        return format_output(result)
    
    def multiply(self, a, b):
        """Умножение двух чисел.
        
        Args:
            a: Первое число
            b: Второе число
            
        Returns:
            float: Результат умножения
        """
        if not validate_input(a) or not validate_input(b):
            log_operation("умножение", False)
            raise ValueError("Некорректные аргументы для операции умножения")
        
        result = a * b
        self.last_result = result
        log_operation("умножение", True)
        return format_output(result)
    
    def divide(self, a, b):
        """Деление двух чисел.
        
        Args:
            a: Первое число
            b: Второе число
            
        Returns:
            float: Результат деления
        """
        if not validate_input(a) or not validate_input(b):
            log_operation("деление", False)
            raise ValueError("Некорректные аргументы для операции деления")
        
        if b == 0:
            log_operation("деление", False)
            raise ZeroDivisionError("Деление на ноль невозможно")
        
        result = a / b
        self.last_result = result
        log_operation("деление", True)
        return format_output(result)
    
    def calculate(self, expression):
        """Вычисление математического выражения.
        
        Args:
            expression: Строка с математическим выражением
            
        Returns:
            float: Результат вычисления
        """
        if not validate_input(expression):
            log_operation("вычисление", False)
            raise ValueError("Некорректное выражение")
        
        try:
            # Безопасное вычисление выражения
            result = eval(expression)
            self.last_result = result
            log_operation("вычисление", True)
            return format_output(result)
        except Exception as e:
            log_operation("вычисление", False)
            raise ValueError(f"Ошибка при вычислении выражения: {str(e)}")
    
    def memory_store(self):
        """Сохранение последнего результата в память."""
        self.memory = self.last_result
        log_operation("сохранение в память", True)
        return self.memory
    
    def memory_recall(self):
        """Получение значения из памяти."""
        log_operation("чтение из памяти", True)
        return self.memory
    
    def memory_clear(self):
        """Очистка памяти."""
        self.memory = 0
        log_operation("очистка памяти", True)
        return True