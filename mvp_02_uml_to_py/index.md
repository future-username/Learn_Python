## Class Descriptions

### 🟣 _MyString

**Description**: Main class containing string manipulation methods.

#### Attributes

| Name     | Type | Visibility | Description             |
|----------|------|------------|-------------------------|
| `__line` | str  | private    | Internal string storage |

#### Methods

| Method           | Returns         | Description               |
|------------------|-----------------|---------------------------|
| `switch_cases()` | `SwitchCase`    | Short desc                |
| `justifies()`    | `JustifyString` | Get justification methods |
| `is_methods()`   | `IsString`      | Get validation methods    |

---

### 🔵 _SwitchCases

**Description**: Handles case transformation operations.

#### Constructor

```python
__init__(line: str)`
```

**Args**:

- `line`: исходная строка

#### Methods

| Method    | Returns | Description           |
|-----------|---------|-----------------------|
| `upper()` | str     | Convert to uppercase  |
| `lower()` | str     | Convert to lowercase  |
| `title()` | str     | Convert to title case |

---

### 🟡 _IsString

**Description**: Provides string validation checks.

#### Methods

| Method      | Returns | Description                      |
|-------------|---------|----------------------------------|
| `isupper()` | bool    | Check if all chars are uppercase |
| `islower()` | bool    | Check if all chars are lowercase |
| `istitle()` | bool    | Check if string is title-cased   |

---

### 🟠 _JustifyString

**Description**: Handles string alignment operations.

#### Methods

| Method                         | Returns | Description                      |
|--------------------------------|---------|----------------------------------|
| `center(width, fill_char)`     | str     | Center-align string with padding |
| `left_just(width, fill_char)`  | str     | Left-align string with padding   |
| `right_just(width, fill_char)` | str     | Right-align string with padding  |

---

### 🔴 _JustifyString1

**Description**: Secondary justification interface (duplicate?).

#### Methods

Same as _JustifyString but without constructor documentation.

---

## Relationships

```plantuml
_SwitchCases *-- _MyString: composition
_IsString *-- _MyString: composition
_JustifyString *-- _MyString: composition
```

1. `_MyString` COMPOSES:
    - Case manipulation functionality through `_SwitchCases`
    - Validation checks through `_IsString`
    - Text alignment through `_JustifyString`

```