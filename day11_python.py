# ============================================================
# DAY 11 – PYTHON MODULES & PACKAGES
# ============================================================

# ============================================================
# 1. WHAT IS A MODULE?
# ============================================================

# A module is a Python file containing code,
# functions, variables, classes, etc.

# Example:
# math.py is a built-in Python module.


# ============================================================
# 2. IMPORT A MODULE
# ============================================================

import math

print(math.sqrt(25))
print(math.pi)


# ============================================================
# 3. USING DIFFERENT FUNCTIONS FROM math
# ============================================================

print("Square root:", math.sqrt(16))
print("Power:", math.pow(2, 3))
print("Ceiling:", math.ceil(4.2))
print("Floor:", math.floor(4.8))


# ============================================================
# 4. IMPORT MODULE WITH ALIAS
# ============================================================

# 'as' gives a short name to the module.

import math as m

print("Square root:", m.sqrt(36))
print("PI:", m.pi)


# ============================================================
# 5. FROM MODULE IMPORT
# ============================================================

# We can import only a specific function.

from math import sqrt

print("Square root:", sqrt(49))


# ============================================================
# 6. IMPORT MULTIPLE FUNCTIONS
# ============================================================

from math import sqrt, pow

print("Square root:", sqrt(64))
print("Power:", pow(2, 4))


# ============================================================
# 7. RANDOM MODULE
# ============================================================

import random

print("Random number:", random.randint(1, 10))


# Random number between 1 and 100

number = random.randint(1, 100)

print("Random number:", number)


# ============================================================
# 8. RANDOM CHOICE
# ============================================================

fruits = ["Apple", "Mango", "Banana", "Orange"]

print("Random fruit:", random.choice(fruits))


# ============================================================
# 9. RANDOM FLOAT
# ============================================================

print("Random decimal:", random.random())


# ============================================================
# 10. DATETIME MODULE
# ============================================================

import datetime

today = datetime.date.today()

print("Today's date:", today)


# Current date and time

now = datetime.datetime.now()

print("Current date and time:", now)


# ============================================================
# 11. OS MODULE
# ============================================================

import os

print("Current folder:")
print(os.getcwd())


# ============================================================
# 12. LIST FILES IN CURRENT FOLDER
# ============================================================

print("Files and folders:")

print(os.listdir())


# ============================================================
# 13. SYS MODULE
# ============================================================

import sys

print("Python version:")
print(sys.version)


# ============================================================
# 14. CREATE YOUR OWN MODULE
# ============================================================

# We can create our own Python file.
#
# Example:
#
# calculator.py
#
# def add(a, b):
#     return a + b
#
# def subtract(a, b):
#     return a - b
#
# Then another Python file can use:
#
# import calculator
#
# print(calculator.add(10, 20))
# print(calculator.subtract(20, 5))


# ============================================================
# 15. EXAMPLE OF OWN MODULE
# ============================================================

# Create a file named:
# mymodule.py
#
# Put this code inside it:
#
# def greet(name):
#     print("Hello", name)
#
# def square(number):
#     return number * number
#
# Then in another file:
#
# import mymodule
#
# mymodule.greet("Trupti")
# print(mymodule.square(5))


# ============================================================
# 16. __name__ == "__main__"
# ============================================================

# This is commonly used in Python modules.
#
# Code inside this block runs when the file
# is directly executed.


def welcome():
    print("Welcome to Python!")


if __name__ == "__main__":
    welcome()


# ============================================================
# 17. WHAT IS A PACKAGE?
# ============================================================

# A package is a folder containing Python modules.
#
# Example:
#
# mypackage/
#     __init__.py
#     calculator.py
#     student.py
#
# We can import modules from the package.


# ============================================================
# 📝 PRACTICE QUESTIONS
# ============================================================

# ==========================================
# DAY 11 – PRACTICE QUESTIONS ANSWERS
# PYTHON MODULES & PACKAGES
# ==========================================


# Q1. Use math module to find square root of 144

import math

print(math.sqrt(144))


# ------------------------------------------
# Q2. Find the value of pi using math module
# ------------------------------------------

import math

print(math.pi)


# ------------------------------------------
# Q3. Use math module to find:
# square root of 81
# power of 2^5
# ceiling of 4.3
# floor of 7.9
# ------------------------------------------

import math

print("Square Root:", math.sqrt(81))
print("Power:", math.pow(2, 5))
print("Ceiling:", math.ceil(4.3))
print("Floor:", math.floor(7.9))


# ------------------------------------------
# Q4. Use alias 'm' for math module
# and find square root of 100
# ------------------------------------------

import math as m

print(m.sqrt(100))


# ------------------------------------------
# Q5. Import only sqrt from math module
# and find square root of 225
# ------------------------------------------

from math import sqrt

print(sqrt(225))


# ------------------------------------------
# Q6. Generate a random number between
# 1 and 50
# ------------------------------------------

import random

number = random.randint(1, 50)

print("Random Number:", number)


# ------------------------------------------
# Q7. Select a random fruit from a list
# ------------------------------------------

import random

fruits = ["Apple", "Mango", "Banana", "Orange", "Grapes"]

fruit = random.choice(fruits)

print("Random Fruit:", fruit)


# ------------------------------------------
# Q8. Print today's date
# ------------------------------------------

import datetime

today = datetime.date.today()

print("Today's Date:", today)


# ------------------------------------------
# Q9. Print current date and time
# ------------------------------------------

import datetime

now = datetime.datetime.now()

print("Current Date and Time:", now)


# ------------------------------------------
# Q10. Print current working directory
# ------------------------------------------

import os

print("Current Folder:", os.getcwd())


# ==========================================
# MINI PRACTICE
# RANDOM NUMBER GAME
# ==========================================

import random

secret_number = random.randint(1, 10)

guess = int(input("Guess a number between 1 and 10: "))

if guess == secret_number:
    print("Correct! You guessed the number.")
else:
    print("Wrong!")
    print("The correct number was:", secret_number)


# ==========================================
# EXTRA PRACTICE
# ==========================================

# Generate 5 random numbers

import random

for i in range(5):
    number = random.randint(1, 100)
    print(number)


# ------------------------------------------
# Random student selection
# ------------------------------------------

import random

students = ["Trupti", "Nensi", "Riya", "Priya", "Aisha"]

selected_student = random.choice(students)

print("Selected Student:", selected_student)


# ------------------------------------------
# Find square root using imported function
# ------------------------------------------

from math import sqrt

number = int(input("Enter a number: "))

print("Square Root:", sqrt(number))

# ============================================================
# 🎯 MINI PROJECT – RANDOM NUMBER GUESSING GAME
# ============================================================

import random

secret_number = random.randint(1, 10)

print("\n================================")
print("🎯 NUMBER GUESSING GAME")
print("================================")

guess = int(input("Guess a number between 1 and 10: "))


if guess == secret_number:

    print("🎉 Correct! You guessed the number.")

elif guess < secret_number:

    print("Too low!")
    print("The number was:", secret_number)

else:

    print("Too high!")
    print("The number was:", secret_number)


print("================================")

