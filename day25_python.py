# ============================================================
#  DAY 25 – PYTHON + SQLITE DATABASE
# ============================================================

import sqlite3


# ------------------------------------------------------------
# 1. DATABASE SE CONNECT KARNA
# ------------------------------------------------------------

# students.db naam ki database file banegi
# Agar file already hai to usi database se connect hoga.

connection = sqlite3.connect("students.db")

print("Database connected!")


# ------------------------------------------------------------
# 2. CURSOR
# ------------------------------------------------------------

cursor = connection.cursor()

# Cursor database ke saath commands execute karta hai.


# ------------------------------------------------------------
# 3. TABLE CREATE KARNA
# ------------------------------------------------------------

cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    age INTEGER,
    course TEXT,
    marks REAL
)
""")

connection.commit()

print("Table created!")


# ------------------------------------------------------------
# 4. INSERT DATA
# ------------------------------------------------------------

cursor.execute("""
INSERT INTO students (name, age, course, marks)
VALUES (?, ?, ?, ?)
""", ("Trupti", 20, "BSc IT", 85))

connection.commit()

print("Student added!")


# ------------------------------------------------------------
# 5. INSERT MULTIPLE STUDENTS
# ------------------------------------------------------------

students = [
    ("Nisha", 20, "BSc IT", 92),
    ("Priya", 21, "BSc IT", 78),
    ("Riya", 20, "BCA", 88)
]

cursor.executemany("""
INSERT INTO students (name, age, course, marks)
VALUES (?, ?, ?, ?)
""", students)

connection.commit()

print("Multiple students added!")


# ------------------------------------------------------------
# 6. READ ALL DATA
# ------------------------------------------------------------

cursor.execute("SELECT * FROM students")

rows = cursor.fetchall()

print("\n----- ALL STUDENTS -----")

for row in rows:
    print(row)


# ------------------------------------------------------------
# 7. READ SPECIFIC COLUMNS
# ------------------------------------------------------------

cursor.execute("SELECT name, marks FROM students")

rows = cursor.fetchall()

for row in rows:
    print("Name:", row[0], "Marks:", row[1])


# ------------------------------------------------------------
# 8. SEARCH STUDENT
# ------------------------------------------------------------

name = "Trupti"

cursor.execute(
    "SELECT * FROM students WHERE name = ?",
    (name,)
)

student = cursor.fetchone()

print("\nSearch Result:")

if student:
    print(student)
else:
    print("Student not found!")


# ------------------------------------------------------------
# 9. WHERE CONDITION
# ------------------------------------------------------------

cursor.execute(
    "SELECT * FROM students WHERE marks >= ?",
    (80,)
)

students = cursor.fetchall()

print("\nStudents with marks >= 80:")

for student in students:
    print(student)


# ------------------------------------------------------------
# 10. UPDATE DATA
# ------------------------------------------------------------

cursor.execute("""
UPDATE students
SET marks = ?
WHERE name = ?
""", (95, "Trupti"))

connection.commit()

print("\nMarks updated!")


# ------------------------------------------------------------
# 11. DELETE DATA
# ------------------------------------------------------------

cursor.execute(
    "DELETE FROM students WHERE name = ?",
    ("Riya",)
)

connection.commit()

print("Student deleted!")


# ------------------------------------------------------------
# 12. COUNT STUDENTS
# ------------------------------------------------------------

cursor.execute("SELECT COUNT(*) FROM students")

count = cursor.fetchone()[0]

print("\nTotal students:", count)


# ------------------------------------------------------------
# 13. HIGHEST MARKS
# ------------------------------------------------------------

cursor.execute(
    "SELECT MAX(marks) FROM students"
)

highest = cursor.fetchone()[0]

print("Highest marks:", highest)


# ------------------------------------------------------------
# 14. LOWEST MARKS
# ------------------------------------------------------------

cursor.execute(
    "SELECT MIN(marks) FROM students"
)

lowest = cursor.fetchone()[0]

print("Lowest marks:", lowest)


# ------------------------------------------------------------
# 15. AVERAGE MARKS
# ------------------------------------------------------------

cursor.execute(
    "SELECT AVG(marks) FROM students"
)

average = cursor.fetchone()[0]

print("Average marks:", average)


# ------------------------------------------------------------
# 16. SORT DATA
# ------------------------------------------------------------

cursor.execute("""
SELECT * FROM students
ORDER BY marks DESC
""")

students = cursor.fetchall()

print("\n----- TOP STUDENTS -----")

for student in students:
    print(student)


# ------------------------------------------------------------
# 17. CLOSE DATABASE
# ------------------------------------------------------------

connection.close()

print("\nDatabase closed!")


# ============================================================
# 📝 PRACTICE QUESTIONS + ANSWERS
# ============================================================

# Q1. Import sqlite3.

import sqlite3


# Q2. Create database named company.db.

connection = sqlite3.connect("company.db")

print("Company database created!")


# Q3. Create employee table.

cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS employees (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    salary INTEGER,
    department TEXT
)
""")

connection.commit()

print("Employee table created!")


# Q4. Insert employee.

cursor.execute("""
INSERT INTO employees (name, salary, department)
VALUES (?, ?, ?)
""", ("Trupti", 30000, "IT"))

connection.commit()

print("Employee added!")


# Q5. Display employees.

cursor.execute("SELECT * FROM employees")

employees = cursor.fetchall()

for employee in employees:
    print(employee)


# Q6. Find employees with salary > 25000.

cursor.execute(
    "SELECT * FROM employees WHERE salary > ?",
    (25000,)
)

employees = cursor.fetchall()

for employee in employees:
    print(employee)


# Q7. Update salary.

cursor.execute("""
UPDATE employees
SET salary = ?
WHERE name = ?
""", (35000, "Trupti"))

connection.commit()


# Q8. Delete employee.

cursor.execute(
    "DELETE FROM employees WHERE name = ?",
    ("Trupti",)
)

connection.commit()


connection.close()


# ============================================================
# 🚀 MINI PROJECT – STUDENT DATABASE MANAGEMENT SYSTEM
# ============================================================

import sqlite3


def create_database():

    connection = sqlite3.connect("student_management.db")

    cursor = connection.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        course TEXT,
        marks REAL
    )
    """)

    connection.commit()

    return connection


def add_student(connection):

    name = input("Enter student name: ")
    course = input("Enter course: ")
    marks = float(input("Enter marks: "))

    cursor = connection.cursor()

    cursor.execute("""
    INSERT INTO students (name, course, marks)
    VALUES (?, ?, ?)
    """, (name, course, marks))

    connection.commit()

    print("Student added successfully!")


def show_students(connection):

    cursor = connection.cursor()

    cursor.execute("SELECT * FROM students")

    students = cursor.fetchall()

    print("\n----- STUDENTS -----")

    if not students:
        print("No students found.")

    for student in students:
        print(
            "ID:", student[0],
            "| Name:", student[1],
            "| Course:", student[2],
            "| Marks:", student[3]
        )


def search_student(connection):

    name = input("Enter name to search: ")

    cursor = connection.cursor()

    cursor.execute(
        "SELECT * FROM students WHERE name = ?",
        (name,)
    )

    student = cursor.fetchone()

    if student:
        print("\nStudent Found!")
        print("ID:", student[0])
        print("Name:", student[1])
        print("Course:", student[2])
        print("Marks:", student[3])

    else:
        print("Student not found!")


def update_marks(connection):

    name = input("Enter student name: ")
    marks = float(input("Enter new marks: "))

    cursor = connection.cursor()

    cursor.execute("""
    UPDATE students
    SET marks = ?
    WHERE name = ?
    """, (marks, name))

    connection.commit()

    print("Marks updated!")


def delete_student(connection):

    name = input("Enter student name: ")

    cursor = connection.cursor()

    cursor.execute(
        "DELETE FROM students WHERE name = ?",
        (name,)
    )

    connection.commit()

    print("Student deleted!")


# ------------------------------------------------------------
# MAIN MENU
# ------------------------------------------------------------

connection = create_database()

while True:

    print("\n========== STUDENT MANAGEMENT ==========")

    print("1. Add Student")
    print("2. Show Students")
    print("3. Search Student")
    print("4. Update Marks")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        add_student(connection)

    elif choice == "2":

        show_students(connection)

    elif choice == "3":

        search_student(connection)

    elif choice == "4":

        update_marks(connection)

    elif choice == "5":

        delete_student(connection)

    elif choice == "6":

        connection.close()

        print("Thank you!")
        break

    else:

        print("Invalid choice!")


# ============================================================
#  IMPORTANT INTERVIEW QUESTIONS
# ============================================================

# 1. What is a database?
# Database is used to store and manage data.

# 2. What is SQLite?
# SQLite is a lightweight database built into Python.

# 3. Which module is used?
# sqlite3

# 4. What is cursor?
# Cursor executes SQL commands.

# 5. What does execute() do?
# It executes an SQL query.

# 6. What does commit() do?
# It saves database changes.

# 7. What does fetchall() do?
# It returns all matching records.

# 8. What does fetchone() do?
# It returns one record.

# 9. What does SELECT do?
# Reads data.

# 10. What does INSERT do?
# Adds data.

# 11. What does UPDATE do?
# Changes existing data.

# 12. What does DELETE do?
# Removes data.


