# import re
#
# def extract_all_interfaces(text):
#     # Регулярное выражение для извлечения всех интерфейсов
#     pattern = r'interface \w+ \{[^}]+\}'
#     matches = re.findall(pattern, text)
#     return matches
#
# # Пример содержимого файла
#
# # Извлечение всех интерфейсов
# with open('uml_class_line.puml', '+r') as uml_class:
#     interfaces = extract_all_interfaces(uml_class.read())
#
# # Вывод всех найденных интерфейсов
# print("Найденные интерфейсы:")
# for interface in interfaces:
#     print(interface)


# import re
#
# def extract_all_interfaces(text):
#     # Регулярное выражение для извлечения всех интерфейсов
#     pattern = r'interface (\w+) \{([^}]+)\}'
#     matches = re.findall(pattern, text)
#     interfaces = {}
#     for match in matches:
#         interface_name, content = match
#         interfaces[interface_name] = content.strip()
#     return interfaces
#
# def parse_interface_methods(interface_content):
#     # Регулярное выражение для извлечения методов и атрибутов
#     method_pattern = r'([+-])(\w+)\(([^)]*)\):\s*(\w+)'
#     attribute_pattern = r'([+-])(\w+):\s*(\w+)'
#
#     methods = re.findall(method_pattern, interface_content)
#     attributes = re.findall(attribute_pattern, interface_content)
#
#     return methods, attributes
#
# def generate_method_signature(method):
#     visibility, name, params, return_type = method
#     param_list = params.replace(':', '').split(',')
#     param_names = [param.strip().split(' ')[0] for param in param_list]
#     param_str = ', '.join(param_names) if param_names[0] else ''
#     return f'def {name}(self, {param_str}):\n        return'
#
# def generate_class_code(interface_name, methods):
#     class_code = [f'class {interface_name}:\n    def __init__(self):\n        pass\n']
#     for method in methods:
#         if method[1] != '__init__':
#             class_code.append(f'    {generate_method_signature(method)}\n')
#     return '\n'.join(class_code)
#
# def generate_python_classes(interfaces):
#     class_codes = []
#     for interface_name, content in interfaces.items():
#         methods, _ = parse_interface_methods(content)
#         class_codes.append(generate_class_code(interface_name, methods))
#     return '\n\n'.join(class_codes)
#
# # Пример содержимого UML-файла
# with open('uml_class_line.puml', '+r') as uml_class:
#     interfaces = extract_all_interfaces(uml_class.read())
#
# def save_python_classes_to_file(filename, class_code):
#     with open(filename, 'w') as file:
#         file.write(class_code)
#
# # Генерация Python-классов
# class_code = generate_python_classes(interfaces)
#
# # Сохранение в файл
# output_file = 'generated_classes.py'
# save_python_classes_to_file(output_file, class_code)
#
# print(f"Python-классы сгенерированы и сохранены в файл '{output_file}':\n")
# print(class_code)

import re

def extract_all_interfaces(text):
    # Регулярное выражение для извлечения всех интерфейсов
    pattern = r'interface (\w+) \{([^}]+)\}'
    matches = re.findall(pattern, text)
    interfaces = {}
    for match in matches:
        interface_name, content = match
        interfaces[interface_name] = content.strip()
    return interfaces

def extract_compositions(text):
    # Регулярное выражение для извлечения связей композиции
    pattern = r'(\w+) \*\-- (\w+): composition'
    matches = re.findall(pattern, text)
    compositions = {}
    for child, parent in matches:
        compositions.setdefault(parent, []).append(child)
    return compositions

def parse_interface_methods_and_attributes(interface_content):
    # Регулярное выражение для извлечения методов и атрибутов
    method_pattern = r'([+-])(\w+)\(([^)]*)\):\s*(\w+)'
    attribute_pattern = r'([+-])(\w+):\s*(\w+)'

    methods = re.findall(method_pattern, interface_content)
    attributes = re.findall(attribute_pattern, interface_content)

    return methods, attributes

def generate_method_signature(method):
    visibility, name, params, return_type = method
    param_list = [param.strip() for param in params.split(',') if param.strip()]
    param_str = ', '.join(param_list)
    return f'def {name}(self, {param_str}):\n        pass'

def generate_attribute_declaration(attribute):
    visibility, name, attr_type = attribute
    visibility_prefix = '' if visibility == '+' else '_'
    return f'self.{visibility_prefix}{name} = None  # type: {attr_type}'

def generate_class_code(interface_name, methods, attributes, compositions):
    class_code = [f'class {interface_name}:\n    def __init__(self):']

    # Добавляем атрибуты в конструктор
    for attribute in attributes:
        class_code.append(f'        {generate_attribute_declaration(attribute)}')

    # Добавляем композиционные объекты
    for comp in compositions.get(interface_name, []):
        class_code.append(f'        self.{comp.lower()} = {comp}()')

    # Добавляем методы
    for method in methods:
        if method[1] != '__init__':
            class_code.append(f'    {generate_method_signature(method)}')

    return '\n'.join(class_code)

def generate_python_classes(interfaces, compositions):
    class_codes = []
    for interface_name, content in interfaces.items():
        methods, attributes = parse_interface_methods_and_attributes(content)
        class_codes.append(generate_class_code(interface_name, methods, attributes, compositions))
    return '\n\n'.join(class_codes)

# Пример содержимого UML-файла
with open('uml_class_line.puml', 'r') as uml_class:
    uml_content = uml_class.read()

interfaces = extract_all_interfaces(uml_content)
compositions = extract_compositions(uml_content)

def save_python_classes_to_file(filename, class_code):
    with open(filename, 'w') as file:
        file.write(class_code)

# Генерация Python-классов
class_code = generate_python_classes(interfaces, compositions)

# Сохранение в файл
output_file = 'generated_classes.py'
save_python_classes_to_file(output_file, class_code)

print(f"Python-классы сгенерированы и сохранены в файл '{output_file}':\n")
print(class_code)