# Lesson 3 Examples: Conditionals

# --- Simple if / elif / else ---
score = int(input("Enter your score (0-100): "))

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")

# --- Logical operators ---
age = int(input("Enter your age: "))

if age >= 16 and age < 18:
    print("You can get a learner's permit.")
elif age >= 18:
    print("You can get a full license.")
else:
    print("You must wait to drive.")

# --- Nested conditionals: simple login ---
correct_user = "pioneer"
correct_pass = "secret123"

username = input("Username: ")
password = input("Password: ")

if username == correct_user:
    if password == correct_pass:
        print("Login successful!")
    else:
        print("Wrong password.")
else:
    print("Unknown username.")
