# ============================================================
# DAY 22 – JSON IN PYTHON
# ============================================================

import json


# ------------------------------------------------------------
# 1. JSON KYA HAI?
# ------------------------------------------------------------

# JSON = JavaScript Object Notation
# Data ko store aur exchange karne ke liye use hota hai.

# Example JSON:
# {
#     "name": "Trupti",
#     "age": 20,
#     "course": "BSc IT"
# }


# ------------------------------------------------------------
# 2. Python Dictionary → JSON String
# ------------------------------------------------------------

student = {
    "name": "Trupti",
    "age": 20,
    "course": "BSc IT"
}

json_data = json.dumps(student)

print(json_data)
print(type(json_data))


# ------------------------------------------------------------
# 3. JSON String → Python Dictionary
# ------------------------------------------------------------

json_string = '{"name": "Trupti", "age": 20, "course": "BSc IT"}'

student_data = json.loads(json_string)

print(student_data)
print(type(student_data))

print(student_data["name"])


# ------------------------------------------------------------
# 4. dumps() with indent
# ------------------------------------------------------------

student = {
    "name": "Trupti",
    "age": 20,
    "skills": ["Python", "Cloud", "Git"]
}

json_data = json.dumps(student, indent=4)

print(json_data)


# ------------------------------------------------------------
# 5. Python List → JSON
# ------------------------------------------------------------

names = ["Trupti", "Nisha", "Priya"]

json_names = json.dumps(names)

print(json_names)


# ------------------------------------------------------------
# 6. JSON → Python List
# ------------------------------------------------------------

json_names = '["Trupti", "Nisha", "Priya"]'

names = json.loads(json_names)

print(names)
print(names[0])


# ------------------------------------------------------------
# 7. Python Data Types and JSON
# ------------------------------------------------------------

data = {
    "name": "Trupti",       # string
    "age": 20,              # integer
    "marks": 85.5,          # float
    "passed": True,         # boolean
    "skills": ["Python"],   # list
    "extra": None           # None
}

print(json.dumps(data, indent=4))


# ------------------------------------------------------------
# 8. WRITE JSON FILE – json.dump()
# ------------------------------------------------------------

student = {
    "name": "Trupti",
    "course": "BSc IT",
    "year": 3,
    "marks": 85
}

with open("student.json", "w") as file:
    json.dump(student, file, indent=4)

print("JSON file created!")


# ------------------------------------------------------------
# 9. READ JSON FILE – json.load()
# ------------------------------------------------------------

with open("student.json", "r") as file:
    data = json.load(file)

print(data)

print("Name:", data["name"])
print("Course:", data["course"])
print("Marks:", data["marks"])


# ------------------------------------------------------------
# 10. UPDATE JSON DATA
# ------------------------------------------------------------

with open("student.json", "r") as file:
    data = json.load(file)

data["marks"] = 90
data["skills"] = ["Python", "Cloud Computing", "Git"]

with open("student.json", "w") as file:
    json.dump(data, file, indent=4)

print("Data updated!")


# ------------------------------------------------------------
# 11. NESTED JSON
# ------------------------------------------------------------

student = {
    "name": "Trupti",
    "course": "BSc IT",
    "address": {
        "city": "Surat",
        "state": "Gujarat"
    },
    "skills": [
        "Python",
        "Cloud Computing",
        "Git"
    ]
}

print(student["address"]["city"])
print(student["skills"][0])


# ------------------------------------------------------------
# 12. LOOP THROUGH JSON
# ------------------------------------------------------------

student = {
    "name": "Trupti",
    "age": 20,
    "course": "BSc IT"
}

for key, value in student.items():
    print(key, ":", value)


# ------------------------------------------------------------
# 13. LIST OF STUDENTS
# ------------------------------------------------------------

students = [
    {
        "name": "Trupti",
        "marks": 85
    },
    {
        "name": "Nisha",
        "marks": 92
    },
    {
        "name": "Priya",
        "marks": 78
    }
]

for student in students:
    print(student["name"], student["marks"])


# ------------------------------------------------------------
# 14. FIND TOP STUDENT
# ------------------------------------------------------------

students = [
    {"name": "Trupti", "marks": 85},
    {"name": "Nisha", "marks": 92},
    {"name": "Priya", "marks": 78}
]

top_student = max(students, key=lambda x: x["marks"])

print("Top Student:", top_student["name"])
print("Marks:", top_student["marks"])


# ============================================================
# 📝 PRACTICE QUESTIONS + ANSWERS
# ============================================================

# Q1. Create a dictionary and convert it into JSON.

student = {
    "name": "Trupti",
    "age": 20
}

print(json.dumps(student))


# Q2. Convert this JSON string into Python dictionary.

data = '{"name": "Trupti", "course": "BSc IT"}'

result = json.loads(data)

print(result)


# Q3. Print only the name.

print(result["name"])


# Q4. Create a JSON file called employee.json.

employee = {
    "name": "Rahul",
    "salary": 30000,
    "department": "IT"
}

with open("employee.json", "w") as file:
    json.dump(employee, file, indent=4)

print("Employee file created!")


# Q5. Read employee.json.

with open("employee.json", "r") as file:
    employee_data = json.load(file)

print(employee_data)


# Q6. Change salary to 40000.

employee_data["salary"] = 40000

with open("employee.json", "w") as file:
    json.dump(employee_data, file, indent=4)

print("Salary updated!")


# Q7. Create nested JSON.

person = {
    "name": "Trupti",
    "contact": {
        "email": "trupti@gmail.com",
        "city": "Surat"
    }
}

print(json.dumps(person, indent=4))


# Q8. Print city.

print(person["contact"]["city"])


# Q9. Create 3 students in a list and print their names.

students = [
    {"name": "A", "marks": 80},
    {"name": "B", "marks": 90},
    {"name": "C", "marks": 75}
]

for student in students:
    print(student["name"])


# Q10. Find student with highest marks.

top = max(students, key=lambda x: x["marks"])

print("Highest:", top["name"])
print("Marks:", top["marks"])


# ============================================================
# 🚀 MINI PROJECT – STUDENT JSON MANAGEMENT SYSTEM
# ============================================================

students = []

# Add students
students.append({
    "name": "Trupti",
    "course": "BSc IT",
    "marks": 85
})

students.append({
    "name": "Nisha",
    "course": "BSc IT",
    "marks": 92
})

students.append({
    "name": "Priya",
    "course": "BSc IT",
    "marks": 78
})


# Save students into JSON file
with open("students.json", "w") as file:
    json.dump(students, file, indent=4)

print("Students saved successfully!")


# Read students from JSON file
with open("students.json", "r") as file:
    students = json.load(file)


# Display students
print("\n--- STUDENT LIST ---")

for student in students:
    print(
        "Name:", student["name"],
        "| Course:", student["course"],
        "| Marks:", student["marks"]
    )


# Find highest marks
top_student = max(students, key=lambda x: x["marks"])

print("\n--- TOP STUDENT ---")
print("Name:", top_student["name"])
print("Marks:", top_student["marks"])


# Average marks
total = sum(student["marks"] for student in students)

average = total / len(students)

print("\nAverage Marks:", average)


# ============================================================
# ⭐ IMPORTANT INTERVIEW QUESTIONS
# ============================================================

# 1. What is JSON?
# JSON is a lightweight format used to store and exchange data.

# 2. Which module is used for JSON in Python?
# json

# 3. What is json.dumps()?
# Python object → JSON string

# 4. What is json.loads()?
# JSON string → Python object

# 5. What is json.dump()?
# Python object → JSON file

# 6. What is json.load()?
# JSON file → Python object

# 7. What is the difference between dump and dumps?
# dump  = works with file
# dumps = creates string

# 8. What is the difference between load and loads?
# load  = reads from file
# loads = reads from string

