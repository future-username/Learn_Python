# Вспомогательные функции

def validate_input(data):
    """Проверка входных данных.
    
    Args:
        data: Данные для проверки
        
    Returns:
        bool: Результат проверки
    """
    if data is None:
        return False
    return True


def format_output(data):
    """Форматирование выходных данных.
    
    Args:
        data: Данные для форматирования
        
    Returns:
        Отформатированные данные
    """
    # Здесь будет логика форматирования
    return data


def log_operation(operation_name, status):
    """Логирование операций.
    
    Args:
        operation_name (str): Название операции
        status (bool): Статус выполнения
        
    Returns:
        None
    """
    print(f"Операция {operation_name}: {'успешно' if status else 'неудачно'}")