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

