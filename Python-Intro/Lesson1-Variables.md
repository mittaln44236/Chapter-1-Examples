# Lesson 1: Variables and Data Types

## What is a Variable?
A variable is a named container that stores a value in memory. In Python, you do **not** need to declare a data type — Python figures it out automatically.

```python
name      = "Alex"   # str   (text)
age       = 16       # int   (whole number)
gpa       = 3.85     # float (decimal number)
honor_roll = True    # bool  (True or False)
```

## Core Data Types

| Type    | Example           | Description               |
|---------|-------------------|---------------------------|
| `str`   | `"Hello"`         | Text (always in quotes)   |
| `int`   | `42`              | Whole number              |
| `float` | `3.14`            | Decimal number            |
| `bool`  | `True` / `False`  | Logical true/false value  |

## Checking the Type of a Variable
Use the built-in `type()` function to see what type a variable holds.

```python
x = 7
print(type(x))   # <class 'int'>
```

## String Operations
Strings can be combined (**concatenated**) with `+` and repeated with `*`.

```python
first    = "Hello"
second   = "World"
greeting = first + " " + second
print(greeting)          # Hello World
print("Ha" * 3)          # HaHaHa
```

## Converting Between Types
| Function    | What it does                   |
|-------------|-------------------------------|
| `int(x)`    | Converts `x` to an integer    |
| `float(x)`  | Converts `x` to a decimal     |
| `str(x)`    | Converts `x` to text          |

```python
num_text = "5"
num      = int(num_text)
print(num + 3)    # 8
```

## Practice Exercises

1. Create variables that store your **name**, your **age**, your **GPA**, and whether you are an **honor roll** student. Print each variable on its own line.

2. Convert the integer `2026` to a string and concatenate it with `"Class of "`. Print the result.

3. What does `type(3.0)` return? What about `type(3)`? Why are they different?

---
*Next: [Lesson 2 — Input & Output](Lesson2-InputOutput.md)*
