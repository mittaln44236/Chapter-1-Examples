# Lesson 4: Loops

## Why Use Loops?
Loops let you repeat a block of code without copy-pasting it. Python has two kinds: `for` loops and `while` loops.

---

## The `for` Loop
A `for` loop iterates over a **sequence** (like a range of numbers or a list).

### Looping with `range()`
```python
for i in range(5):
    print(i)
# Prints: 0 1 2 3 4  (one per line)
```

`range(start, stop, step)` — `stop` is **excluded**.

```python
for i in range(1, 11):        # 1 through 10
    print(i)

for i in range(0, 20, 2):     # even numbers 0–18
    print(i)

for i in range(10, 0, -1):    # count down from 10 to 1
    print(i)
```

### Looping Over a String
```python
word = "Pioneer"
for letter in word:
    print(letter)
```

---

## The `while` Loop
A `while` loop runs **as long as** a condition is `True`.

```python
count = 1
while count <= 5:
    print(count)
    count += 1     # same as count = count + 1
```

> **Warning:** If the condition never becomes `False`, you get an **infinite loop**. Always make sure something inside the loop moves toward making the condition `False`.

### Input Validation with `while`
`while` loops are great for asking the user to re-enter invalid data.

```python
age = int(input("Enter your age (1-120): "))
while age < 1 or age > 120:
    print("Invalid age. Please try again.")
    age = int(input("Enter your age (1-120): "))
print(f"Your age is {age}.")
```

---

## `break` and `continue`
- `break` — exits the loop immediately.
- `continue` — skips the rest of the current iteration and moves to the next one.

```python
for i in range(10):
    if i == 7:
        break         # stop at 7
    print(i)

for i in range(10):
    if i % 2 == 0:
        continue      # skip even numbers
    print(i)          # prints only odd numbers
```

---

## Nested Loops
A loop inside another loop.

```python
for row in range(1, 4):
    for col in range(1, 4):
        print(row * col, end="\t")
    print()   # new line after each row
```

---

## Practice Exercises

1. Print every **odd** number from 1 to 99 using a `for` loop.

2. Write a program that asks the user to guess a secret number (pick one and store it in a variable). Keep asking until they guess correctly, then print how many guesses it took.

3. Print a right-triangle pattern of `*` characters with 5 rows:
   ```
   *
   **
   ***
   ****
   *****
   ```

---
*Previous: [Lesson 3 — Conditionals](Lesson3-Conditionals.md)*  
*Next: [Lesson 5 — Functions](Lesson5-Functions.md)*
