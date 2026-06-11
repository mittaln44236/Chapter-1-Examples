# Lesson 6: Lists

## What is a List?
A **list** is an ordered collection of items. Items can be of any type, and a list can even mix types (though it's best practice to keep them consistent).

```python
fruits    = ["apple", "banana", "cherry"]
scores    = [95, 87, 72, 100, 68]
mixed     = [1, "two", 3.0, True]
empty     = []
```

---

## Accessing Items — Indexing
List indices start at **0**.

```python
fruits = ["apple", "banana", "cherry"]
print(fruits[0])   # apple
print(fruits[2])   # cherry
print(fruits[-1])  # cherry  (last item, negative index)
```

---

## Slicing
Get a subset of the list with `[start:stop]` — `stop` is **excluded**.

```python
scores = [95, 87, 72, 100, 68]
print(scores[1:4])   # [87, 72, 100]
print(scores[:3])    # [95, 87, 72]
print(scores[2:])    # [72, 100, 68]
```

---

## Modifying a List
Lists are **mutable** — you can change them after creation.

```python
fruits = ["apple", "banana", "cherry"]
fruits[1] = "blueberry"          # replace
fruits.append("mango")           # add to end
fruits.insert(1, "avocado")      # insert at index 1
fruits.remove("apple")           # remove first occurrence
popped = fruits.pop()            # remove & return last item
```

---

## Useful List Methods and Functions

| Operation             | Example                          | Result / Effect           |
|-----------------------|----------------------------------|---------------------------|
| Length                | `len(scores)`                    | `5`                       |
| Sort (in place)       | `scores.sort()`                  | ascending order           |
| Reverse sort          | `scores.sort(reverse=True)`      | descending order          |
| Sorted copy           | `sorted(scores)`                 | new sorted list           |
| Sum                   | `sum(scores)`                    | total of all items        |
| Min / Max             | `min(scores)` / `max(scores)`    | smallest / largest        |
| Check membership      | `"apple" in fruits`              | `True` or `False`         |
| Index of item         | `fruits.index("cherry")`         | first matching index      |

---

## Iterating Over a List
```python
scores = [95, 87, 72, 100, 68]

# Access values
for score in scores:
    print(score)

# Access index and value together
for i, score in enumerate(scores):
    print(f"Student {i+1}: {score}")
```

---

## Building a List Dynamically
```python
squares = []
for n in range(1, 6):
    squares.append(n ** 2)
print(squares)   # [1, 4, 9, 16, 25]
```

### List Comprehension (Shortcut)
```python
squares = [n ** 2 for n in range(1, 6)]
print(squares)   # [1, 4, 9, 16, 25]
```

---

## Practice Exercises

1. Create a list of **five of your favorite movies**. Print:
   - The first and last movie.
   - All movies in alphabetical order.
   - The total count of movies in the list.

2. Ask the user to enter **five test scores** one at a time and store them in a list. Then print:
   - The **average** score.
   - The **highest** and **lowest** scores.
   - All scores that are **above the average**.

3. Write a function `remove_duplicates(lst)` that returns a new list with all duplicate values removed, keeping the original order. (Hint: build a new list and only add an item if it's not already there.)

---
*Previous: [Lesson 5 — Functions](Lesson5-Functions.md)*
