# ============================================================
# 🐍 DAY 16 – ADVANCED DICTIONARIES
# ============================================================

# ------------------------------------------------------------
# 1️⃣ DICTIONARY BASICS
# ------------------------------------------------------------

student = {
    "name": "Trupti",
    "age": 20,
    "course": "B.Sc IT"
}

print(student)


# ------------------------------------------------------------
# 2️⃣ ACCESS VALUES
# ------------------------------------------------------------

print(student["name"])
print(student["course"])

# get() is safer
print(student.get("name"))
print(student.get("city", "Not Available"))


# ------------------------------------------------------------
# 3️⃣ ADD / UPDATE VALUE
# ------------------------------------------------------------

student["city"] = "Surat"
student["age"] = 21

print(student)


# ------------------------------------------------------------
# 4️⃣ DICTIONARY METHODS
# ------------------------------------------------------------

print(student.keys())
print(student.values())
print(student.items())

# Remove one item
student.pop("city")

print(student)

# Remove last item
student.popitem()

print(student)


# ------------------------------------------------------------
# 5️⃣ LOOP THROUGH DICTIONARY
# ------------------------------------------------------------

student = {
    "name": "Trupti",
    "age": 20,
    "course": "B.Sc IT"
}

# Only keys
for key in student:
    print(key)

# Keys + values
for key, value in student.items():
    print(key, ":", value)


# ------------------------------------------------------------
# 6️⃣ NESTED DICTIONARY
# ------------------------------------------------------------

students = {
    "student1": {
        "name": "Trupti",
        "age": 20,
        "marks": 85
    },

    "student2": {
        "name": "Nensi",
        "age": 21,
        "marks": 78
    }
}

print(students)

print(students["student1"]["name"])
print(students["student2"]["marks"])


# ------------------------------------------------------------
# 7️⃣ LOOP THROUGH NESTED DICTIONARY
# ------------------------------------------------------------

for student_id, data in students.items():

    print("\nID:", student_id)
    print("Name:", data["name"])
    print("Age:", data["age"])
    print("Marks:", data["marks"])


# ------------------------------------------------------------
# 8️⃣ DICTIONARY COMPREHENSION
# ------------------------------------------------------------

numbers = [1, 2, 3, 4, 5]

squares = {x: x * x for x in numbers}

print(squares)

# Output:
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}


# ------------------------------------------------------------
# 9️⃣ DICTIONARY COMPREHENSION WITH CONDITION
# ------------------------------------------------------------

numbers = [10, 15, 20, 25, 30]

even_numbers = {
    x: x * x
    for x in numbers
    if x % 2 == 0
}

print(even_numbers)


# ------------------------------------------------------------
# 🔟 CONVERT TWO LISTS INTO DICTIONARY
# ------------------------------------------------------------

names = ["Trupti", "Nensi", "Riya"]
marks = [85, 78, 92]

result = dict(zip(names, marks))

print(result)


# ------------------------------------------------------------
# 1️⃣1️⃣ FIND MAXIMUM VALUE
# ------------------------------------------------------------

marks = {
    "Trupti": 85,
    "Nensi": 78,
    "Riya": 92,
    "Priya": 88
}

highest = max(marks.values())

print("Highest Marks:", highest)


# Find student with highest marks
top_student = max(marks, key=marks.get)

print("Top Student:", top_student)


# ------------------------------------------------------------
# 1️⃣2️⃣ FIND MINIMUM VALUE
# ------------------------------------------------------------

lowest = min(marks.values())

print("Lowest Marks:", lowest)

lowest_student = min(marks, key=marks.get)

print("Lowest Student:", lowest_student)


# ------------------------------------------------------------
# 1️⃣3️⃣ SORT DICTIONARY BY VALUES
# ------------------------------------------------------------

marks = {
    "Trupti": 85,
    "Nensi": 78,
    "Riya": 92,
    "Priya": 88
}

# Ascending
ascending = dict(sorted(marks.items(), key=lambda x: x[1]))

print("Ascending:", ascending)

# Descending
descending = dict(
    sorted(marks.items(), key=lambda x: x[1], reverse=True)
)

print("Descending:", descending)


# ------------------------------------------------------------
# 1️⃣4️⃣ UPDATE DICTIONARY
# ------------------------------------------------------------

student = {
    "name": "Trupti",
    "age": 20
}

student.update({
    "course": "B.Sc IT",
    "city": "Surat"
})

print(student)


# ============================================================
# 📝 PRACTICE QUESTIONS + ANSWERS
# ============================================================

# Q1. Create a dictionary containing name, age and city.

person = {
    "name": "Trupti",
    "age": 20,
    "city": "Surat"
}

print(person)


# Q2. Print only dictionary keys.

for key in person.keys():
    print(key)


# Q3. Print only dictionary values.

for value in person.values():
    print(value)


# Q4. Add "course": "B.Sc IT".

person["course"] = "B.Sc IT"

print(person)


# Q5. Create a dictionary of 5 students and marks.

marks = {
    "Trupti": 85,
    "Nensi": 78,
    "Riya": 92,
    "Priya": 88,
    "Komal": 75
}

print(marks)


# Q6. Find highest marks.

highest = max(marks.values())

print("Highest:", highest)


# Q7. Find student who got highest marks.

student = max(marks, key=marks.get)

print("Top Student:", student)


# Q8. Sort marks in ascending order.

ascending = dict(
    sorted(marks.items(), key=lambda x: x[1])
)

print(ascending)


# Q9. Sort marks in descending order.

descending = dict(
    sorted(marks.items(), key=lambda x: x[1], reverse=True)
)

print(descending)


# Q10. Create squares dictionary from 1 to 10.

squares = {
    x: x * x
    for x in range(1, 11)
}

print(squares)


# Q11. Create dictionary containing only even numbers.

even = {
    x: x
    for x in range(1, 11)
    if x % 2 == 0
}

print(even)


# Q12. Convert two lists into dictionary.

names = ["A", "B", "C"]
marks = [80, 90, 70]

result = dict(zip(names, marks))

print(result)


# Q13. Create a nested dictionary of 2 students.

students = {
    "student1": {
        "name": "Trupti",
        "marks": 85
    },

    "student2": {
        "name": "Riya",
        "marks": 92
    }
}

print(students)


# Q14. Print all student names.

for data in students.values():
    print(data["name"])


# Q15. Print students who scored more than 80.

for name, mark in marks.items():

    if mark > 80:
        print(name, mark)


# ============================================================
# 🚀 MINI PROJECT – STUDENT RESULT SYSTEM
# ============================================================

students = {}

n = int(input("Enter number of students: "))

for i in range(n):

    name = input("\nEnter student name: ")

    marks1 = float(input("Enter Python marks: "))
    marks2 = float(input("Enter Cloud marks: "))
    marks3 = float(input("Enter Database marks: "))

    total = marks1 + marks2 + marks3
    average = total / 3

    students[name] = {
        "Python": marks1,
        "Cloud": marks2,
        "Database": marks3,
        "Total": total,
        "Average": average
    }


# ------------------------------------------------------------
# Display Result
# ------------------------------------------------------------

print("\n========== STUDENT RESULTS ==========")

for name, data in students.items():

    print("\nName:", name)
    print("Python:", data["Python"])
    print("Cloud:", data["Cloud"])
    print("Database:", data["Database"])
    print("Total:", data["Total"])
    print("Average:", round(data["Average"], 2))


# ------------------------------------------------------------
# Find Top Student
# ------------------------------------------------------------

top_student = max(
    students,
    key=lambda name: students[name]["Average"]
)

print("\n🏆 Top Student:", top_student)

print(
    "Highest Average:",
    round(students[top_student]["Average"], 2)
)


# ------------------------------------------------------------
# Find Lowest Student
# ------------------------------------------------------------

lowest_student = min(
    students,
    key=lambda name: students[name]["Average"]
)

print("Lowest Student:", lowest_student)

print(
    "Lowest Average:",
    round(students[lowest_student]["Average"], 2)
)


