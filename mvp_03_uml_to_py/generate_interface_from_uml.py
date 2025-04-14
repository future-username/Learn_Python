from dataclasses import dataclass
from typing import Dict, List, Optional, Tuple
import re


@dataclass
class Method:
    visibility: str
    name: str
    params: List[Tuple[str, Optional[str], Optional[str]]]
    return_type: Optional[str]
    doc: Optional[str] = None
    is_property: bool = False


@dataclass
class Attribute:
    visibility: str
    name: str
    type: Optional[str]
    default: Optional[str] = None


@dataclass
class Property:
    name: str
    getter: Optional[Method]
    setter: Optional[Method]
    type: Optional[str]
    doc: Optional[str] = None


@dataclass
class Interface:
    name: str
    doc: Optional[str]
    constructor: Optional[Method]
    attributes: List[Attribute]
    methods: List[Method]
    properties: List[Property]


def _generate_property_code(prop: Property) -> str:
    code = []

    if prop.getter:
        code.append(f'    @property')
        code.append(f'    def {prop.name}(self) -> {prop.type}:')
        if prop.doc or prop.getter.doc:
            docs = []
            if prop.doc:
                docs.append(prop.doc)
            if prop.getter.doc:
                docs.append(prop.getter.doc)
            code.append(f'        """\n{"\n".join(docs)}\n        """')
        code.append(f'        return self._{prop.name}\n')

    if prop.setter:
        code.append(f'    @{prop.name}.setter')
        code.append(f'    def {prop.name}(self, value: {prop.type}):')
        if prop.setter.doc:
            code.append(f'        """{prop.setter.doc}"""')
        code.append(f'        self._{prop.name} = value')

    return '\n'.join(code)


def _parse_properties(content: str, methods: List[Method]) -> List[Property]:
    properties = {}

    # Группируем getter/setter
    for method in methods:
        if method.name.startswith('get_'):
            prop_name = method.name[4:]
            prop = properties.get(prop_name, Property(
                name=prop_name,
                getter=None,
                setter=None,
                type=method.return_type,
                doc=method.doc
            ))
            prop.getter = method
            prop.type = method.return_type
            properties[prop_name] = prop

        elif method.name.startswith('set_'):
            prop_name = method.name[4:]
            prop = properties.get(prop_name, Property(
                name=prop_name,
                getter=None,
                setter=None,
                type=method.params[0][1] if method.params else None,
                doc=method.doc
            ))
            prop.setter = method
            properties[prop_name] = prop

    return list(properties.values())


def generate_class_code(interface: Interface, class_doc: Optional[str]) -> str:
    code_lines = [f'class {interface.name}:']

    # Документация класса
    doc_source = class_doc or interface.doc
    if doc_source:
        code_lines.append(f'    """{doc_source}"""\n')

    # Конструктор
    if interface.constructor:
        code_lines.append(_generate_constructor_code(interface.constructor))
        code_lines.append('')

    # Свойства
    for prop in interface.properties:
        code_lines.append(_generate_property_code(prop))
        code_lines.append('')

    # Обычные методы
    for method in interface.methods:
        if not any([method.is_property, method.name.startswith(('get_', 'set_'))]):
            code_lines.append(_generate_method_code(method))
        code_lines.append('')

    return '\n'.join(code_lines).strip()


def _generate_constructor_code(constructor: Method) -> str:
    params = ['self'] + [f'{name}: {type_}' for name, type_, _ in constructor.params]
    code = [f'    def __init__({", ".join(params)}):']

    if constructor.doc:
        code.append(f'        """{constructor.doc}"""')

    # Инициализация атрибутов
    for name, _, _ in constructor.params:
        code.append(f'        self._{name} = {name}')

    return '\n'.join(code)


def _generate_method_code(method: Method) -> str:
    params = ['self'] + [f'{name}: {type_}' for name, type_, _ in method.params]
    return_type = f' -> {method.return_type}' if method.return_type else ''
    code = [f'    def {method.name}({", ".join(params)}){return_type}:']

    if method.doc:
        code.append(f'        """{method.doc}"""')

    code.append('        raise NotImplementedError()')
    return '\n'.join(code)

def parse_md_docs(md_content: str) -> Dict[str, str]:
    method_docs = {}
    sections = re.split(r'\n## ', md_content)

    for section in sections:
        if not section.strip():
            continue

        header_line = section.split('\n', 1)[0].strip()

        if header_line.startswith('`') and '`' in header_line:
            method_name_match = re.match(r'`(\w+)\(\)`', header_line)
            if method_name_match:
                method_name = method_name_match.group(1)
                content = section.split('\n', 1)[1] if '\n' in section else ''
                content = re.sub(r'^---\s*', '', content, flags=re.MULTILINE).strip()
                method_docs[method_name] = content
        elif header_line.startswith('_'):
            class_doc = re.sub(r'^_', '', header_line).strip()
            content = section.split('\n', 1)[1] if '\n' in section else ''
            method_docs['__class__'] = content.strip()

    return method_docs


def extract_all_interfaces(text: str) -> Dict[str, str]:
    pattern = r'interface (\w+)\s*\{([^}]+)\}'
    matches = re.findall(pattern, text, re.DOTALL)
    return {name: content.strip() for name, content in matches}


def _parse_docstring(content: str) -> Optional[str]:
    doc_pattern = r'^\s*"""(.*?)"""\s*'
    doc_match = re.search(doc_pattern, content, re.DOTALL)
    return doc_match.group(1).strip() if doc_match else None


def _parse_constructor(content: str) -> Optional[Method]:
    method_pattern = r'^\s*\+\s*__init__\(([^)]*)\)(?:\s*->\s*(\w+))?'
    match = re.search(method_pattern, content, re.MULTILINE)
    if match:
        params_str, return_type = match.groups()
        params = _parse_params(params_str)
        doc = _parse_method_docstring(content, '__init__')
        return Method('+', '__init__', params, return_type, doc)
    return None


def _parse_attributes(content: str) -> List[Attribute]:
    attribute_pattern = r'^\s*([+-])(\w+):\s*(\w+)'
    matches = re.findall(attribute_pattern, content, re.MULTILINE)
    return [Attribute(vis, name, type_) for vis, name, type_ in matches]


def _parse_methods(content: str) -> List[Method]:
    methods = []

    # Парсим свойства
    property_pattern = r'^\s*[+] (get|set)(\w+)\(([^)]*)\)(?:\s*->\s*(\w+))?'
    for match in re.finditer(property_pattern, content, re.MULTILINE):
        prop_type, name, params_str, ret_type = match.groups()
        method = Method(
            visibility='+',
            name=f'{prop_type.lower()}_{name}',
            params=_parse_params(params_str),
            return_type=ret_type,
            doc=_parse_method_docstring(content, f'{prop_type}{name}'),
            is_property=True
        )
        methods.append(method)

    # Парсим обычные методы
    method_pattern = r'^\s*([+])(\w+)\(([^)]*)\)(?:\s*->\s*(\w+))?'
    matches = re.findall(method_pattern, content, re.MULTILINE)
    for vis, name, params_str, ret_type in matches:
        if name.startswith(('get', 'set')):
            continue
        method = Method(
            visibility=vis,
            name=name,
            params=_parse_params(params_str),
            return_type=ret_type,
            doc=_parse_method_docstring(content, name)
        )
        methods.append(method)

    return methods


def _parse_method_docstring(content: str, method_name: str) -> Optional[str]:
    method_block_pattern = rf'^\s*\+{method_name}\([^)]*\)\s*(->\s*\w+)?\s*:\n\s*"""(.*?)"""'
    match = re.search(method_block_pattern, content, re.DOTALL | re.MULTILINE)
    return match.group(2).strip() if match else None


def _parse_params(params_str: str) -> List[Tuple[str, Optional[str], Optional[str]]]:
    params = []
    for param in params_str.split(','):
        param = param.strip()
        if not param:
            continue
        parts = re.split(r':|=', param, maxsplit=2)
        name = parts[0].strip()
        type_ = parts[1].strip() if len(parts) > 1 else None
        default = parts[2].strip() if len(parts) > 2 else None
        params.append((name, type_, default))
    return params


def generate_python_classes(interfaces: Dict[str, str], method_docs: Dict[str, str]) -> str:
    parsed_interfaces = []

    for name, content in interfaces.items():
        interface = Interface(
            name=name,
            doc=_parse_docstring(content),
            constructor=_parse_constructor(content),
            attributes=_parse_attributes(content),
            methods=_parse_methods(content),
            properties=_parse_properties(content)
        )

        if method_docs:
            for method in interface.methods:
                if method.name in method_docs:
                    method.doc = method_docs[method.name]
            if interface.constructor and '__init__' in method_docs:
                interface.constructor.doc = method_docs['__init__']

        parsed_interfaces.append(interface)

    return '\n\n'.join(
        generate_class_code(interface, method_docs.get('__class__'))
        for interface in parsed_interfaces
    )


def save_python_classes_to_file(filename: str, class_code: str) -> None:
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(class_code)


if __name__ == "__main__":
    with open('uml_class_for_test.puml', 'r', encoding='utf-8') as f:
        uml_content = f.read()

    method_docs = {}
    try:
        with open('index.md', 'r', encoding='utf-8') as f:
            method_docs = parse_md_docs(f.read())
    except FileNotFoundError:
        print("Info: MD documentation not found, using UML only")
    except Exception as e:
        print(f"Error reading MD file: {e}")

    interfaces = extract_all_interfaces(uml_content)
    generated_code = generate_python_classes(interfaces, method_docs)
    save_python_classes_to_file('generated_classes.py', generated_code)
