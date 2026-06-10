# Python VS Java

## Scripting vs Class Architecture
Java is strictly a class based language. This means:
* All methods (a.k.a. functions) are in a .java file referred to as a **class**.
* *Static* method can be accessed as if they are similar to library functions in Python
* Any other methods that are public can only be referenced from an **instance** of the class.
* The entire code is compiled **first**, before execution. This allows the compiler to check for possible run-time errors.

Python can be class based, but can also be a scripting language. This means:
* Functions can be in a library file or can be written dynamically.
* All variables are stored in the memory stack as objects
* Code is compiled as it is called, more run-time errors are possible.

Advantages to Python:
* Easy to write short programs.
* A wide variety of libraries for analysis and visualization.
* You don't need to assign data types to variables.

Advantages to Java:
* Easier to write full applications.
* A wide variety of libraries for analysis and visualization.
* You do need to assign data types to variables.
* Better data security for variables in a class.

## First Programs
### Python
In Python, the first program is usually a print statement in the Python environment.
```python
print("Hello Pioneers!")
```
If we put this into a Python file, we would have to write the command in a .py file and then from the terminal, we would type in 
<p>Windows</p>
```
C:\Users\Pioneer> python pyFile.py
```
<p>Linux / Mac</p>
```
Pioneer@Pioneer:~$ python pyFile.py
```
Then the Python compiler would turn the python code to bytecode and print the message to the screen.

If we want to adopt the structure of a Java program, we would write the command in a function and then call the function after it is closed
```python
def firstProgram():
   print("Hello Pioneers")

firstProgram()
```

Again we would execute the program by saving the file (pyFile.py) and then executing the file in the terminal using the ```python pyFile.py``` command.
