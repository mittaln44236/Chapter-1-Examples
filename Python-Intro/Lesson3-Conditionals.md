# Lesson 3: Conditionals

## What is a Conditional?
A conditional lets your program make decisions. It runs different blocks of code depending on whether a condition is `True` or `False`.

## The `if` Statement
```python
score = 85

if score >= 90:
    print("A")
```

Python uses **indentation** (4 spaces or one tab) to define code blocks — there are no curly braces like in Java.

## `if` / `else`
```python
score = 72

if score >= 60:
    print("Passing")
else:
    print("Failing")
```

## `if` / `elif` / `else`
Use `elif` ("else if") to check multiple conditions in order.

```python
score = int(input("Enter your score: "))

if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("F")
```

## Comparison Operators
| Operator | Meaning                  | Example        |
|----------|--------------------------|----------------|
| `==`     | Equal to                 | `x == 5`       |
| `!=`     | Not equal to             | `x != 5`       |
| `>`      | Greater than             | `x > 5`        |
| `<`      | Less than                | `x < 5`        |
| `>=`     | Greater than or equal to | `x >= 5`       |
| `<=`     | Less than or equal to    | `x <= 5`       |

## Logical Operators
Combine conditions using `and`, `or`, and `not`.

```python
age = 17

if age >= 16 and age < 18:
    print("You can get a learner's permit.")

if age < 13 or age > 19:
    print("You are not a teenager.")

if not age == 18:
    print("You are not 18.")
```

## Nested Conditionals
You can place an `if` inside another `if`.

```python
username = input("Username: ")
password = input("Password: ")

if username == "pioneer":
    if password == "secret123":
        print("Login successful!")
    else:
        print("Wrong password.")
else:
    print("Unknown username.")
```

## Practice Exercises

1. Ask the user for a number and print whether it is **positive**, **negative**, or **zero**.

2. Ask the user for their **age** and print one of these messages:
   - Under 13: `"Child"`
   - 13–17: `"Teenager"`
   - 18–64: `"Adult"`
   - 65 or older: `"Senior"`

3. Write a simple login program: define a correct username and password as variables. Ask the user to enter both. Print `"Access granted"` if both match, otherwise print `"Access denied"`.

---
*Previous: [Lesson 2 — Input & Output](Lesson2-InputOutput.md)*  
*Next: [Lesson 4 — Loops](Lesson4-Loops.md)*
