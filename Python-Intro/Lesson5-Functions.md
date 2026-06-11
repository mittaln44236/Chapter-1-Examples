# Lesson 5: Functions

## What is a Function?
A **function** is a named, reusable block of code. Functions help you:
- Avoid repeating the same code.
- Break a large problem into smaller, manageable pieces.
- Make your code easier to read and test.

---

## Defining and Calling a Function
Use `def` to define a function. Call it by writing its name followed by parentheses.

```python
def greet():
    print("Hello, Pioneer!")

greet()   # call the function
greet()   # call it again
```

---

## Parameters and Arguments
**Parameters** are variables listed inside the parentheses of a `def`. **Arguments** are the actual values you pass when calling the function.

```python
def greet(name):
    print(f"Hello, {name}!")

greet("Alex")     # Hello, Alex!
greet("Jordan")   # Hello, Jordan!
```

### Multiple Parameters
```python
def add(a, b):
    print(a + b)

add(3, 5)   # 8
```

### Default Parameter Values
If an argument is not provided, the default is used.

```python
def power(base, exponent=2):
    print(base ** exponent)

power(4)      # 16  (exponent defaults to 2)
power(2, 10)  # 1024
```

---

## Return Values
Use `return` to send a value back to the caller.

```python
def square(n):
    return n * n

result = square(7)
print(result)         # 49
print(square(3) + 1)  # 10
```

A function **without** an explicit `return` statement returns `None`.

---

## Scope: Local vs. Global Variables
Variables created **inside** a function are **local** — they only exist while the function runs.

```python
def demo():
    message = "I'm local"
    print(message)

demo()
# print(message)  # ERROR — message doesn't exist here
```

Variables defined **outside** all functions are **global** and can be read (but not reassigned) inside a function without extra steps.

---

## Putting It All Together: A Mini Calculator
```python
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: division by zero"
    return a / b

x = float(input("First number: "))
y = float(input("Second number: "))
op = input("Operation (+, -, *, /): ")

if op == "+":
    print(add(x, y))
elif op == "-":
    print(subtract(x, y))
elif op == "*":
    print(multiply(x, y))
elif op == "/":
    print(divide(x, y))
else:
    print("Unknown operation")
```

---

## Practice Exercises

1. Write a function `celsius_to_fahrenheit(c)` that returns the Fahrenheit equivalent of a Celsius temperature (`F = C * 9/5 + 32`). Test it with a few values.

2. Write a function `is_even(n)` that returns `True` if `n` is even and `False` otherwise. Use it to print all even numbers from 1 to 20.

3. Write a function `max_of_three(a, b, c)` that returns the largest of three numbers **without** using the built-in `max()` function.

---
*Previous: [Lesson 4 — Loops](Lesson4-Loops.md)*  
*Next: [Lesson 6 — Lists](Lesson6-Lists.md)*
