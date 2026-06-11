# Lesson 1 Examples: Variables and Data Types

# --- Declaring variables of different types ---
name       = "Alex"
age        = 16
gpa        = 3.85
honor_roll = True

print(name)
print(age)
print(gpa)
print(honor_roll)

# --- Checking types ---
print(type(name))        # <class 'str'>
print(type(age))         # <class 'int'>
print(type(gpa))         # <class 'float'>
print(type(honor_roll))  # <class 'bool'>

# --- String concatenation and repetition ---
first    = "Hello"
second   = "World"
greeting = first + " " + second
print(greeting)          # Hello World
print("Ha" * 3)          # HaHaHa

# --- Type conversion ---
num_text = "5"
num      = int(num_text)
print(num + 3)           # 8

year      = 2026
year_text = str(year)
print("Class of " + year_text)   # Class of 2026
