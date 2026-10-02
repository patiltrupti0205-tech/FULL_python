# ============================================================
# DAY 10 – PYTHON FUNCTIONS
# REMAINING TOPICS
# ============================================================

# ===========================================================
# 1. FUNCTION WITH MULTIPLE RETURN VALUES
# ============================================================

# A function can return more than one value.

def calculate(a, b):
    addition = a + b
    subtraction = a - b
    multiplication = a * b

    return addition, subtraction, multiplication


result = calculate(10, 5)

print("Addition:", result[0])
print("Subtraction:", result[1])
print("Multiplication:", result[2])


# We can also store returned values separately

add_result, sub_result, mul_result = calculate(20, 10)

print(add_result)
print(sub_result)
print(mul_result)


# ============================================================
# 2. FUNCTION WITH LIST
# ============================================================

# A list can be passed to a function.

def find_total(numbers):
    total = 0

    for number in numbers:
        total += number

    return total


numbers = [10, 20, 30, 40, 50]

print("Total:", find_total(numbers))


# ============================================================
# 3. FUNCTION WITH TUPLE
# ============================================================

def find_max(numbers):
    return max(numbers)


marks = (85, 90, 78, 95, 88)

print("Highest Marks:", find_max(marks))


# ============================================================
# 4. FUNCTION WITH DICTIONARY
# ============================================================

def display_student(student):
    print("Name:", student["name"])
    print("Age:", student["age"])
    print("Course:", student["course"])


student = {
    "name": "Trupti",
    "age": 20,
    "course": "B.Sc IT"
}

display_student(student)


# ============================================================
# 5. FUNCTION WITH SET
# ============================================================

def show_unique_numbers(numbers):
    unique_numbers = set(numbers)
    return unique_numbers


numbers = [1, 2, 2, 3, 4, 4, 5]

print("Unique Numbers:", show_unique_numbers(numbers))


# ============================================================
# 6. RECURSIVE FUNCTION
# ============================================================

# A function calling itself is called recursion.

def countdown(number):

    if number == 0:
        print("Done!")
    else:
        print(number)
        countdown(number - 1)


countdown(5)


# ============================================================
# 7. RECURSION – FACTORIAL
# ============================================================

def factorial(number):

    if number == 0 or number == 1:
        return 1

    return number * factorial(number - 1)


print("Factorial:", factorial(5))


# ============================================================
# 8. RECURSION – SUM OF NUMBERS
# ============================================================

def sum_numbers(number):

    if number == 0:
        return 0

    return number + sum_numbers(number - 1)


print("Sum:", sum_numbers(5))


# ============================================================
# 9. NESTED FUNCTION
# ============================================================

# A function inside another function is called
# a nested function.

def outer_function():

    print("This is outer function")

    def inner_function():
        print("This is inner function")

    inner_function()


outer_function()


# ============================================================
# 10. FUNCTION AS AN ARGUMENT
# ============================================================

# One function can be passed to another function.

def square(number):
    return number * number


def calculate(function, number):
    return function(number)


result = calculate(square, 5)

print("Result:", result)


# ============================================================
# 11. DOCSTRING
# ============================================================

# A docstring explains what a function does.

def greet(name):
    """
    This function prints a greeting message.
    """
    print("Hello", name)


print(greet.__doc__)

greet("Trupti")


# ============================================================
# 📝 PRACTICE QUESTIONS
# ============================================================

# Q1. Function that returns addition, subtraction
#     and multiplication of two numbers.

def calculate(a, b):
    addition = a + b
    subtraction = a - b
    multiplication = a * b

    return addition, subtraction, multiplication


result = calculate(10, 5)

print("Addition:", result[0])
print("Subtraction:", result[1])
print("Multiplication:", result[2])


# ============================================================
# Q2. Function that accepts a list
#     and returns total.
# ============================================================

def find_total(numbers):
    total = 0

    for number in numbers:
        total += number

    return total


numbers = [10, 20, 30, 40, 50]

print("Total:", find_total(numbers))


# ============================================================
# Q3. Function that accepts a tuple
#     and returns highest value.
# ============================================================

def find_max(numbers):
    return max(numbers)


marks = (85, 90, 78, 95, 88)

print("Highest Marks:", find_max(marks))


# ============================================================
# Q4. Function that accepts a dictionary
#     and prints student information.
# ============================================================

def display_student(student):
    print("Name:", student["name"])
    print("Age:", student["age"])
    print("Course:", student["course"])


student = {
    "name": "Trupti",
    "age": 20,
    "course": "B.Sc IT"
}

display_student(student)


# ============================================================
# Q5. Remove duplicate values from a list
#     using a set.
# ============================================================

def remove_duplicates(numbers):
    return set(numbers)


numbers = [1, 2, 2, 3, 4, 4, 5]

print("Original List:", numbers)
print("Unique Values:", remove_duplicates(numbers))


# ============================================================
# Q6. Recursive function to print
#     numbers from 1 to 10.
# ============================================================

def print_numbers(number):

    if number > 10:
        return

    print(number)

    print_numbers(number + 1)


print_numbers(1)


# ============================================================
# Q7. Recursive function to calculate factorial.
# ============================================================

def factorial(number):

    if number == 0 or number == 1:
        return 1

    return number * factorial(number - 1)


print("Factorial:", factorial(5))


# ============================================================
# Q8. Recursive function to calculate
#     sum of numbers from 1 to n.
# ============================================================

def sum_numbers(number):

    if number == 0:
        return 0

    return number + sum_numbers(number - 1)


print("Sum:", sum_numbers(5))


# ============================================================
# Q9. Create a nested function.
# ============================================================

def outer_function():

    print("This is outer function")

    def inner_function():
        print("This is inner function")

    inner_function()


outer_function()


# ============================================================
# Q10. Function with a docstring.
# ============================================================

def greet(name):
    """
    This function prints a greeting message.
    """

    print("Hello", name)


greet("Trupti")

print(greet.__doc__)


# ============================================================
# 🎯 MINI PROJECT – CALCULATOR USING FUNCTIONS
# ============================================================

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):

    if b == 0:
        return "Cannot divide by zero"

    return a / b


print("\n========== SIMPLE CALCULATOR ==========")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("\nChoose Operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = input("Enter your choice: ")


if choice == "1":

    result = add(num1, num2)
    print("Result:", result)


elif choice == "2":

    result = subtract(num1, num2)
    print("Result:", result)


elif choice == "3":

    result = multiply(num1, num2)
    print("Result:", result)


elif choice == "4":

    result = divide(num1, num2)
    print("Result:", result)


else:

    print("Invalid choice!")


print("========================================")

