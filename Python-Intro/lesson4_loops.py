# Lesson 4 Examples: Loops

# --- for loop with range ---
print("Counting 1 to 10:")
for i in range(1, 11):
    print(i, end=" ")
print()

# --- Count down ---
print("Countdown:")
for i in range(10, 0, -1):
    print(i, end=" ")
print("Go!")

# --- Loop over a string ---
word = "Pioneer"
print("Letters in 'Pioneer':")
for letter in word:
    print(letter)

# --- while loop ---
print("while loop:")
count = 1
while count <= 5:
    print(count)
    count += 1

# --- Input validation ---
age = int(input("Enter your age (1-120): "))
while age < 1 or age > 120:
    print("Invalid. Please try again.")
    age = int(input("Enter your age (1-120): "))
print(f"Your age is {age}.")

# --- break and continue ---
print("break example — stop at 7:")
for i in range(10):
    if i == 7:
        break
    print(i, end=" ")
print()

print("continue example — odd numbers only:")
for i in range(10):
    if i % 2 == 0:
        continue
    print(i, end=" ")
print()

# --- Nested loops: multiplication table ---
print("3x3 Multiplication Table:")
for row in range(1, 4):
    for col in range(1, 4):
        print(row * col, end="\t")
    print()
