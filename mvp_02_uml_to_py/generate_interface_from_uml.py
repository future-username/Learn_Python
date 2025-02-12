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
# def extract_compositions(text):
#     # Регулярное выражение для извлечения связей композиции
#     pattern = r'(\w+) \*\-- (\w+): composition'
#     matches = re.findall(pattern, text)
#     compositions = {}
#     for child, parent in matches:
#         compositions.setdefault(parent, []).append(child)
#     return compositions
#
# def parse_interface_methods_and_attributes(interface_content):
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
#     param_list = [param.strip() for param in params.split(',') if param.strip()]
#     param_str = ', '.join(param_list)
#     return f'def {name}(self, {param_str}):\n        pass'
#
# def generate_attribute_declaration(attribute):
#     visibility, name, attr_type = attribute
#     visibility_prefix = '' if visibility == '+' else '_'
#     return f'self.{visibility_prefix}{name} = None  # type: {attr_type}'
#
# def generate_class_code(interface_name, methods, attributes, compositions):
#     class_code = [f'class {interface_name}:\n    def __init__(self):']
#
#     # Добавляем атрибуты в конструктор
#     for attribute in attributes:
#         class_code.append(f'        {generate_attribute_declaration(attribute)}')
#
#     # Добавляем композиционные объекты
#     for comp in compositions.get(interface_name, []):
#         class_code.append(f'        self.{comp.lower()} = {comp}()')
#
#     # Добавляем методы
#     for method in methods:
#         if method[1] != '__init__':
#             class_code.append(f'    {generate_method_signature(method)}')
#
#     return '\n'.join(class_code)
#
# def generate_python_classes(interfaces, compositions):
#     class_codes = []
#     for interface_name, content in interfaces.items():
#         methods, attributes = parse_interface_methods_and_attributes(content)
#         class_codes.append(generate_class_code(interface_name, methods, attributes, compositions))
#     return '\n\n'.join(class_codes)
#
# # Пример содержимого UML-файла
# with open('uml_class_line.puml', 'r') as uml_class:
#     uml_content = uml_class.read()
#
# interfaces = extract_all_interfaces(uml_content)
# compositions = extract_compositions(uml_content)
#
# def save_python_classes_to_file(filename, class_code):
#     with open(filename, 'w') as file:
#         file.write(class_code)
#
# # Генерация Python-классов
# class_code = generate_python_classes(interfaces, compositions)
#
# # Сохранение в файл
# output_file = 'generated_classes.py'
# save_python_classes_to_file(output_file, class_code)
#
# print(f"Python-классы сгенерированы и сохранены в файл '{output_file}':\n")
# print(class_code)


# import re
#
# def extract_all_interfaces(text):
#     pattern = r'interface (\w+) \{([^}]+)\}'
#     matches = re.findall(pattern, text)
#     interfaces = {}
#     for match in matches:
#         interface_name, content = match
#         interfaces[interface_name] = content.strip()
#     return interfaces
#
# def extract_compositions(text):
#     pattern = r'(\w+) \*\-- (\w+): composition'
#     matches = re.findall(pattern, text)
#     compositions = {}
#     for child, parent in matches:
#         compositions.setdefault(parent, []).append(child)
#     return compositions
#
# def parse_interface_methods_and_attributes(interface_content):
#     method_pattern = r'([+-])(\w+)\(([^)]*)\):\s*(\w+)'
#     attribute_pattern = r'([+-])(\w+):\s*(\w+)'
#     methods = re.findall(method_pattern, interface_content)
#     attributes = re.findall(attribute_pattern, interface_content)
#     return methods, attributes
#
# def generate_method_signature(method):
#     visibility, name, params, return_type = method
#     param_list = [param.strip() for param in params.split(',') if param.strip()]
#     if param_list:
#         param_str = ', '.join(param_list)
#         method_params = f'self, {param_str}'
#     else:
#         method_params = 'self'
#     return f'def {name}({method_params}):\n        pass'
#
# def generate_attribute_declaration(attribute):
#     visibility, name, attr_type = attribute
#     # Удаляем все ведущие подчёркивания из имени атрибута
#     cleaned_name = name.lstrip('_')
#     # Добавляем одно подчёркивание для приватных атрибутов
#     python_name = f'_{cleaned_name}' if visibility == '-' else cleaned_name
#     return f'self.{python_name} = None  # type: {attr_type}'
#
# def generate_class_code(interface_name, methods, attributes, compositions):
#     class_code = [f'class {interface_name}:\n    def __init__(self):']
#     for attribute in attributes:
#         class_code.append(f'        {generate_attribute_declaration(attribute)}')
#     for comp in compositions.get(interface_name, []):
#         class_code.append(f'        self.{comp.lower()} = {comp}()')
#     for method in methods:
#         if method[1] != '__init__':
#             class_code.append(f'    {generate_method_signature(method)}')
#     return '\n'.join(class_code)
#
# def generate_python_classes(interfaces, compositions):
#     class_codes = []
#     for interface_name, content in interfaces.items():
#         methods, attributes = parse_interface_methods_and_attributes(content)
#         class_codes.append(generate_class_code(interface_name, methods, attributes, compositions))
#     return '\n\n'.join(class_codes)
#
# with open('uml_class_for_test.puml', 'r') as uml_class:
#     uml_content = uml_class.read()
#
# interfaces = extract_all_interfaces(uml_content)
# compositions = extract_compositions(uml_content)
#
# def save_python_classes_to_file(filename, class_code):
#     with open(filename, 'w', encoding='utf-8') as file:
#         file.write(class_code)
#
# class_code = generate_python_classes(interfaces, compositions)
# output_file = 'ready_class_for_test.py'
# save_python_classes_to_file(output_file, class_code)
#
# print(f"Python-классы сгенерированы и сохранены в файл '{output_file}':\n")
# print(class_code)

# import re
#
#
# def extract_all_interfaces(text):
#     pattern = r'interface\s+(\w+)\s*\{([^}]+)\}'
#     matches = re.findall(pattern, text, re.DOTALL)
#     interfaces = {}
#     for match in matches:
#         interface_name, content = match
#         interfaces[interface_name] = content.strip()
#     return interfaces
#
#
# def extract_compositions(text):
#     pattern = r'(\w+)\s+\*\--\s+(\w+):\s+composition'
#     matches = re.findall(pattern, text)
#     compositions = {}
#     for child, parent in matches:
#         compositions.setdefault(parent, []).append(child)
#     return compositions
#
#
# def parse_interface_methods_and_attributes(interface_content):
#     method_pattern = r'([+-])(\w+)\(([^)]*)\)(?:\s*:\s*(?:->\s*)?(\w+))?'
#     attribute_pattern = r'([+-])(\w+):\s*(\w+)'
#
#     # Разделяем содержимое на строки и сортируем методы и атрибуты
#     lines = interface_content.split('\n')
#     methods = []
#     attributes = []
#     for line in lines:
#         line = line.strip()
#         if not line or line.startswith('..'):
#             continue
#         method_match = re.match(method_pattern, line)
#         if method_match:
#             methods.append(method_match.groups())
#             continue
#         attribute_match = re.match(attribute_pattern, line)
#         if attribute_match:
#             attributes.append(attribute_match.groups())
#     return methods, attributes
#
#
# def generate_method_signature(method):
#     visibility, name, params, return_type = method
#     param_list = [param.strip() for param in params.split(',') if param.strip()]
#     method_params = f'self{", " + ", ".join(param_list) if param_list else ""}'
#     return_anno = f' -> {return_type}' if return_type else ''
#     return f'\tdef {name}({method_params}){return_anno}:\n\t\traise NotImplementedError()'
#
#
# def generate_class_code(interface_name, methods, attributes, compositions):
#     class_code = [f'\nclass {interface_name}:']
#     init_method = None
#     other_methods = []
#
#     # Разделяем __init__ от других методов
#     for method in methods:
#         if method[1] == '__init__':
#             init_method = method
#         else:
#             other_methods.append(method)
#
#     # Обрабатываем __init__
#     if init_method:
#         visibility, name, params, return_type = init_method
#         param_list = [param.strip() for param in params.split(',') if param.strip()]
#         method_params = 'self' + (', ' + ', '.join(param_list) if param_list else '')
#         class_code.append(f'\tdef __init__({method_params}):')
#
#         # Названия параметров для сопоставления с атрибутами
#         init_param_names = [param.split(':')[0].strip() for param in param_list]
#
#         # Присваиваем значения атрибутам из параметров
#         for param in param_list:
#             param_name = param.split(':')[0].strip()
#             # Находим соответствующий атрибут
#             matched_attr = next((attr for attr in attributes if attr[1].lstrip('_') == param_name), None)
#             if matched_attr:
#                 attr_visibility, attr_name, attr_type = matched_attr
#                 class_code.append(f'\t\tself.{attr_name} = {param_name}')
#
#         # Присваиваем None оставшимся атрибутам
#         for attr in attributes:
#             attr_visibility, attr_name, attr_type = attr
#             cleaned_name = attr_name.lstrip('_')
#             if cleaned_name not in init_param_names:
#                 class_code.append(f'\t\tself.{attr_name} = None')
#     else:
#         # Если __init__ отсутствует, создаём пустой конструктор
#         class_code.append('    def __init__(self):')
#         for attr in attributes:
#             visibility, name, attr_type = attr
#             cleaned_name = name.lstrip('_')
#             python_name = f'__{cleaned_name}' if visibility == '-' else cleaned_name
#             class_code.append(f'\t\tself.{python_name} = None')
#
#     # Обрабатываем композиции, если есть
#     for comp in compositions.get(interface_name, []):
#         class_code.append(f'\t\tself.{comp.lower()} = {comp}()')
#
#     # Добавляем остальные методы
#     for method in other_methods:
#         class_code.append('')
#         class_code.append(generate_method_signature(method))
#
#     return '\n'.join(class_code)
#
#
# def generate_python_classes(interfaces, compositions):
#     class_codes = []
#     for interface_name, content in interfaces.items():
#         methods, attributes = parse_interface_methods_and_attributes(content)
#         class_codes.append(generate_class_code(interface_name, methods, attributes, compositions))
#     return '\n\n'.join(class_codes).strip() + '\n'
#
#
# def save_python_classes_to_file(filename, class_code):
#     with open(filename, 'w', encoding='utf-8') as file:
#         file.write(class_code)
#
#
# if __name__ == "__main__":
#     input_file = 'uml_class_line.puml'
#     output_file = 'generated_classes.py'
#     with open(input_file, 'r', encoding='utf-8') as uml_class:
#         uml_content = uml_class.read()
#
#     interfaces = extract_all_interfaces(uml_content)
#     compositions = extract_compositions(uml_content)
#
#     class_code = generate_python_classes(interfaces, compositions)
#     save_python_classes_to_file(output_file, class_code)
#
#     print(f"Python-классы сгенерированы и сохранены в файл '{output_file}':\n")
#     print(class_code)


# import re
#
#
# def extract_all_interfaces(text):
#     pattern = r'interface (\w+) \{\s*?"""(.*?)"""\s*?((?:.*?\n)*?)\}'
#     matches = re.findall(pattern, text, re.DOTALL)
#     interfaces = {}
#     for match in matches:
#         interface_name, class_doc, content = match
#         interfaces[interface_name] = {
#             'doc': class_doc.strip(),
#             'content': content.strip()
#         }
#     return interfaces
#
#
# def parse_interface_content(content):
#     method_pattern = r'^([+-])(\w+)\(([^)]*)\)(?:\s*->\s*(\w+))?'
#     attribute_pattern = r'^([+-])(\w+):\s*(\w+)'
#
#     sections = {
#         'constructor': [],
#         'attributes': [],
#         'methods': []
#     }
#
#     current_section = None
#
#     for line in content.split('\n'):
#         line = line.strip()
#
#         # Обработка секций
#         if line.startswith('..'):
#             section_name = line.split('..')[1].strip().lower()
#             current_section = section_name
#             continue
#
#         if not line or line.startswith('"""'):
#             continue
#
#         # Парсинг методов
#         if current_section in ['constructor', 'methods']:
#             match = re.match(method_pattern, line)
#             if match:
#                 sections['methods' if current_section == 'methods' else 'constructor'].append(match.groups())
#
#         # Парсинг атрибутов
#         elif current_section == 'attributes':
#             match = re.match(attribute_pattern, line)
#             if match:
#                 sections['attributes'].append(match.groups())
#
#     return sections
#
#
# def generate_class_doc(docstring):
#     if docstring:
#         return f'    """{docstring}"""'
#     return ''
#
#
# def generate_method_signature(method, is_constructor=False):
#     vis, name, params, ret_type = method
#     param_list = []
#
#     for param in params.split(','):
#         param = param.strip()
#         if not param:
#             continue
#         if '=' in param:
#             p, default = map(str.strip, param.split('=', 1))
#             param = f'{p} = {default}'
#         param_list.append(param)
#
#     if is_constructor:
#         params_str = 'self' + (', ' + ', '.join(param_list) if param_list else '')
#         body = '\n'.join([f'        self.__{p.split(":")[0].strip()} = {p.split(":")[0].strip()}'
#                           for p in param_list])
#         return f'    def {name}({params_str}):\n{body}'
#     else:
#         params_str = 'self' + (', ' + ', '.join(param_list) if param_list else '')
#         return_type = f' -> {ret_type}' if ret_type else ''
#         return f'    def {name}({params_str}){return_type}:\n        raise NotImplementedError()'
#
#
# def generate_class_code(interface_name, interface_data):
#     class_code = [f'class {interface_name}:']
#
#     # Добавляем docstring класса
#     if interface_data['doc']:
#         class_code.append(generate_class_doc(interface_data['doc']))
#
#     sections = parse_interface_content(interface_data['content'])
#
#     # Генерация конструктора
#     if sections['constructor']:
#         constructor = sections['constructor'][0]
#         class_code.append(generate_method_signature(constructor, is_constructor=True))
#
#     # Генерация методов
#     for method in sections['methods']:
#         class_code.append('\n' + generate_method_signature(method))
#
#     return '\n'.join(class_code)
#
#
# def generate_python_classes(interfaces):
#     return '\n\n'.join(
#         generate_class_code(name, data) for name, data in interfaces.items()
#     )
#
#
# def save_python_classes_to_file(filename, class_code):
#     with open(filename, 'w', encoding='utf-8') as file:
#         file.write(class_code)
#
#
# if __name__ == "__main__":
#     with open('uml_class_line.puml', 'r', encoding='utf-8') as f:
#         uml_content = f.read()
#
#     interfaces = extract_all_interfaces(uml_content)
#     generated_code = generate_python_classes(interfaces)
#     save_python_classes_to_file('generated_classes.py', generated_code)
#     print(generated_code)


import re


def extract_all_interfaces(text):
    pattern = r'interface (\w+)\s*\{([^}]+)\}'
    matches = re.findall(pattern, text, re.DOTALL)
    interfaces = {}
    for name, content in matches:
        interfaces[name] = content.strip()
    return interfaces


def parse_interface_content(content):
    method_pattern = r'^\s*([+-])(\w+)\(([^)]*)\)(?:\s*->\s*(\w+))?'
    attribute_pattern = r'^\s*([+-])(\w+):\s*(\w+)'
    doc_pattern = r'^\s*"""(.+)"""'

    sections = {
        'doc': None,
        'constructor': [],
        'attributes': [],
        'methods': []
    }

    for line in content.split('\n'):
        line = line.strip()
        if not line:
            continue

        # Парсинг docstring
        if doc_match := re.match(doc_pattern, line):
            sections['doc'] = doc_match.group(1).strip()
            continue

        # Игнорируем секционные комментарии
        if line.startswith('..'):
            continue

        # Парсинг методов
        if method_match := re.match(method_pattern, line):
            sections['methods' if method_match.group(2) != '__init__' else 'constructor'].append(method_match.groups())

        # Парсинг атрибутов
        elif attr_match := re.match(attribute_pattern, line):
            sections['attributes'].append(attr_match.groups())

    return sections


def generate_class_code(interface_name, content):
    sections = parse_interface_content(content)
    code = [f'class {interface_name}:']

    # Добавляем docstring класса
    if sections['doc']:
        code.append(f'    """{sections["doc"]}"""')

    # Генерация конструктора
    if sections['constructor']:
        _, name, params, _ = sections['constructor'][0]
        param_list = [p.strip() for p in params.split(',') if p.strip()]
        params_str = 'self' + (', ' + ', '.join(param_list) if param_list else '')
        code.append(f'    def {name}({params_str}):')
        for param in param_list:
            var_name = param.split(':')[0].strip()
            code.append(f'        self.__{var_name} = {var_name}')

    # Генерация методов
    for method in sections['methods']:
        vis, name, params, ret_type = method
        param_list = []
        for param in params.split(','):
            param = param.strip()
            if '=' in param:
                p, default = map(str.strip, param.split('=', 1))
                param = f'{p} = {default}'
            param_list.append(param)

        params_str = 'self' + (', ' + ', '.join(param_list) if param_list else '')
        return_type = f' -> {ret_type}' if ret_type else ''
        code.append(f'\n    def {name}({params_str}){return_type}:\n        raise NotImplementedError()')

    return '\n'.join(code)


def generate_python_classes(interfaces):
    return '\n\n'.join(
        generate_class_code(name, content)
        for name, content in interfaces.items()
    )


def save_python_classes_to_file(filename, class_code):
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(class_code)


if __name__ == "__main__":
    with open('uml_class_line.puml', 'r', encoding='utf-8') as f:
        uml_content = f.read()

    interfaces = extract_all_interfaces(uml_content)
    generated_code = generate_python_classes(interfaces)
    save_python_classes_to_file('generated_classes.py', generated_code)
    print(generated_code)