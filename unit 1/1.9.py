#Write a program to define and use user-defined
#functions with different types of arguments.

# User-defined functions

# No argument
def greet():
    print("Hello")
greet()

# Positional arguments
def add(a, b):
    print("Addition:", a + b)
add(10, 20)

# Default argument
def welcome(name="Student"):
    print("Welcome", name)
welcome()
welcome("Yuvraj")

# Keyword arguments
def student(name, age):
    print("Name:", name)
    print("Age:", age)
student(age=21, name="Yuvraj")

