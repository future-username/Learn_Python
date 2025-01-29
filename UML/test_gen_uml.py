import random

# Списки для генерации
class_names = ["DataProcessor", "NetworkManager", "CryptEngine",
               "StorageProxy", "ApiValidator", "CacheController"]

attributes = ["config", "logger", "buffer", "cache",
              "session_token", "metadata", "threshold"]

method_names = ["initialize", "validate", "encrypt", "serialize",
                "refresh", "audit", "normalize", "sanitize"]

descriptions = [
    "Инициализирует внутренние компоненты",
    "Проверяет целостность данных",
    "Шифрует конфиденциальные данные",
    "Преобразует в бинарный формат",
    "Обновляет внутренний кэш",
    "Выполняет проверку безопасности",
    "Приводит данные к единому формату",
    "Очищает входные данные"
]

parameters = [
    "(key: str)",
    "(data: bytes)",
    "(threshold: int)",
    "(enable_logging: bool)",
    ""
]

types = ['str', 'int', 'bool', 'list']


# Генератор случайных классов
def generate_random_class():
    class_def = []

    # Выбор имени класса
    class_def.append(f"class {random.choice(class_names)} {{")

    # Случайные свойства (33% вероятность)
    if random.random() < 0.33:
        class_def.append("    .. Property ..")
        for _ in range(random.randint(1, 2)):
            class_def.append(f"    {random.choice(attributes)}: {random.choice(types)}")

    # Конструктор (50% вероятность)
    if random.random() < 0.5:
        class_def.extend([
            "    .. Constructor ..",
            f"    +__init__{random.choice(parameters)}:"
        ])

        # Атрибуты
        class_def.append("    .. Attributes ..")
        for _ in range(random.randint(0, 3)):
            class_def.append(f"    - {random.choice(attributes)}: {random.choice(types)}")

    if random.random() < 0.67:
        # Методы
        class_def.append("    .. Methods ..")
        for _ in range(random.randint(1, 4)):
            method = f"    + {random.choice(method_names)}{random.choice(parameters)}: {random.choice(types)}"
            class_def.append(method)
            class_def.append(f"    \"{random.choice(descriptions)}\"")

        class_def.append("}\n")
        return "\n".join(class_def)


# Генерация диаграммы
print("@startuml")
for _ in range(3):  # Количество классов
    print(generate_random_class())
print("@enduml")
