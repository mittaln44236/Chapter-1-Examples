# Chapter-1-Examples
Examples of simple Java and Python programs
Please run the java files to see their output and add them to the First Project you started in Eclipse.

```java
public class FirstProgram {
   public static void main(String[] args) {
      System.out.println("Hello Pioneers!");
   }
}
```
A Java file has a class signature, typically declared as public, then the name of the class.
It is required that the name of the .java file matches the name in the class signature. 

A method in a Java file is similar to a function in a Python file. We have more specific modifiers in Java:
* public
* private
* protected

Most of the methods we make will be public. This allows the user to access and execute the methods. 
Private methods are also called *helper* methods that perform useful functions inside other methods.
Protected methods are used for classes that extend the current class. We will learn about **inheritance** later in the year. 

The method that is executable is the **main** method. Any of the commands in the main are executed

The main method takes a single parameter of a String array. Any of the commands in this method will be executed. 

Write a program called MyIntro.java which prints your name, your graduation year, and whether you are a boarder or day student. 

---

## Introductory Python Course

The `Python-Intro/` folder contains six self-contained lessons for students who are new to Python.

| Lesson | Topic | Files |
|--------|-------|-------|
| 1 | Variables & Data Types | [Lesson1-Variables.md](Python-Intro/Lesson1-Variables.md) · [lesson1_variables.py](Python-Intro/lesson1_variables.py) |
| 2 | Input & Output | [Lesson2-InputOutput.md](Python-Intro/Lesson2-InputOutput.md) · [lesson2_input_output.py](Python-Intro/lesson2_input_output.py) |
| 3 | Conditionals | [Lesson3-Conditionals.md](Python-Intro/Lesson3-Conditionals.md) · [lesson3_conditionals.py](Python-Intro/lesson3_conditionals.py) |
| 4 | Loops | [Lesson4-Loops.md](Python-Intro/Lesson4-Loops.md) · [lesson4_loops.py](Python-Intro/lesson4_loops.py) |
| 5 | Functions | [Lesson5-Functions.md](Python-Intro/Lesson5-Functions.md) · [lesson5_functions.py](Python-Intro/lesson5_functions.py) |
| 6 | Lists | [Lesson6-Lists.md](Python-Intro/Lesson6-Lists.md) · [lesson6_lists.py](Python-Intro/lesson6_lists.py) |

Each lesson markdown file explains the concept with examples and ends with practice exercises. The matching `.py` file contains all runnable code from that lesson.

Run any example file from the terminal:
```
python Python-Intro/lesson1_variables.py
```

