# YAML

YAML (YAML Ain't Markup Language) is a human-readable data serialization
language for all programming languages.
It is commonly used for configuration files and in applications where data is
being stored or transmitted.
It uses Python-style indentation to indicate nesting and does not require
quotes around most string values (it also supports JSON style [] and {} mixed
in the same file).

## Content

-   [YAML to JSON conversion](yaml_to_json.py)
-   [JSON to YAML conversion](json_to_yaml.py)
-   Example files:
    -   [YAML example](example.yaml)
    -   [JSON example](example.json)

# Syntax

-   [Indentation](#indentation)
-   [Comments](#comments)
-   [Scalar](#scalar):
    -   [Boolean](#boolean)
    -   [Integer](#integer)
    -   [Float](#float)
    -   [String](#string)
-   [List](#list)
-   [Associative Array](#associative-array)

-   ## Indentation

Whitespace indentation is used for denoting structure; however, tab characters
are not allowed as part of that indentation.

Example YAML:

```yaml
Section:
    heading: Heading 1
```

<details>
    <summary>JSON equivalence</summary><br>

```json
{
    "Section": {
        "heading": "Heading 1"
    }
}
```

</details>

-   ## Comments

Comments begin with the number sign `#` and can start anywhere on a line and
continue until the end of the line.
Comments must be separated from other tokens by whitespace characters.

Example YAML:

```yaml
# Section:
#     heading: Heading 1
```

<details>
    <summary>JSON equivalence</summary><br>

JSON (equivalence):

```json
// {
//     "Section": {
//         "heading": "Heading 1"
//     }
// }
```

</details>

-   ## Scalar

Scalar is a simple data type.
In YAML, scalar means a simple value for a key.
The value of the scalar can be boolean, integer, float and string.

-   ### Boolean

A Boolean value can be True/False or Yes/No or On/Off.

Example YAML:

```yaml
bool: True
answer: No
state: Off
```

<details>
    <summary>JSON equivalence</summary><br>

JSON (equivalence):

```json
{
    "bool": true,
    "answer": "No",
    "state": "Off"
}
```

</details>

-   ### Integer

An Integer data type can be decimal, octal or hexadecimal.
Hex values are indicated by `0x`.
Octal values are indicated by a leading zero `0`.

Example YAML:

```yaml
dec: 12345
oct: 012345
hex: 0x12d4
```

<details>
    <summary>JSON equivalence</summary><br>

JSON (equivalence):

```json
{
    "dec": 12345,
    "oct": 12345,
    "hex": 4820
}
```

</details>

-   ### Float

The floating-point value can be fixed and exponential.

Example YAML:

```yaml
float: 180.0
exp: 12.3015e+05
```

<details>
    <summary>JSON equivalence</summary><br>

JSON (equivalence):

```json
{
    "float": 180.0,
    "exp": 1230150.0
}
```

</details>

-   ### String

Strings (one type of scalar in YAML) are ordinarily unquoted, but may be
enclosed in double-quotes `"` or single-quotes `'`.

Example YAML:

```yaml
Section:
    heading: "Heading 1"
```

<details>
    <summary>JSON equivalence</summary><br>

JSON (equivalence):

```json
{
    "Section": {
        "heading": "Heading 1"
    }
}
```

</details>

-   ## List

List members are denoted by a leading hyphen `-` with one member per line.

Example YAML:

```yaml
Font Sizes:
    - 11
    - 15
    - 22
```

<details>
    <summary>JSON equivalence</summary><br>

JSON (equivalence):

```json
{
    "Font Sizes": [
        11,
        15,
        22
    ]
}
```

YAML (equivalence):

```yaml
Font Sizes: [11, 15, 22]
```

YAML (equivalence):

```yaml
Font Sizes: [
    11,
    15,
    22
]
```

</details>

-   ## Associative Array

An associative array entry is represented using colon space in the form
`key: value` with one entry per line.
YAML requires the colon to be followed by a space so that strings can be
represented without needing to be enclosed in quotes.

Example YAML:

```yaml
Section:
    heading: Heading 1
    font:
        name: Times New Roman
        size: 22
        color_theme: ACCENT_2
```

<details>
    <summary>JSON equivalence</summary><br>

JSON (equivalence):

```json
{
    "Section": {
        "heading": "Heading 1",
        "font": {
            "name": "Times New Roman",
            "size": 22,
            "color_theme": "ACCENT_2"
        }
    }
}
```

YAML (equivalence):

```yaml
Section:
    font: { color_theme: ACCENT_2, name: Times New Roman, size: 22 }
    heading: Heading 1
```

YAML (equivalence):

```yaml
Section:
    {
        heading: Heading 1,
        font: { color_theme: ACCENT_2, name: Times New Roman, size: 22 }
    }
```

</details>
