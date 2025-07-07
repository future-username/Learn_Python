"""
Скрипт для сравнения классов, методов и полей между диаграммой классов (mermaid) и реальным кодом Python.
"""
import re
import ast
from pathlib import Path
from typing import Dict, List, Set

MERMAID_PATH = Path(__file__).parent / "app_rainbow_mvc_class_diagram.md"
CODE_PATH = Path(__file__).parent / "app_rainbow_mvc.py"

# --- Парсер диаграммы классов (mermaid) ---
def parse_mermaid_classes(mermaid_text: str) -> Dict[str, Dict]:
    classes = {}
    class_pattern = re.compile(r'class (\w+) \{([\s\S]*?)\}', re.MULTILINE)
    for class_match in class_pattern.finditer(mermaid_text):
        class_name = class_match.group(1)
        body = class_match.group(2)
        fields = set()
        methods = set()
        privates = set()
        for line in body.splitlines():
            line = line.strip()
            if not line or line.startswith('<<'):
                continue
            m = re.match(r'([+-])?([\w_]+)[\s:]*([\w, ()]*)', line)
            if not m:
                continue
            prefix, name, _ = m.groups()
            if '(' in line:
                methods.add(name)
            else:
                fields.add(name)
            if prefix == '-':
                privates.add(name)
        classes[class_name] = {
            'fields': fields,
            'methods': methods,
            'privates': privates,
        }
    return classes

# --- Парсер Python-кода ---
def parse_python_classes(code: str) -> Dict[str, Dict]:
    tree = ast.parse(code)
    classes = {}
    for node in tree.body:
        if not isinstance(node, ast.ClassDef):
            continue
        class_name = node.name
        fields = set()
        methods = set()
        privates = set()
        for item in node.body:
            if isinstance(item, ast.FunctionDef):
                methods.add(item.name)
                if item.name.startswith('_') and not item.name.startswith('__'):
                    privates.add(item.name)
                continue
            if isinstance(item, ast.Assign):
                for target in item.targets:
                    if not isinstance(target, ast.Name):
                        continue
                    fields.add(target.id)
                    if target.id.startswith('_') and not target.id.startswith('__'):
                        privates.add(target.id)
                continue
            if isinstance(item, ast.AnnAssign):
                if not isinstance(item.target, ast.Name):
                    continue
                fields.add(item.target.id)
                if item.target.id.startswith('_') and not item.target.id.startswith('__'):
                    privates.add(item.target.id)
        classes[class_name] = {
            'fields': fields,
            'methods': methods,
            'privates': privates,
        }
    return classes

# --- Сравнение ---
def compare_classes(diagram: Dict, code: Dict) -> List[str]:
    report = []
    all_class_names = set(diagram) | set(code)
    for cname in all_class_names:
        d = diagram.get(cname)
        c = code.get(cname)
        if not d:
            report.append(f"Class '{cname}' present in code but missing in diagram.")
            continue
        if not c:
            report.append(f"Class '{cname}' present in diagram but missing in code.")
            continue
        missing_fields = d['fields'] - c['fields']
        extra_fields = c['fields'] - d['fields']
        if missing_fields:
            report.append(f"Class '{cname}': fields missing in code: {missing_fields}")
        if extra_fields:
            report.append(f"Class '{cname}': extra fields in code: {extra_fields}")
        missing_methods = d['methods'] - c['methods']
        extra_methods = c['methods'] - d['methods']
        if missing_methods:
            report.append(f"Class '{cname}': methods missing in code: {missing_methods}")
        if extra_methods:
            report.append(f"Class '{cname}': extra methods in code: {extra_methods}")
        missing_privates = d['privates'] - c['privates']
        extra_privates = c['privates'] - d['privates']
        if missing_privates:
            report.append(f"Class '{cname}': privates missing in code: {missing_privates}")
        if extra_privates:
            report.append(f"Class '{cname}': extra privates in code: {extra_privates}")
    return report


def main():
    mermaid_text = MERMAID_PATH.read_text(encoding='utf-8')
    # Найти все блоки, начинающиеся с classDiagram и заканчивающиеся ```
    class_diagram_blocks = re.findall(r'([\s\S]+?)```', mermaid_text)
    if not class_diagram_blocks:
        return
    diagram_classes = {}
    for block in class_diagram_blocks:
        parsed = parse_mermaid_classes(block)
        diagram_classes.update(parsed)
    code_text = CODE_PATH.read_text(encoding='utf-8')
    code_classes = parse_python_classes(code_text)
    report = compare_classes(diagram_classes, code_classes)
    if not report:
        print("Все классы, методы и поля совпадают!")
        return
    print("Результаты сравнения:")
    for line in report:
        print(line)

if __name__ == "__main__":
    main() 