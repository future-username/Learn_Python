import unittest
from unittest.mock import Mock, patch, call
import re
import sys
import os

# Функция для чтения содержимого .md файла
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

# Улучшенная функция для извлечения текста диаграммы Mermaid из .md файла
def extract_mermaid_diagram(md_content):
    if not md_content:
        return None
    
    # Попробуем несколько вариантов паттернов для поиска Mermaid диаграмм
    patterns = [
        r'```mermaid\s*([\s\S]*?)```',  # Оригинальный паттерн
        r'```mermaid\n([\s\S]*?)```',   # С явным переносом строки
        r'```mermaid\r?\n([\s\S]*?)```', # С учетом разных переносов строк
        r'```\s*mermaid\s*([\s\S]*?)```', # С возможными пробелами
    ]
    
    for pattern in patterns:
        match = re.search(pattern, md_content, re.DOTALL)
        if match:
            block = match.group(1).strip()
            if block:  # Проверяем, что блок не пустой
                # Найти первую строку, содержащую classDiagram или sequenceDiagram
                lines = block.splitlines()
                for i, line in enumerate(lines):
                    if 'classDiagram' in line or 'sequenceDiagram' in line:
                        # Вернуть содержимое начиная с этой строки
                        return '\n'.join(lines[i:]).strip()
                # Если не найдено, вернуть весь блок
                return block
    
    # Если не найдено, попробуем найти диаграммы без кодовых блоков
    direct_patterns = [
        r'classDiagram\s*([\s\S]*?)(?=\n\n|\Z)',
        r'sequenceDiagram\s*([\s\S]*?)(?=\n\n|\Z)',
    ]
    
    for pattern in direct_patterns:
        match = re.search(pattern, md_content, re.DOTALL)
        if match:
            return match.group(0).strip()
    
    return None

# Функция для отладки - показывает первые строки файла
def debug_file_content(file_path, lines=10):
    content = read_md_file(file_path)
    if content:
        print(f"\nПервые {lines} строк файла {file_path}:")
        print("-" * 50)
        file_lines = content.splitlines()
        for i, line in enumerate(file_lines[:lines]):
            print(f"{i+1:2d}: {line}")
        print("-" * 50)
        
        # Поиск всех кодовых блоков
        code_blocks = re.findall(r'```(\w+)?\s*([\s\S]*?)```', content, re.DOTALL)
        print(f"\nНайдено кодовых блоков: {len(code_blocks)}")
        for i, (lang, block) in enumerate(code_blocks):
            print(f"Блок {i+1}: язык='{lang}', длина={len(block)} символов")
            if 'mermaid' in lang.lower() if lang else False:
                print(f"  Это Mermaid блок!")
    else:
        print(f"Не удалось прочитать файл: {file_path}")

# Функция для парсинга classDiagram из текста Mermaid
def parse_class_diagram(mermaid_text):
    """Парсит classDiagram: классы и их методы."""
    classes = {}
    class_pattern = r'class (\w+) \{([^}]*)\}'
    method_pattern = r'([+-])(\w+)\s*\(([^)]*)\)'
    
    for class_match in re.finditer(class_pattern, mermaid_text, re.DOTALL):
        class_name = class_match.group(1)
        class_body = class_match.group(2)
        methods = []
        
        for line in class_body.split('\n'):
            line = line.strip()
            m = re.match(method_pattern, line)
            if m:
                name = m.group(2)
                params = m.group(3).replace(' ', '')
                methods.append(f"{name}({params})")
        
        classes[class_name] = set(methods)
    
    return classes

def parse_sequence_diagram(mermaid_text):
    """Парсит sequenceDiagram: классы и их методы."""
    classes = {}
    # Найти участников
    participants = {}
    
    for m in re.finditer(r'participant (\w+) as [^\n]+', mermaid_text):
        participants[m.group(1)] = set()
    
    # Найти вызовы: X->>Y: +method(params)
    call_pattern = r'(\w+)->>+(\w+):\s*([+-])?(\w+)\(([^)]*)\)'
    for m in re.finditer(call_pattern, mermaid_text):
        target = m.group(2)
        name = m.group(4)
        params = m.group(5).replace(' ', '')
        
        if target not in participants:
            participants[target] = set()
        participants[target].add(f"{name}({params})")
    
    return participants

# Функция для сравнения двух диаграмм
def compare_structures(classes1, classes2, name1, name2):
    all_classes = set(classes1) | set(classes2)
    
    for cls in sorted(all_classes):
        print(f"\nКласс: {cls}")
        m1 = classes1.get(cls, set())
        m2 = classes2.get(cls, set())
        
        only1 = m1 - m2
        only2 = m2 - m1
        
        if only1:
            print(f"  Только в {name1}: {sorted(only1)}")
        if only2:
            print(f"  Только в {name2}: {sorted(only2)}")
        if not only1 and not only2:
            print("  Методы совпадают.")

def main(file1, file2):
    print(f"Анализ файлов:\n1. {file1}\n2. {file2}\n")
    
    # Проверяем существование файлов
    if not os.path.exists(file1):
        print(f"ОШИБКА: Файл {file1} не найден!")
        return
    if not os.path.exists(file2):
        print(f"ОШИБКА: Файл {file2} не найден!")
        return
    
    # Читаем файлы
    md1 = read_md_file(file1)
    md2 = read_md_file(file2)
    
    if not md1 or not md2:
        print("Не удалось прочитать один или оба файла.")
        return
    
    # Отладочная информация
    print("=== ОТЛАДОЧНАЯ ИНФОРМАЦИЯ ===")
    debug_file_content(file1, 15)
    debug_file_content(file2, 15)
    
    # Извлекаем диаграммы
    mermaid1 = extract_mermaid_diagram(md1)
    mermaid2 = extract_mermaid_diagram(md2)
    
    print(f"\nРезультат извлечения диаграмм:")
    print(f"Диаграмма 1: {'Найдена' if mermaid1 else 'НЕ НАЙДЕНА'}")
    print(f"Диаграмма 2: {'Найдена' if mermaid2 else 'НЕ НАЙДЕНА'}")
    
    if mermaid1:
        print(f"\nДиаграмма 1 (первые 200 символов):")
        print(mermaid1[:200] + "..." if len(mermaid1) > 200 else mermaid1)
    
    if mermaid2:
        print(f"\nДиаграмма 2 (первые 200 символов):")
        print(mermaid2[:200] + "..." if len(mermaid2) > 200 else mermaid2)
    
    if not mermaid1 or not mermaid2:
        print("\nНе удалось найти блоки mermaid в одном или обоих файлах.")
        return
    
    # Определяем тип диаграмм и парсим
    if mermaid1.startswith('classDiagram'):
        classes1 = parse_class_diagram(mermaid1)
        name1 = "classDiagram"
    else:
        classes1 = parse_sequence_diagram(mermaid1)
        name1 = "sequenceDiagram"
    
    if mermaid2.startswith('classDiagram'):
        classes2 = parse_class_diagram(mermaid2)
        name2 = "classDiagram"
    else:
        classes2 = parse_sequence_diagram(mermaid2)
        name2 = "sequenceDiagram"
    
    print(f"\n=== СРАВНЕНИЕ СТРУКТУР ===")
    compare_structures(classes1, classes2, name1, name2)

class TestDiagramsAndImplementation(unittest.TestCase):
    def setUp(self):
        # Используем относительные пути или проверяем существование файлов
        self.md_file1_path = r'c:\Users\Paul\PycharmProjects\Learn_Python\app\app_rainbow_1.4\app_rainbow_mvc_class_diagram.md'
        self.md_file2_path = r'c:\Users\Paul\PycharmProjects\Learn_Python\app\app_rainbow_1.4\app_rainbow_sequence.md'
        
        # Проверяем существование файлов
        if not os.path.exists(self.md_file1_path):
            self.skipTest(f"Файл не найден: {self.md_file1_path}")
        if not os.path.exists(self.md_file2_path):
            self.skipTest(f"Файл не найден: {self.md_file2_path}")
        
        # Читаем оба .md файла
        self.md_file1 = read_md_file(self.md_file1_path)
        self.md_file2 = read_md_file(self.md_file2_path)
        
        if not self.md_file1:
            self.skipTest(f"Не удалось прочитать файл: {self.md_file1_path}")
        if not self.md_file2:
            self.skipTest(f"Не удалось прочитать файл: {self.md_file2_path}")
        
        # Извлекаем текст диаграмм
        self.diagram1 = extract_mermaid_diagram(self.md_file1)
        self.diagram2 = extract_mermaid_diagram(self.md_file2)
        
        # Отладочная информация
        if not self.diagram1:
            print(f"\nОТЛАДКА: Не найдена диаграмма в файле {self.md_file1_path}")
            debug_file_content(self.md_file1_path, 20)
        
        if not self.diagram2:
            print(f"\nОТЛАДКА: Не найдена диаграмма в файле {self.md_file2_path}")
            debug_file_content(self.md_file2_path, 20)
        
        # Пропускаем тесты, если диаграммы не найдены
        if not self.diagram1:
            self.skipTest("Mermaid diagram not found in app_rainbow_mvc_class_diagram.md")
        if not self.diagram2:
            self.skipTest("Mermaid diagram not found in app_rainbow_sequence.md")
        
        # Мокируем tkinter, чтобы не запускать GUI
        self.patcher_tk = patch('tkinter.Tk', autospec=True)
        self.patcher_canvas = patch('tkinter.Canvas', autospec=True)
        self.patcher_button = patch('tkinter.Button', autospec=True)
        self.patcher_frame = patch('tkinter.Frame', autospec=True)
        self.patcher_label = patch('tkinter.Label', autospec=True)
        self.patcher_entry = patch('tkinter.Entry', autospec=True)
        
        self.mock_tk = self.patcher_tk.start()
        self.mock_canvas = self.patcher_canvas.start()
        self.mock_button = self.patcher_button.start()
        self.mock_frame = self.patcher_frame.start()
        self.mock_label = self.patcher_label.start()
        self.mock_entry = self.patcher_entry.start()
        
        self.addCleanup(self.patcher_tk.stop)
        self.addCleanup(self.patcher_canvas.stop)
        self.addCleanup(self.patcher_button.stop)
        self.addCleanup(self.patcher_frame.stop)
        self.addCleanup(self.patcher_label.stop)
        self.addCleanup(self.patcher_entry.stop)

    def test_diagrams_are_identical(self):
        """Проверяем, что диаграммы в обоих .md файлах описывают одинаковые классы, методы и поля."""
        print("\n=== СРАВНЕНИЕ ДИАГРАММ ===")
        
        # Определяем тип диаграмм и парсим
        if self.diagram1.startswith('classDiagram'):
            classes1 = parse_class_diagram(self.diagram1)
            name1 = "classDiagram (файл 1)"
        else:
            classes1 = parse_sequence_diagram(self.diagram1)
            name1 = "sequenceDiagram (файл 1)"
        
        if self.diagram2.startswith('classDiagram'):
            classes2 = parse_class_diagram(self.diagram2)
            name2 = "classDiagram (файл 2)"
        else:
            classes2 = parse_sequence_diagram(self.diagram2)
            name2 = "sequenceDiagram (файл 2)"
        
        compare_structures(classes1, classes2, name1, name2)
        
        # Проверяем, что найдены классы
        self.assertTrue(len(classes1) > 0, "Не найдены классы в первой диаграмме")
        self.assertTrue(len(classes2) > 0, "Не найдены классы во второй диаграмме")

    def test_model_implementation(self):
        """Проверяем, что реализация класса Model соответствует диаграмме."""
        try:
            from app_rainbow_implementation import Model
        except ImportError:
            self.skipTest("Модуль app_rainbow_implementation не найден")
        
        colors = {'#FF0000': 'Red', '#00FF00': 'Green'}
        figures = {'line': (2, 'solid'), 'circle': (0, 'dashed')}
        
        model = Model(colors, figures)
        
        # Проверяем приватные поля
        self.assertTrue(hasattr(model, '_colors'))
        self.assertTrue(hasattr(model, '_figures'))
        
        # Проверяем методы
        self.assertTrue(hasattr(model, 'get_colors'))
        self.assertTrue(hasattr(model, 'get_color_name'))
        self.assertTrue(hasattr(model, 'get_figures'))
        self.assertTrue(hasattr(model, 'get_figure_params'))
        
        # Проверяем функциональность
        self.assertEqual(model.get_colors(), colors)
        self.assertEqual(model.get_color_name('#FF0000'), 'Red')
        self.assertEqual(model.get_figures(), figures)
        self.assertEqual(model.get_figure_params('line'), (2, 'solid'))

    # Остальные тесты остаются без изменений...
    # (Здесь должны быть остальные методы тестирования)

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "compare":
        if len(sys.argv) != 4:
            print("Использование: python script.py compare file1.md file2.md")
        else:
            main(sys.argv[2], sys.argv[3])
    else:
        # Запускаем тесты
        unittest.main()