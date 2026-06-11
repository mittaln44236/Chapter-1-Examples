# Lesson 6 Examples: Lists

# --- Creating and accessing lists ---
fruits = ["apple", "banana", "cherry"]
print(fruits[0])    # apple
print(fruits[-1])   # cherry (last item)

# --- Slicing ---
scores = [95, 87, 72, 100, 68]
print(scores[1:4])   # [87, 72, 100]
print(scores[:3])    # [95, 87, 72]

# --- Modifying a list ---
fruits.append("mango")
fruits.insert(1, "avocado")
fruits.remove("apple")
print(fruits)

# --- Useful functions ---
print(len(scores))       # 5
print(sum(scores))       # 422
print(min(scores))       # 68
print(max(scores))       # 100
print(sorted(scores))    # [68, 72, 87, 95, 100]

# --- Iterating ---
print("All scores:")
for score in scores:
    print(score)

print("Numbered list:")
for i, score in enumerate(scores):
    print(f"Student {i+1}: {score}")

# --- Building a list dynamically ---
squares = []
for n in range(1, 6):
    squares.append(n ** 2)
print("Squares:", squares)

# List comprehension version
squares = [n ** 2 for n in range(1, 6)]
print("Squares (comprehension):", squares)

# --- Collecting user input into a list ---
test_scores = []
for i in range(5):
    s = float(input(f"Enter score {i+1}: "))
    test_scores.append(s)

average = sum(test_scores) / len(test_scores)
print(f"Average: {average:.1f}")
print(f"Highest: {max(test_scores)}")
print(f"Lowest:  {min(test_scores)}")
print("Above average:", [s for s in test_scores if s > average])
