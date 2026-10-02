# Day 7 - Python Tuples
# What is a Tuple?
# A tuple is used to store multiple items in a single variable.
# Tuples are ordered and cannot be changed after creation.

# Creating a Tuple

fruits = ("apple", "banana", "mango", "orange")

print(fruits)


# Accessing Tuple Items

print(fruits[0])
print(fruits[2])


# Negative Indexing

print(fruits[-1])
print(fruits[-2])


# Tuple Slicing

print(fruits[1:3])
print(fruits[:2])
print(fruits[2:])


# Length of Tuple

print(len(fruits))


# Check Item in Tuple

if "apple" in fruits:
    print("Apple is available")


# Loop Through a Tuple

for fruit in fruits:
    print(fruit)


# Tuple with Numbers

numbers = (10, 20, 30, 40, 50)

print(numbers)


# Count Method

marks = (80, 90, 80, 70, 80)

print(marks.count(80))


# Index Method

print(marks.index(90))


# Single Item Tuple

x = ("Python",)

print(x)


# Tuple Unpacking

student = ("Trupti", 20, "MSc IT")

name, age, course = student

print(name)
print(age)
print(course)


# Nested Tuple

data = (("Trupti", 20), ("Rahul", 21))

print(data[0])
print(data[0][0])


# List vs Tuple

# List -> []
# Tuple -> ()

# List can be changed
# Tuple cannot be changed

#Here are some quetions:

# 1. Create a tuple of 5 fruits and print it

fruits = ("apple", "banana", "mango", "orange", "grapes")

print(fruits)


# 2. Print the first and last item

print(fruits[0])
print(fruits[-1])


# 3. Print the tuple using slicing

print(fruits[1:4])


# 4. Find the length of the tuple

print(len(fruits))


# 5. Check whether "Python" exists in a tuple

languages = ("Java", "Python", "C++", "Dart")

if "Python" in languages:
    print("Python is available")
else:
    print("Python is not available")


# 6. Create a tuple of numbers and print each number using a loop

numbers = (10, 20, 30, 40, 50)

for number in numbers:
    print(number)


# 7. Count how many times 10 appears in a tuple

numbers = (10, 20, 10, 30, 10, 40)

print(numbers.count(10))


# 8. Find the index of a particular item

fruits = ("apple", "banana", "mango", "orange")

print(fruits.index("mango"))


# 9. Tuple Unpacking

student = ("Trupti", 20, "MSc IT")

name, age, course = student

print(name)
print(age)
print(course)


# 10. Create a nested tuple and access one inner value

students = (
    ("Trupti", 20),
    ("Rahul", 21),
    ("Priya", 22)
)

print(students[0][0])


# Student Result Manager

student = ("Trupti", 20, "MSc IT")
marks = (85, 78, 92, 88, 90)

# Student Information
name, age, course = student

print("===== STUDENT INFORMATION =====")
print("Name:", name)
print("Age:", age)
print("Course:", course)

# Marks
print("\n===== MARKS =====")

for mark in marks:
    print(mark)

# Total Marks
total = sum(marks)

print("\nTotal Marks:", total)

# Average Marks
average = total / len(marks)

print("Average Marks:", average)

# Highest Marks
print("Highest Marks:", max(marks))

# Lowest Marks
print("Lowest Marks:", min(marks))

# Check Result
if average >= 40:
    print("Result: PASS")
else:
    print("Result: FAIL")

# Subject Count
print("Total Subjects:", len(marks))