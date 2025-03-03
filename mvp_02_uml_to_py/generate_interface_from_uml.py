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


# import re
#
#
# def extract_all_interfaces(text):
#     pattern = r'interface (\w+)\s*\{([^}]+)\}'
#     matches = re.findall(pattern, text, re.DOTALL)
#     interfaces = {}
#     for name, content in matches:
#         interfaces[name] = content.strip()
#     return interfaces
#
#
# def parse_interface_content(content):
#     method_pattern = r'^\s*([+-])(\w+)\(([^)]*)\)(?:\s*->\s*(\w+))?'
#     attribute_pattern = r'^\s*([+-])(\w+):\s*(\w+)'
#     doc_pattern = r'^\s*"""(.+)"""'
#
#     sections = {
#         'doc': None,
#         'constructor': [],
#         'attributes': [],
#         'methods': []
#     }
#
#     for line in content.split('\n'):
#         line = line.strip()
#         if not line:
#             continue
#
#         # Парсинг docstring
#         if doc_match := re.match(doc_pattern, line):
#             sections['doc'] = doc_match.group(1).strip()
#             continue
#
#         # Игнорируем секционные комментарии
#         if line.startswith('..'):
#             continue
#
#         # Парсинг методов
#         if method_match := re.match(method_pattern, line):
#             sections['methods' if method_match.group(2) != '__init__' else 'constructor'].append(method_match.groups())
#
#         # Парсинг атрибутов
#         elif attr_match := re.match(attribute_pattern, line):
#             sections['attributes'].append(attr_match.groups())
#
#     return sections
#
#
# def generate_class_code(interface_name, content):
#     sections = parse_interface_content(content)
#     code = [f'class {interface_name}:']
#
#     # Добавляем docstring класса
#     if sections['doc']:
#         code.append(f'    """{sections["doc"]}"""')
#
#     # Генерация конструктора
#     if sections['constructor']:
#         _, name, params, _ = sections['constructor'][0]
#         param_list = [p.strip() for p in params.split(',') if p.strip()]
#         params_str = 'self' + (', ' + ', '.join(param_list) if param_list else '')
#         code.append(f'    def {name}({params_str}):')
#         for param in param_list:
#             var_name = param.split(':')[0].strip()
#             code.append(f'        self.__{var_name} = {var_name}')
#
#     # Генерация методов
#     for method in sections['methods']:
#         vis, name, params, ret_type = method
#         param_list = []
#         for param in params.split(','):
#             param = param.strip()
#             if '=' in param:
#                 p, default = map(str.strip, param.split('=', 1))
#                 param = f'{p} = {default}'
#             param_list.append(param)
#
#         params_str = 'self' + (', ' + ', '.join(param_list) if param_list else '')
#         return_type = f' -> {ret_type}' if ret_type else ''
#         code.append(f'\n    def {name}({params_str}){return_type}:\n        raise NotImplementedError()')
#
#     return '\n'.join(code)
#
#
# def generate_python_classes(interfaces):
#     return '\n\n'.join(
#         generate_class_code(name, content)
#         for name, content in interfaces.items()
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


# import re
#
# def extract_all_interfaces(text):
#     pattern = r'interface (\w+)\s*\{([^}]+)\}'
#     matches = re.findall(pattern, text, re.DOTALL)
#     interfaces = {}
#     for name, content in matches:
#         interfaces[name] = content.strip()
#     return interfaces
#
# def parse_interface_content(content):
#     method_pattern = r'^\s*([+-])(\w+)\(([^)]*)\)(?:\s*->\s*(\w+))?'
#     attribute_pattern = r'^\s*([+-])(\w+):\s*(\w+)'
#     doc_pattern = r'"""(.*?)"""'
#
#     sections = {
#         'doc': None,
#         'constructor': [],
#         'attributes': [],
#         'methods': []
#     }
#
#     lines = content.split('\n')
#     i = 0
#     while i < len(lines):
#         line = lines[i].strip()
#         if not line:
#             i += 1
#             continue
#
#         # Парсинг docstring
#         if '"""' in line:
#             doc_match = re.search(doc_pattern, '\n'.join(lines[i:i+3]), re.DOTALL)
#             if doc_match:
#                 sections['doc'] = doc_match.group(1).strip()
#                 i += 2  # Пропускаем строки docstring
#             i += 1
#             continue
#
#         # Игнорируем секционные комментарии
#         if line.startswith('..'):
#             i += 1
#             continue
#
#         # Парсинг методов
#         if method_match := re.match(method_pattern, line):
#             sections['methods' if method_match.group(2) != '__init__' else 'constructor'].append(method_match.groups())
#
#         # Парсинг атрибутов
#         elif attr_match := re.match(attribute_pattern, line):
#             sections['attributes'].append(attr_match.groups())
#
#         i += 1
#
#     return sections
#
# def generate_class_code(interface_name, content):
#     sections = parse_interface_content(content)
#     code_lines = [f'class {interface_name}:']
#
#     # Добавляем docstring класса
#     if sections['doc']:
#         code_lines.append(f'    """\n\t{sections["doc"]}\n\t"""\n')
#
#     # Генерация конструктора
#     if sections['constructor']:
#         _, name, params, _ = sections['constructor'][0]
#         param_list = [p.strip() for p in params.split(',') if p.strip()]
#         params_str = 'self' + (', ' + ', '.join(param_list) if param_list else '')
#         code_lines.append(f'    def {name}({params_str}):')
#         for param in param_list:
#             var_name = param.split(':')[0].strip()
#             code_lines.append(f'        self.__{var_name} = {var_name}')
#
#     # Генерация методов
#     for method in sections['methods']:
#         vis, name, params, ret_type = method
#         param_list = []
#         for param in params.split(','):
#             param = param.strip()
#             if param:  # Только если параметр не пустой
#                 if '=' in param:
#                     p, default = map(str.strip, param.split('=', 1))
#                     param = f'{p} = {default}'
#                 param_list.append(param)
#
#         # Формируем строку параметров
#         params_str = 'self'
#         if param_list:
#             params_str += ', ' + ', '.join(param_list)
#
#         return_type = f' -> {ret_type}' if ret_type else ''
#         code_lines.append(f'\n    def {name}({params_str}){return_type}:')
#         code_lines.append('        raise NotImplementedError()')
#
#     return '\n'.join(code_lines)
#
# def generate_python_classes(interfaces):
#     return '\n\n'.join(
#         generate_class_code(name, content)
#         for name, content in interfaces.items()
#     )
#
# def save_python_classes_to_file(filename, class_code):
#     with open(filename, 'w', encoding='utf-8') as file:
#         file.write(class_code)
#
# if __name__ == "__main__":
#     with open('uml_class_line.puml', 'r', encoding='utf-8') as f:
#         uml_content = f.read()
#
#     interfaces = extract_all_interfaces(uml_content)
#     generated_code = generate_python_classes(interfaces)
#     save_python_classes_to_file('generated_classes.py', generated_code)
#     print(generated_code)


# import re
# from typing import Dict, List, Optional, Tuple
#
# from dataclasses import dataclass
#
#
# @dataclass
# class Method:
#     visibility: str
#     name: str
#     params: List[Tuple[str, Optional[str], Optional[str]]]
#     return_type: Optional[str]
#
#
# @dataclass
# class Attribute:
#     visibility: str
#     name: str
#     type: Optional[str]
#
#
# @dataclass
# class Interface:
#     name: str
#     doc: Optional[str]
#     constructor: Optional[Method]
#     attributes: List[Attribute]
#     methods: List[Method]
#
#
# def extract_all_interfaces(text: str) -> Dict[str, str]:
#     """
#     Извлекает все интерфейсы из текста UML-диаграммы.
#
#     Args:
#         text: Текст UML-диаграммы.
#
#     Returns:
#         Словарь, где ключ - имя интерфейса, значение - содержимое интерфейса.
#     """
#     pattern = r'interface (\w+)\s*\{([^}]+)\}'
#     matches = re.findall(pattern, text, re.DOTALL)
#     interfaces = {}
#     for name, content in matches:
#         interfaces[name] = content.strip()
#     return interfaces
#
#
# def parse_interface_content(content: str) -> Interface:
#     """
#     Разбирает содержимое интерфейса на составные части.
#
#     Args:
#         content: Содержимое интерфейса.
#
#     Returns:
#         Объект Interface.
#     """
#     doc = _parse_docstring(content)
#     constructor = _parse_constructor(content)
#     attributes = _parse_attributes(content)
#     methods = _parse_methods(content)
#
#     return Interface(
#         name="",  # Имя будет присвоено позже
#         doc=doc,
#         constructor=constructor,
#         attributes=attributes,
#         methods=methods
#     )
#
#
# def _parse_docstring(content: str) -> Optional[str]:
#     """
#     Извлекает docstring из содержимого интерфейса.
#     """
#     doc_pattern = r'"""(.*?)"""'
#     doc_match = re.search(doc_pattern, content, re.DOTALL)
#     return doc_match.group(1).strip() if doc_match else None
#
#
# def _parse_constructor(content: str) -> Optional[Method]:
#     """
#     Извлекает конструктор из содержимого интерфейса
#     """
#     method_pattern = r'^\s*([+-])(__init__)\(([^)]*)\)(?:\s*->\s*(\w+))?'
#     match = re.search(method_pattern, content, re.MULTILINE)
#
#     if match:
#         visibility, name, params_str, return_type = match.groups()
#         params = _parse_params(params_str)
#         return Method(visibility, name, params, return_type)
#
#     return None
# def _parse_attributes(content: str) -> List[Attribute]:
#     """
#     Извлекает атрибуты из содержимого интерфейса.
#     """
#     attribute_pattern = r'^\s*([+-])(\w+):\s*(\w+)'
#     matches = re.findall(attribute_pattern, content, re.MULTILINE)
#     return [Attribute(visibility, name, type) for visibility, name, type in matches]
#
#
# def _parse_methods(content: str) -> List[Method]:
#     """
#     Извлекает методы из содержимого интерфейса (исключая конструктор).
#     """
#     method_pattern = r'^\s*([+-])(\w+)\(([^)]*)\)(?:\s*->\s*(\w+))?'
#     matches = re.findall(method_pattern, content, re.MULTILINE)
#     methods = []
#     for visibility, name, params_str, return_type in matches:
#         if name != '__init__':
#             params = _parse_params(params_str)
#             methods.append(Method(visibility, name, params, return_type))
#     return methods
#
# def _parse_params(params_str: str) -> List[Tuple[str, Optional[str], Optional[str]]]:
#     """
#     Разбирает строку параметров метода.
#     """
#     params = []
#     for param_str in params_str.split(','):
#         param_str = param_str.strip()
#         if not param_str:
#             continue
#
#         parts = param_str.split(':')
#         name = parts[0].strip()
#         type = parts[1].strip() if len(parts) > 1 else None
#
#         parts = param_str.split('=')
#         default = parts[1].strip() if len(parts) > 1 else None
#
#         params.append((name, type, default))
#     return params
#
# def generate_class_code(interface: Interface) -> str:
#     """
#     Генерирует код класса Python на основе разобранного интерфейса.
#
#     **Args:**
#         interface: Разобранный интерфейс.
#
#     Returns:
#         Строка с кодом класса.
#     """
#     code_lines = [f'class {interface.name}:']
#
#     if interface.doc:
#         code_lines.append(f'    """\n\t{interface.doc}\n\t"""\n')
#
#     if interface.constructor:
#         code_lines.append(_generate_constructor_code(interface.constructor))
#
#     if not interface.constructor and interface.attributes:
#         for attribute in interface.attributes:
#             code_lines.append(_generate_attribute_code(attribute))
#
#     for method in interface.methods:
#         code_lines.append(_generate_method_code(method))
#
#     return '\n'.join(code_lines)
#
#
# def _generate_constructor_code(constructor: Method) -> str:
#     """Генерирует код конструктора."""
#     params_str = 'self'
#     for name, type, default in constructor.params:
#         param_decl = name
#         if type:
#             param_decl += f': {type}'
#         if default:
#             param_decl += f' = {default}'
#         params_str += ', ' + param_decl
#
#     code = f'    def {constructor.name}({params_str}):\n'
#     for name, _, _ in constructor.params:
#         code += f'        self.__{name} = {name}\n'
#     return code
#
# def _generate_attribute_code(attribute: Attribute) -> str:
#     """
#     Генерирует код атрибута.
#     """
#     return f'    {attribute.name}: {attribute.type} = None\n'
#
# def _generate_method_code(method: Method) -> str:
#     """
#     Генерирует код метода (заглушку).
#     """
#     params_str = 'self'
#     for name, type_param, default in method.params:
#         param_decl = name
#         if type_param:
#             param_decl += f': {type_param}'
#         if default:
#             param_decl += f' = {default}'
#         params_str += ', ' + param_decl
#
#     return_type = f' -> {method.return_type}' if method.return_type else ''
#     code = f'    def {method.name}({params_str}){return_type}:\n'
#     code += '        raise NotImplementedError()\n'
#     return code
#
# def generate_python_classes(interfaces: Dict[str, str]) -> str:
#     """
#     Генерирует код классов Python для всех интерфейсов.
#
#     Args:
#         interfaces: Словарь с интерфейсами.
#
#     Returns:
#         Строка с кодом классов.
#     """
#     parsed_interfaces = []
#     for name, content in interfaces.items():
#         parsed_interface = parse_interface_content(content)
#         parsed_interface.name = name
#         parsed_interfaces.append(parsed_interface)
#
#     return '\n\n'.join(
#         generate_class_code(interface) for interface in parsed_interfaces
#     )
#
# def save_python_classes_to_file(filename: str, class_code: str) -> None:
#     """
#     Сохраняет сгенерированный код классов в файл.
#
#     Args:
#         filename: Имя файла.
#         class_code: Код классов.
#     """
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


# import re
# from typing import Dict, List, Optional, Tuple
#
# from dataclasses import dataclass
#
#
# @dataclass
# class Method:
#     visibility: str
#     name: str
#     params: List[Tuple[str, Optional[str], Optional[str]]]
#     return_type: Optional[str]
#     doc: Optional[str] = None
#
#
# @dataclass
# class Attribute:
#     visibility: str
#     name: str
#     type: Optional[str]
#
#
# @dataclass
# class Interface:
#     name: str
#     doc: Optional[str]
#     constructor: Optional[Method]
#     attributes: List[Attribute]
#     methods: List[Method]
#
#
# def extract_all_interfaces(text: str) -> Dict[str, str]:
#     """
#     Извлекает все интерфейсы из текста UML-диаграммы.
#
#     Args:
#         text: Текст UML-диаграммы.
#
#     Returns:
#         Словарь, где ключ - имя интерфейса, значение - содержимое интерфейса.
#     """
#     pattern = r'interface (\w+)\s*\{([^}]+)\}'
#     matches = re.findall(pattern, text, re.DOTALL)
#     interfaces = {}
#     for name, content in matches:
#         interfaces[name] = content.strip()
#     return interfaces
#
#
# def parse_interface_content(content: str) -> Interface:
#     """
#     Разбирает содержимое интерфейса на составные части.
#
#     Args:
#         content: Содержимое интерфейса.
#
#     Returns:
#         Объект Interface.
#     """
#     doc = _parse_docstring(content)
#     constructor = _parse_constructor(content)
#     attributes = _parse_attributes(content)
#     methods = _parse_methods(content)
#
#     return Interface(
#         name="",  # Имя будет присвоено позже
#         doc=doc,
#         constructor=constructor,
#         attributes=attributes,
#         methods=methods
#     )
#
#
# def _parse_docstring(content: str) -> Optional[str]:
#     """
#     Извлекает docstring из содержимого интерфейса.
#     """
#     doc_pattern = r'"""(.*?)"""'
#     doc_match = re.search(doc_pattern, content, re.DOTALL)
#     return doc_match.group(1).strip() if doc_match else None
#
#
# def _parse_constructor(content: str) -> Optional[Method]:
#     """
#     Извлекает конструктор из содержимого интерфейса
#     """
#     method_pattern = r'^\s*([+-])(__init__)\(([^)]*)\)(?:\s*->\s*(\w+))?'
#     match = re.search(method_pattern, content, re.MULTILINE)
#
#     if match:
#         visibility, name, params_str, return_type = match.groups()
#         params = _parse_params(params_str)
#         doc = _parse_method_docstring(content, name)
#         return Method(visibility, name, params, return_type, doc)
#
#     return None
#
#
# def _parse_attributes(content: str) -> List[Attribute]:
#     """
#     Извлекает атрибуты из содержимого интерфейса.
#     """
#     attribute_pattern = r'^\s*([+-])(\w+):\s*(\w+)'
#     matches = re.findall(attribute_pattern, content, re.MULTILINE)
#     return [Attribute(visibility, name, type) for visibility, name, type in matches]
#
#
# def _parse_methods(content: str) -> List[Method]:
#     """
#     Извлекает методы из содержимого интерфейса (исключая конструктор).
#     """
#     method_pattern = r'^\s*([+-])(\w+)\(([^)]*)\)(?:\s*->\s*(\w+))?'
#     matches = re.findall(method_pattern, content, re.MULTILINE)
#     methods = []
#     for visibility, name, params_str, return_type in matches:
#         if name != '__init__':
#             params = _parse_params(params_str)
#             doc = _parse_method_docstring(content, name)
#             methods.append(Method(visibility, name, params, return_type, doc))
#     return methods
#
#
# def _parse_method_docstring(content: str, method_name: str) -> Optional[str]:
#     """
#     Извлекает docstring для конкретного метода и форматирует его.
#     """
#     method_start_pattern = rf'^\s*[+-]{method_name}\('
#     method_start_match = re.search(method_start_pattern, content, re.MULTILINE)
#
#     if method_start_match:
#         method_start_index = method_start_match.start()
#         doc_pattern = r'"""(.*?)"""'
#         doc_match = re.search(doc_pattern, content[method_start_index:], re.DOTALL)
#
#         if doc_match:
#             docstring = doc_match.group(1).strip()
#             return _format_docstring(docstring)
#     return None
#
#
# def _format_docstring(docstring: str) -> str:
#     """
#     Форматирует строку документации (docstring), добавляя правильные отступы
#     и пустые строки в начале и конце. Разбивает текст на секции (например, Args, Returns)
#     и форматирует их для удобного чтения.
#
#     Args:
#         docstring (str): Исходная строка документации, которую нужно отформатировать.
#
#     Returns:
#         str: Отформатированная строка документации с отступами и пустыми строками.
#              Если входная строка пуста, возвращается пустая строка.
#     """
#     if not docstring:
#         return ""
#
#     formatted_lines = []
#
#     formatted_lines.append("")
#
#     for line in docstring.split("\n"):
#         print(line)
#         if line.strip().startswith('**'):
#             formatted_lines.append(f"\n\t\t{line.strip()}")
#         elif ':' in line and '**' not in line:
#             formatted_lines.append(f"\t\t\t{line.strip()}")
#         else:
#             formatted_lines.append(f"\t\t{line.strip()}")
#
#     formatted_lines.append("")
#
#     formatted_docstring = "\n".join(formatted_lines)
#
#     return formatted_docstring
#
#
# def _parse_params(params_str: str) -> List[Tuple[str, Optional[str], Optional[str]]]:
#     """
#     Разбирает строку параметров метода.
#     """
#     params = []
#     for param_str in params_str.split(','):
#         param_str = param_str.strip()
#         if not param_str:
#             continue
#
#         parts = param_str.split(':')
#         name = parts[0].strip()
#         type_ = parts[1].strip() if len(parts) > 1 else None  # Переименовал type
#
#         parts = param_str.split('=')
#         default = parts[1].strip() if len(parts) > 1 else None
#
#         params.append((name, type_, default))  # Используем переименованную переменную
#     return params
#
#
# def generate_class_code(interface: Interface) -> str:
#     """
#     Генерирует код класса Python на основе разобранного интерфейса.
#
#     Args:
#         interface: Разобранный интерфейс.
#
#     Returns:
#         Строка с кодом класса.
#     """
#     code_lines = [f'class {interface.name}:']  # PEP 8: пробелы после двоеточия
#
#     if interface.doc:
#         code_lines.append(f'    """\n\t{interface.doc}\n\t"""\n')  # PEP 8: 4 пробела, одна пустая строка
#
#     if interface.constructor:
#         code_lines.append(_generate_constructor_code(interface.constructor))
#         code_lines.append('')  # Пустая строка после конструктора
#
#     if not interface.constructor and interface.attributes:
#         for attribute in interface.attributes:
#             code_lines.append(_generate_attribute_code(attribute))
#         code_lines.append('') # Пустая строка после атрибутов
#
#     for method in interface.methods:
#         code_lines.append(_generate_method_code(method))
#         code_lines.append('')  # Пустая строка после каждого метода
#
#     return '\n'.join(code_lines)
#
#
# def _generate_constructor_code(constructor: Method) -> str:
#     """Генерирует код конструктора."""
#     params_str = 'self'
#     for name, type_, default in constructor.params:  # Используем переименованную переменную
#         param_decl = name
#         if type_:
#             param_decl += f': {type_}'
#         if default:
#             param_decl += f' = {default}'
#         params_str += ', ' + param_decl
#
#     code = f'    def {constructor.name}({params_str}):\n'  # PEP 8: 4 пробела
#
#     if constructor.doc:
#         code += f'        """\t\t{constructor.doc}\t\t"""\n'  # PEP 8: 8 пробелов
#
#     for name, _, _ in constructor.params:
#         code += f'        self.__{name} = {name}\n'  # PEP 8: 8 пробелов
#     return code
#
#
# def _generate_attribute_code(attribute: Attribute) -> str:
#     """
#     Генерирует код атрибута.
#     """
#     return f'    {attribute.name}: {attribute.type} = None'  # PEP 8: 4 пробела
#
#
# def _generate_method_code(method: Method) -> str:
#     """
#     Генерирует код метода (заглушку).
#     """
#     params_str = 'self'
#     for name, type_param, default in method.params:
#         param_decl = name
#         if type_param:
#             param_decl += f': {type_param}'
#         if default:
#             param_decl += f' = {default}'
#         params_str += ', ' + param_decl
#
#     return_type = f' -> {method.return_type}' if method.return_type else ''
#     code = f'    def {method.name}({params_str}){return_type}:\n'  # PEP 8: 4 пробела
#
#     if method.doc:
#         code += f'        """{method.doc}\t\t"""\n'  # PEP 8: 8 пробелов
#
#     code += '        raise NotImplementedError()\n'  # PEP 8: 8 пробелов
#     return code
#
#
# def generate_python_classes(interfaces: Dict[str, str]) -> str:
#     """
#     Генерирует код классов Python для всех интерфейсов.
#
#     Args:
#         interfaces: Словарь с интерфейсами.
#
#     Returns:
#         Строка с кодом классов.
#     """
#     parsed_interfaces = []
#     for name, content in interfaces.items():
#         parsed_interface = parse_interface_content(content)
#         parsed_interface.name = name
#         parsed_interfaces.append(parsed_interface)
#
#     return '\n\n'.join(
#         generate_class_code(interface) for interface in parsed_interfaces
#     )
#
#
# def save_python_classes_to_file(filename: str, class_code: str) -> None:
#     """
#     Сохраняет сгенерированный код классов в файл.
#
#     Args:
#         filename: Имя файла.
#         class_code: Код классов.
#     """
#     with open(filename, 'w', encoding='utf-8') as file:
#         file.write(class_code)
#
#
# if __name__ == "__main__":
#     with open('uml_class_for_test.puml', 'r', encoding='utf-8') as f:
#         uml_content = f.read()
#
#     interfaces = extract_all_interfaces(uml_content)
#     generated_code = generate_python_classes(interfaces)
#     save_python_classes_to_file('generated_classes_from_test1.py', generated_code)


import re
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass

@dataclass
class Method:
    visibility: str
    name: str
    params: List[Tuple[str, Optional[str], Optional[str]]]
    return_type: Optional[str]
    doc: Optional[str] = None

@dataclass
class Attribute:
    visibility: str
    name: str
    type: Optional[str]

@dataclass
class Interface:
    name: str
    doc: Optional[str]
    constructor: Optional[Method]
    attributes: List[Attribute]
    methods: List[Method]

def parse_md_docs(md_content: str) -> Dict[str, str]:
    method_docs = {}
    sections = re.split(r'\n## ', md_content)
    for section in sections:
        if not section.strip():
            continue
        header_line = section.split('\n', 1)[0].strip()
        if header_line.startswith('`') and '`' in header_line:
            # Это описание метода
            method_name_match = re.match(r'`?(\w+)(?:\(\))?`?', header_line)
            if not method_name_match:
                continue
            method_name = method_name_match.group(1)
            content = section.split('\n', 1)[1] if '\n' in section else ''
            content = re.sub(r'^---\s*', '', content, flags=re.MULTILINE).strip()
            method_docs[method_name] = content
        else:
            # Это описание класса
            class_doc = section.strip()
            # Убираем лишние символы
            # class_doc = re.sub(r'^# `_SwitchCases`\s*', '', class_doc)
            class_doc = re.sub(r'^# `_(.*?)`\s*', '', class_doc)
            class_doc = re.sub(r'---\s*', '', class_doc)
            method_docs['__class__'] = class_doc.strip()
    return method_docs

def extract_all_interfaces(text: str) -> Dict[str, str]:
    pattern = r'interface (\w+)\s*\{([^}]+)\}'
    matches = re.findall(pattern, text, re.DOTALL)
    return {name: content.strip() for name, content in matches}

def _parse_docstring(content: str) -> Optional[str]:
    doc_pattern = r'"""(.*?)"""'
    doc_match = re.search(doc_pattern, content, re.DOTALL)
    return doc_match.group(1).strip() if doc_match else None

def _parse_constructor(content: str) -> Optional[Method]:
    method_pattern = r'^\s*([+-])(__init__)\(([^)]*)\)(?:\s*->\s*(\w+))?'
    match = re.search(method_pattern, content, re.MULTILINE)
    if match:
        visibility, name, params_str, return_type = match.groups()
        params = _parse_params(params_str)
        doc = _parse_method_docstring(content, name)
        return Method(visibility, name, params, return_type, doc)
    return None

def _parse_attributes(content: str) -> List[Attribute]:
    attribute_pattern = r'^\s*([+-])(\w+):\s*(\w+)'
    matches = re.findall(attribute_pattern, content, re.MULTILINE)
    return [Attribute(visibility, name, type_) for visibility, name, type_ in matches]

def _parse_methods(content: str) -> List[Method]:
    method_pattern = r'^\s*([+-])(\w+)\(([^)]*)\)(?:\s*->\s*(\w+))?'
    matches = re.findall(method_pattern, content, re.MULTILINE)
    return [Method(visibility, name, _parse_params(params_str), return_type, _parse_method_docstring(content, name))
            for visibility, name, params_str, return_type in matches if name != '__init__']

def _parse_method_docstring(content: str, method_name: str) -> Optional[str]:
    method_start_pattern = rf'^\s*[+-]{method_name}\('
    method_start_match = re.search(method_start_pattern, content, re.MULTILINE)
    if method_start_match:
        doc_pattern = r'"""(.*?)"""'
        doc_match = re.search(doc_pattern, content[method_start_match.start():], re.DOTALL)
        return doc_match.group(1).strip() if doc_match else None
    return None

def _parse_params(params_str: str) -> List[Tuple[str, Optional[str], Optional[str]]]:
    params = []
    for param in params_str.split(','):
        param = param.strip()
        if not param:
            continue
        name_type = param.split('=', 1)
        name_type_default = name_type[0].split(':', 1)
        name = name_type_default[0].strip()
        type_ = name_type_default[1].strip() if len(name_type_default) > 1 else None
        default = name_type[1].strip() if len(name_type) > 1 else None
        params.append((name, type_, default))
    return params

def generate_class_code(interface: Interface, class_doc: Optional[str]) -> str:
    code_lines = [f'class {interface.name}:']
    if class_doc:
        code_lines.append(f'    """{class_doc}"""\n')
    elif interface.doc:
        code_lines.append(f'    """{interface.doc}"""\n')
    if interface.constructor:
        code_lines.append(_generate_constructor_code(interface.constructor))
        code_lines.append('')

    if interface.attributes and not interface.constructor:
        for attr in interface.attributes:
            code_lines.append(f'    {attr.name}: {attr.type} = None')
        code_lines.append('')
    for method in interface.methods:
        code_lines.append(_generate_method_code(method))
        code_lines.append('')
    return '\n'.join(code_lines).strip()

def _generate_constructor_code(constructor: Method) -> str:
    params = ['self'] + [f'{name}: {type_}' if type_ else name for name, type_, _ in constructor.params]
    code = f'    def __init__({", ".join(params)}):\n'
    if constructor.doc:
        code += f'        """\n{_format_docstring(constructor.doc)}\n        """\n'
    for name, _, _ in constructor.params:
        code += f'        self._{name} = {name}\n'
    return code

def _generate_method_code(method: Method) -> str:
    params = ['self'] + [f'{name}: {type_}' if type_ else name for name, type_, _ in method.params]
    return_type = f' -> {method.return_type}' if method.return_type else ''
    code = f'    def {method.name}({", ".join(params)}){return_type}:\n'
    if method.doc:
        code += f'        """\n{_format_docstring(method.doc)}\n        """\n'
    code += '        raise NotImplementedError()'
    return code

def _format_docstring(docstring: str) -> str:
    if not docstring:
        return ""
    lines = docstring.split('\n')
    formatted_lines = []
    for line in lines:
        stripped = line.strip()
        if stripped.startswith('**'):
            formatted_lines.append(f'        {stripped}')
        elif ':' in stripped and not stripped.startswith('**'):
            formatted_lines.append(f'            {stripped}')
        else:
            formatted_lines.append(f'        {stripped}')
    return '\n'.join(formatted_lines)

def generate_python_classes(interfaces: Dict[str, str], method_docs: Dict[str, str]) -> str:
    parsed_interfaces = []
    for name, content in interfaces.items():
        interface = Interface(
            name=name,
            doc=_parse_docstring(content),
            constructor=_parse_constructor(content),
            attributes=_parse_attributes(content),
            methods=_parse_methods(content)
        )
        for method in interface.methods:
            if method.name in method_docs:
                method.doc = f'{method.doc}\n\n{method_docs[method.name]}' if method.doc else method_docs[method.name]
        if interface.constructor and interface.constructor.name in method_docs:
            interface.constructor.doc = f'{interface.constructor.doc}\n\n{method_docs[interface.constructor.name]}'\
                if interface.constructor.doc else method_docs[interface.constructor.name]
        parsed_interfaces.append(interface)
    return '\n\n'.join(generate_class_code(interface, method_docs.get('__class__')) for interface in parsed_interfaces)

def save_python_classes_to_file(filename: str, class_code: str) -> None:
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(class_code)

if __name__ == "__main__":
    with open('uml_class_for_test.puml', 'r', encoding='utf-8') as f:
        uml_content = f.read()
    with open('index.md', 'r', encoding='utf-8') as f:
        md_content = f.read()
    method_docs = parse_md_docs(md_content)
    interfaces = extract_all_interfaces(uml_content)
    generated_code = generate_python_classes(interfaces, method_docs)
    save_python_classes_to_file('generated_classes_from_test1.py', generated_code)