# Архитектура Python-проекта

Архитектура Python-проекта может значительно варьироваться в зависимости от его типа и сложности, но вот основные шаги и практики, которые помогут структурировать проект:

## 1. *Определение структуры проекта*
   - **Корневая директория**: содержит основные файлы проекта, например `README.md`, `requirements.txt`, файл для лицензии (`LICENSE`), и файл для конфигурации (`.env`).
   - *Папка для исходного кода* (`src` или название вашего проекта): хранит основной код и модули.
   - *Тесты* (`tests`): отдельная папка для тестирования кода.
   - *Документация* (`docs`): хранит файлы с описанием архитектуры, API и пользовательских инструкций.

## 2. *Использование модулей и пакетов*
Разделите код на логически связанные модули и пакеты:
   - **Модули**: отдельные файлы Python для каждой функциональности.
   - **Пакеты**: папки с файлами Python и файлом `__init__.py`.

Пример базовой структуры проекта:

```
project/
├── src/
│   ├── __init__.py
│   ├── main.py
│   ├── module1.py
│   └── module2/
│       ├── __init__.py
│       └── submodule.py
├── tests/
│   ├── test_module1.py
│   └── test_module2.py
├── requirements.txt
├── README.md
└── .env
```

Пример расширенной структуры проекта:

```
project/
├── src/
│   ├── __init__.py
│   ├── main.py
│   ├── core/
│   │   ├── __init__.py
│   │   ├── models.py
│   │   ├── exceptions.py
│   │   └── utils.py
│   ├── api/
│   │   ├── __init__.py
│   │   ├── routes.py
│   │   └── handlers.py
│   ├── services/
│   │   ├── __init__.py
│   │   ├── auth_service.py
│   │   └── data_service.py
│   └── config/
│       ├── __init__.py
│       ├── settings.py
│       └── constants.py
├── tests/
│   ├── unit/
│   │   ├── test_models.py
│   │   └── test_utils.py
│   └── integration/
│       ├── test_api.py
│       └── test_services.py
├── docs/
│   ├── architecture.md
│   ├── api_reference.md
│   └── user_guide.md
├── scripts/
│   ├── setup.py
│   └── deploy.py
├── requirements/
│   ├── base.txt
│   ├── dev.txt
│   └── prod.txt
├── .env.example
├── .gitignore
├── README.md
└── pyproject.toml
```

## 3. *Сторонние зависимости*
   - Используйте `requirements.txt` или `pyproject.toml` (в случае с Poetry) для управления зависимостями.
   - Убедитесь, что используете виртуальное окружение (`venv` или `virtualenv`) для изоляции зависимостей.

### Пример файла requirements.txt:
```
# Основные зависимости
python-dotenv==1.0.0
requests==2.31.0
pydantic==2.4.2

# Веб-фреймворк (если нужен)
fastapi==0.103.1
uvicorn==0.23.2

# Работа с базами данных
sqlalchemy==2.0.21
alembic==1.12.0

# Тестирование
pytest==7.4.2
pytest-cov==4.1.0
```

### Пример файла pyproject.toml (для Poetry):
```toml
[tool.poetry]
name = "my-project"
version = "0.1.0"
description = "Описание проекта"
authors = ["Your Name <your.email@example.com>"]

[tool.poetry.dependencies]
python = "^3.10"
python-dotenv = "^1.0.0"
requests = "^2.31.0"
pydantic = "^2.4.2"

[tool.poetry.group.dev.dependencies]
pytest = "^7.4.2"
pytest-cov = "^4.1.0"
black = "^23.9.1"
isort = "^5.12.0"
flake8 = "^6.1.0"

[build-system]
requires = ["poetry-core>=1.0.0"]
build-backend = "poetry.core.masonry.api"
```

## 4. *Тестирование*
   - Настройте автоматизированные тесты, используя `unittest`, `pytest` или другой фреймворк.
   - Интегрируйте CI/CD для проверки тестов перед развертыванием.

### Пример структуры тестов:
```python
# tests/unit/test_models.py
import pytest
from src.core.models import User

def test_user_creation():
    user = User(id=1, name="Test User", email="test@example.com")
    assert user.name == "Test User"
    assert user.email == "test@example.com"

def test_user_validation():
    with pytest.raises(ValueError):
        User(id=1, name="Test User", email="invalid-email")
```

## 5. *Конфигурация проекта*

Существует несколько подходов к конфигурации Python-проектов:

### 5.1. Переменные окружения

Используйте библиотеку `python-dotenv` для загрузки переменных окружения из файла `.env`:

```python
# src/config/settings.py
import os
from dotenv import load_dotenv

# Загрузка переменных из .env файла
load_dotenv()

# Базовые настройки
DEBUG = os.getenv("DEBUG", "False").lower() == "true"
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")

# Настройки базы данных
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = int(os.getenv("DB_PORT", "5432"))
DB_NAME = os.getenv("DB_NAME", "mydb")
DB_USER = os.getenv("DB_USER", "postgres")
DB_PASSWORD = os.getenv("DB_PASSWORD", "")

# Формирование строки подключения к БД
DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# API настройки
API_KEY = os.getenv("API_KEY")
API_VERSION = os.getenv("API_VERSION", "v1")
```

### 5.2. YAML/JSON конфигурация

Для более сложных конфигураций удобно использовать YAML или JSON файлы:

```python
# src/config/settings.py
import os
import yaml
from pathlib import Path

# Определение пути к конфигурационному файлу
config_path = os.getenv("CONFIG_PATH", Path(__file__).parent / "config.yaml")

# Загрузка конфигурации из YAML файла
with open(config_path, "r") as f:
    config = yaml.safe_load(f)

# Доступ к настройкам
DEBUG = config.get("debug", False)
LOG_LEVEL = config.get("logging", {}).get("level", "INFO")

# Настройки базы данных
db_config = config.get("database", {})
DATABASE_URL = f"postgresql://{db_config.get('user')}:{db_config.get('password')}@{db_config.get('host')}:{db_config.get('port')}/{db_config.get('name')}"
```

### 5.3. Конфигурация для разных окружений

Создайте отдельные конфигурационные файлы для разных окружений:

```python
# src/config/settings.py
import os

# Определение текущего окружения
ENVIRONMENT = os.getenv("ENVIRONMENT", "development")

# Базовые настройки для всех окружений
class BaseConfig:
    DEBUG = False
    LOG_LEVEL = "INFO"
    API_VERSION = "v1"

# Настройки для разработки
class DevelopmentConfig(BaseConfig):
    DEBUG = True
    LOG_LEVEL = "DEBUG"
    DB_HOST = "localhost"
    DB_NAME = "dev_db"

# Настройки для тестирования
class TestingConfig(BaseConfig):
    DEBUG = True
    LOG_LEVEL = "DEBUG"
    DB_HOST = "localhost"
    DB_NAME = "test_db"

# Настройки для продакшена
class ProductionConfig(BaseConfig):
    LOG_LEVEL = "WARNING"
    DB_HOST = os.getenv("DB_HOST")
    DB_NAME = os.getenv("DB_NAME")

# Выбор конфигурации в зависимости от окружения
config_by_environment = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "production": ProductionConfig
}

# Активная конфигурация
Config = config_by_environment.get(ENVIRONMENT, DevelopmentConfig)
```

### 5.4. Управление секретами

Для безопасного хранения секретов используйте специализированные инструменты:

- **HashiCorp Vault** - для централизованного управления секретами
- **AWS Secrets Manager** или **Azure Key Vault** - для облачных решений
- **Ansible Vault** - для шифрования конфигурационных файлов

Пример использования с AWS Secrets Manager:

```python
import boto3
from botocore.exceptions import ClientError

def get_secret(secret_name, region_name="us-east-1"):
    session = boto3.session.Session()
    client = session.client(service_name="secretsmanager", region_name=region_name)
    
    try:
        response = client.get_secret_value(SecretId=secret_name)
        return response["SecretString"]
    except ClientError as e:
        raise e

# Получение секрета
db_credentials = get_secret("db-credentials")
```

## 6. *Логирование*

Настройка логирования с использованием стандартного модуля `logging`:

```python
# src/utils/logger.py
import logging
import os
from logging.handlers import RotatingFileHandler
from pathlib import Path

from src.config.settings import Config

# Создание директории для логов, если она не существует
logs_dir = Path("logs")
logs_dir.mkdir(exist_ok=True)

# Настройка логгера
def setup_logger(name):
    logger = logging.getLogger(name)
    logger.setLevel(getattr(logging, Config.LOG_LEVEL))
    
    # Форматирование логов
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    
    # Обработчик для вывода в консоль
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)
    
    # Обработчик для записи в файл с ротацией
    file_handler = RotatingFileHandler(
        logs_dir / "app.log",
        maxBytes=10485760,  # 10 MB
        backupCount=5
    )
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    
    return logger
```

## 7. *Документирование*
   - Используйте `docstrings` для документирования кода.
   - Генерируйте документацию с помощью инструментов вроде Sphinx.

### Пример документирования функции:
```python
def calculate_total(items, tax_rate=0.1):
    """
    Рассчитывает общую стоимость товаров с учетом налога.
    
    Args:
        items (list): Список товаров с ценами.
        tax_rate (float, optional): Ставка налога в виде десятичной дроби. По умолчанию 0.1 (10%).
        
    Returns:
        float: Общая стоимость с учетом налога.
        
    Raises:
        ValueError: Если список товаров пуст или содержит отрицательные цены.
        TypeError: Если tax_rate не является числом.
        
    Examples:
        >>> calculate_total([10, 20, 30])
        66.0
        >>> calculate_total([100], tax_rate=0.2)
        120.0
    """
    if not items:
        raise ValueError("Список товаров не может быть пустым")
        
    if any(price < 0 for price in items):
        raise ValueError("Цены не могут быть отрицательными")
        
    if not isinstance(tax_rate, (int, float)):
        raise TypeError("Ставка налога должна быть числом")
        
    subtotal = sum(items)
    total = subtotal * (1 + tax_rate)
    
    return total
```

## 8. *UML-диаграммы*

UML-диаграммы помогают визуализировать архитектуру проекта и взаимодействие между компонентами.

### 8.1. Диаграмма классов

Диаграмма классов отображает структуру классов, их атрибуты, методы и отношения между ними.

```
+------------------+       +------------------+
|      User        |       |     Profile      |
+------------------+       +------------------+
| - id: int        |       | - id: int        |
| - username: str  |<>-----| - user_id: int   |
| - email: str     |       | - bio: str       |
| - password: str  |       | - avatar: str    |
+------------------+       +------------------+
| + authenticate() |       | + update()       |
| + get_profile()  |       | + get_avatar()   |
+------------------+       +------------------+
         ^                          
         |                          
         |                          
+------------------+                
|    AdminUser     |                
+------------------+                
| - role: str      |                
+------------------+                
| + grant_access() |                
+------------------+                
```

### 8.2. Диаграмма последовательностей

Диаграмма последовательностей показывает взаимодействие объектов во времени.

```
+--------+    +-------------+    +------------+    +----------+
| Client |    | AuthService |    | UserModel  |    | Database |
+--------+    +-------------+    +------------+    +----------+
    |                |                |                 |
    | login(creds)   |                |                 |
    |--------------->|                |                 |
    |                | validate(creds)|                 |
    |                |--------------->|                 |
    |                |                | query(username) |
    |                |                |---------------->|
    |                |                |                 |
    |                |                |  return user    |
    |                |                |<----------------|
    |                |  return user   |                 |
    |                |<---------------|                 |
    |                |                |                 |
    |                | check_password()|                |
    |                |----------------|                 |
    |                |                |                 |
    |                | generate_token()|                |
    |                |----------------|                 |
    |  return token  |                |                 |
    |<---------------|                |                 |
    |                |                |                 |
```

### 8.3. Диаграмма компонентов

Диаграмма компонентов показывает организацию и зависимости между компонентами системы.

```
+-------------------+     +-------------------+
|     Web Layer     |     |    API Layer      |
+-------------------+     +-------------------+
|  - Templates      |     |  - REST Endpoints |
|  - Static Files   |     |  - Serializers    |
|  - Forms          |     |  - Validators     |
+-------------------+     +-------------------+
          |                         |
          v                         v
+-------------------+     +-------------------+
|   Service Layer   |<--->|  External APIs   |
+-------------------+     +-------------------+
|  - Business Logic |     |  - Payment API   |
|  - Validation     |     |  - Email Service |
|  - Orchestration  |     |  - Storage API   |
+-------------------+     +-------------------+
          |
          v
+-------------------+     +-------------------+
|    Data Layer     |<--->|    Database      |
+-------------------+     +-------------------+
|  - Models         |     |  - PostgreSQL    |
|  - Repositories   |     |  - Redis Cache   |
|  - Data Access    |     |  - MongoDB       |
+-------------------+     +-------------------+
```

### 8.4. Диаграмма состояний

Диаграмма состояний показывает возможные состояния объекта и переходы между ними.

```
+----------------+     +----------------+     +----------------+
|    Создан      |---->|   Активирован  |---->|   Заблокирован |
+----------------+     +----------------+     +----------------+
        |                      ^                      |
        |                      |                      |
        v                      |                      v
+----------------+             |             +----------------+
|   Ожидание     |-------------             |   Удален       |
+----------------+                          +----------------+
```

## 9. *Утилиты проекта*

### 9.1. Обработка ошибок

```python
# src/core/exceptions.py
class AppException(Exception):
    """Базовый класс для всех исключений приложения"""
    def __init__(self, message="Произошла ошибка в приложении", status_code=500):
        self.message = message
        self.status_code = status_code
        super().__init__(self.message)

class ValidationError(AppException):
    """Ошибка валидации данных"""
    def __init__(self, message="Ошибка валидации данных", status_code=400, errors=None):
        self.errors = errors or {}
        super().__init__(message, status_code)

class AuthenticationError(AppException):
    """Ошибка аутентификации"""
    def __init__(self, message="Ошибка аутентификации", status_code=401):
        super().__init__(message, status_code)
```

### 9.2. Валидация данных

```python
# src/utils/validators.py
import re
from typing import Dict, Any, List, Optional
from src.core.exceptions import ValidationError

class Validator:
    """Базовый класс для валидации данных"""
    
    @staticmethod
    def validate_email(email: str) -> bool:
        """Проверяет корректность email-адреса"""
        pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return bool(re.match(pattern, email))
    
    @staticmethod
    def validate_password(password: str) -> bool:
        """Проверяет сложность пароля"""
        # Минимум 8 символов, хотя бы одна буква и одна цифра
        pattern = r'^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$'
        return bool(re.match(pattern, password))
```

### 9.3. Кэширование

```python
# src/utils/cache.py
import time
from functools import wraps
from typing import Dict, Any, Callable, Optional

class SimpleCache:
    """Простая реализация кэша в памяти"""
    
    def __init__(self, default_ttl: int = 300):
        """Инициализация кэша
        
        Args:
            default_ttl: Время жизни кэша в секундах по умолчанию (5 минут)
        """
        self.cache: Dict[str, Dict[str, Any]] = {}
        self.default_ttl = default_ttl
    
    def set(self, key: str, value: Any, ttl: Optional[int] = None) -> None:
        """Сохраняет значение в кэш"""
        ttl = ttl if ttl is not None else self.default_ttl
        expires_at = time.time() + ttl
        
        self.cache[key] = {
            'value': value,
            'expires_at': expires_at
        }
    
    def get(self, key: str) -> Optional[Any]:
        """Получает значение из кэша"""
        if key not in self.cache:
            return None
        
        cache_item = self.cache[key]
        if time.time() > cache_item['expires_at']:
            # Удаляем просроченный элемент
            del self.cache[key]
            return None
        
        return cache_item['value']
```

### 9.4. Мониторинг и профилирование

```python
# src/utils/profiler.py
import time
import functools
import cProfile
import pstats
import io
from typing import Callable, Any

def timeit(func: Callable) -> Callable:
    """Декоратор для измерения времени выполнения функции"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Функция {func.__name__} выполнилась за {end_time - start_time:.4f} секунд")
        return result
    return wrapper

def profile(func: Callable) -> Callable:
    """Декоратор для профилирования функции"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        profiler = cProfile.Profile()
        profiler.enable()
        result = func(*args, **kwargs)
        profiler.disable()
        
        s = io.StringIO()
        ps = pstats.Stats(profiler, stream=s).sort_stats('cumulative')
        ps.print_stats(20)  # Выводим топ-20 самых затратных операций
        print(s.getvalue())
        
        return result
    return wrapper
```

## 10. *Архитектурные паттерны*
В зависимости от типа проекта:
   - **MVC (Model-View-Controller)**: для веб-приложений.
   - **Microservices**: для распределённых систем.
   - **CLI/монолит**: для утилит или небольших приложений.
   - **Repository Pattern**: для абстрагирования доступа к данным.
   - **Factory Pattern**: для создания объектов без указания конкретного класса.
   - **Dependency Injection**: для уменьшения связанности компонентов.

### Пример реализации Repository Pattern:

```python
# src/repositories/base.py
from typing import List, Optional, TypeVar, Generic, Type, Any, Dict
from pydantic import BaseModel
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

from src.core.database import Base
from src.core.exceptions import ResourceNotFoundError

T = TypeVar('T', bound=Base)
M = TypeVar('M', bound=BaseModel)

class BaseRepository(Generic[T, M]):
    """Базовый репозиторий для работы с моделями"""
    
    def __init__(self, model: Type[T], schema: Type[M], db: Session):
        self.model = model
        self.schema = schema
        self.db = db
    
    def get_all(self) -> List[M]:
        """Получает все записи"""
        items = self.db.query(self.model).all()
        return [self.schema.from_orm(item) for item in items]
    
    def get_by_id(self, id: int) -> M:
        """Получает запись по ID"""
        item = self.db.query(self.model).filter(self.model.id == id).first()
        if not item:
            raise ResourceNotFoundError(f"{self.model.__name__}")
        return self.schema.from_orm(item)
    
    def create(self, data: Dict[str, Any]) -> M:
        """Создает новую запись"""
        item = self.model(**data)
        self.db.add(item)
        self.db.commit()
        self.db.refresh(item)
        return self.schema.from_orm(item)
```