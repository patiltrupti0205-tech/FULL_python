# Day 8 - Python Dictionaries

# What is a Dictionary?
# A dictionary is used to store multiple items in key-value pairs.
# Dictionaries are ordered and changeable.
# Dictionary is written using curly brackets {}.


# Creating a Dictionary

student = {
    "name": "Trupti",
    "age": 20,
    "course": "MSc IT"
}

print(student)


# Accessing Dictionary Values

print(student["name"])
print(student["age"])
print(student["course"])


# Using get() Method

print(student.get("name"))
print(student.get("course"))


# Adding a New Item

student["city"] = "Surat"

print(student)


# Changing a Value

student["age"] = 21

print(student)


# Removing an Item

student.pop("city")

print(student)


# Check if Key Exists

if "name" in student:
    print("Name is available")


# Length of Dictionary

print(len(student))


# Dictionary Keys

print(student.keys())


# Dictionary Values

print(student.values())


# Dictionary Items

print(student.items())


# Loop Through Dictionary

for key in student:
    print(key)


# Loop Through Dictionary Values

for value in student.values():
    print(value)


# Loop Through Keys and Values

for key, value in student.items():
    print(key, ":", value)


# Dictionary with Numbers

marks = {
    "Python": 85,
    "Java": 78,
    "Cloud Computing": 92,
    "Database": 88,
    "Cyber Security": 90
}

print(marks)


# Total Marks

total = sum(marks.values())

print("Total Marks:", total)


# Highest Marks

print("Highest Marks:", max(marks.values()))


# Lowest Marks

print("Lowest Marks:", min(marks.values()))


# Here are some questions:


# 1. Create a dictionary of 5 fruits and their prices

fruits = {
    "apple": 100,
    "banana": 50,
    "mango": 80,
    "orange": 60,
    "grapes": 90
}

print(fruits)


# 2. Print the price of apple

print(fruits["apple"])


# 3. Add a new fruit

fruits["watermelon"] = 70

print(fruits)


# 4. Change the price of banana

fruits["banana"] = 60

print(fruits)


# 5. Check whether mango exists in the dictionary

if "mango" in fruits:
    print("Mango is available")
else:
    print("Mango is not available")


# 6. Print all fruits using a loop

for fruit in fruits:
    print(fruit)


# 7. Print all prices using a loop

for price in fruits.values():
    print(price)


# 8. Print fruits and prices using a loop

for fruit, price in fruits.items():
    print(fruit, ":", price)


# 9. Create a dictionary of subjects and marks

marks = {
    "Python": 85,
    "Java": 78,
    "Cloud Computing": 92,
    "Database": 88,
    "Cyber Security": 90
}

print(marks)


# 10. Find the total marks

print("Total Marks:", sum(marks.values()))


# Student Information Manager

student = {
    "name": "Trupti",
    "age": 20,
    "course": "MSc IT",
    "city": "Surat"
}

marks = {
    "Python": 85,
    "Java": 78,
    "Cloud Computing": 92,
    "Database": 88,
    "Cyber Security": 90
}


# Student Information

print("===== STUDENT INFORMATION =====")

print("Name:", student["name"])
print("Age:", student["age"])
print("Course:", student["course"])
print("City:", student["city"])


# Marks

print("\n===== MARKS =====")

for subject, mark in marks.items():
    print(subject, ":", mark)


# Total Marks

total = sum(marks.values())

print("\nTotal Marks:", total)


# Average Marks

average = total / len(marks)

print("Average Marks:", average)


# Highest Marks

print("Highest Marks:", max(marks.values()))


# Lowest Marks

print("Lowest Marks:", min(marks.values()))


# Check Result

if average >= 40:
    print("Result: PASS")
else:
    print("Result: FAIL")


# Subject Count

print("Total Subjects:", len(marks))


# ==========================================================
# MINI PROJECT - STUDENT MARKS MANAGER
# ==========================================================

# Create a student information dictionary

student = {
    "name": "Trupti",
    "age": 20,
    "course": "MSc IT",
    "city": "Surat"
}


# Create a marks dictionary

marks = {
    "Python": 85,
    "Java": 78,
    "Cloud Computing": 92,
    "Database": 88,
    "Cyber Security": 90
}


# Student Information

print("===== STUDENT INFORMATION =====")

print("Name:", student["name"])
print("Age:", student["age"])
print("Course:", student["course"])
print("City:", student["city"])


# Display Marks

print("\n===== SUBJECT MARKS =====")

for subject, mark in marks.items():
    print(subject, ":", mark)


# Calculate Total Marks

total = sum(marks.values())

print("\nTotal Marks:", total)


# Calculate Average Marks

average = total / len(marks)

print("Average Marks:", average)


# Highest Marks

highest = max(marks.values())

print("Highest Marks:", highest)


# Lowest Marks

lowest = min(marks.values())

print("Lowest Marks:", lowest)


# Number of Subjects

subjects = len(marks)

print("Total Subjects:", subjects)


# Check Result

if average >= 40:
    print("Result: PASS")
else:
    print("Result: FAIL")


# Check Grade

if average >= 90:
    print("Grade: A+")
elif average >= 80:
    print("Grade: A")
elif average >= 70:
    print("Grade: B")
elif average >= 60:
    print("Grade: C")
elif average >= 40:
    print("Grade: D")
else:
    print("Grade: F")

