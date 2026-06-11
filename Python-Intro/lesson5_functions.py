# Lesson 5 Examples: Functions

# --- Basic function ---
def greet(name):
    print(f"Hello, {name}!")

greet("Alex")
greet("Jordan")

# --- Return values ---
def square(n):
    return n * n

print(square(7))           # 49
print(square(3) + 1)       # 10

# --- Default parameters ---
def power(base, exponent=2):
    return base ** exponent

print(power(4))     # 16
print(power(2, 10)) # 1024

# --- Temperature converter ---
def celsius_to_fahrenheit(c):
    return c * 9 / 5 + 32

print(celsius_to_fahrenheit(0))    # 32.0
print(celsius_to_fahrenheit(100))  # 212.0
print(celsius_to_fahrenheit(37))   # 98.6

# --- Mini calculator ---
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

x  = float(input("First number: "))
y  = float(input("Second number: "))
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
