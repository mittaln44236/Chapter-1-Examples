# Lesson 2: Input and Output

## Printing to the Screen
The `print()` function displays output. You can print multiple values by separating them with commas — Python will add a space between them automatically.

```python
print("Hello, Pioneers!")
print("Two plus two is", 2 + 2)
```

### f-Strings (Formatted Strings)
An **f-string** lets you embed variable values directly inside a string — just prefix the opening quote with `f` and place variable names inside `{}`.

```python
name = "Jordan"
grade = 11
print(f"Welcome, {name}! You are in grade {grade}.")
# Welcome, Jordan! You are in grade 11.
```

## Getting Input from the User
The `input()` function pauses the program and waits for the user to type something. It always returns a **string**.

```python
name = input("What is your name? ")
print(f"Nice to meet you, {name}!")
```

### Converting Input to a Number
Because `input()` returns a string, you must convert it if you want to do math.

```python
age_text = input("How old are you? ")
age      = int(age_text)              # convert to integer
print(f"In 10 years you will be {age + 10}.")
```

Or more concisely:

```python
age = int(input("How old are you? "))
```

## Escape Characters
Special characters inside strings start with a backslash `\`.

| Escape | Meaning         |
|--------|----------------|
| `\n`   | New line        |
| `\t`   | Tab             |
| `\\`   | Literal `\`     |
| `\"`   | Literal `"`     |

```python
print("Line 1\nLine 2\nLine 3")
print("Name:\tAlex")
```

## Practice Exercises

1. Write a program that asks the user for their **first name** and **last name** separately, then prints `"Hello, <first> <last>!"` using an f-string.

2. Ask the user to enter two numbers. Print their **sum**, **difference**, **product**, and **quotient**.

3. Ask the user for their birth year and calculate how old they will turn this calendar year. Print a message like `"You will turn 17 in 2026."`.

---
*Previous: [Lesson 1 — Variables & Data Types](Lesson1-Variables.md)*  
*Next: [Lesson 3 — Conditionals](Lesson3-Conditionals.md)*
