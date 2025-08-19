# import pytest


def read_md_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Файл не найден: {file_path}")
        return None
    except Exception as e:
        print(f"Ошибка при чтении файла {file_path}: {e}")
        return None

# print(read_md_file(r'app\app_rainbow_1,5\uml\app_rainbow_mvc_class_diagram.md'))
print(read_md_file(r'app\app_rainbow_1,5\uml\app_rainbow_sequence.md'))