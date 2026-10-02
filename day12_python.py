# ==========================================
# DAY 12 – PYTHON FILE HANDLING
# ==========================================


# ------------------------------------------
# 1. WHAT IS FILE HANDLING?
# ------------------------------------------

# File handling means:
# Python se file ko create, read, write aur update karna.


# ------------------------------------------
# 2. OPEN A FILE
# ------------------------------------------

# open() is used to open a file

file = open("student.txt", "r")

file.close()


# ------------------------------------------
# 3. FILE MODES
# ------------------------------------------

# "r"  = Read
# "w"  = Write
# "a"  = Append
# "x"  = Create new file
# "r+" = Read + Write


# ------------------------------------------
# 4. WRITE TO A FILE
# ------------------------------------------

file = open("student.txt", "w")

file.write("Hello Trupti!")
file.write("\nWelcome to Python.")

file.close()


# ------------------------------------------
# 5. READ A FILE
# ------------------------------------------

file = open("student.txt", "r")

data = file.read()

print(data)

file.close()


# ------------------------------------------
# 6. READ ONLY FIRST LINE
# ------------------------------------------

file = open("student.txt", "r")

line = file.readline()

print(line)

file.close()


# ------------------------------------------
# 7. READ ALL LINES
# ------------------------------------------

file = open("student.txt", "r")

lines = file.readlines()

print(lines)

file.close()


# ------------------------------------------
# 8. READ FILE USING LOOP
# ------------------------------------------

file = open("student.txt", "r")

for line in file:
    print(line)

file.close()


# ------------------------------------------
# 9. APPEND DATA
# ------------------------------------------

# Append means add new data
# without deleting old data.

file = open("student.txt", "a")

file.write("\nPython Day 12")
file.write("\nFile Handling")

file.close()


# ------------------------------------------
# 10. WITH OPEN()
# ------------------------------------------

# with open() automatically closes the file.

with open("student.txt", "r") as file:
    data = file.read()

print(data)


# ------------------------------------------
# 11. WRITE MULTIPLE LINES
# ------------------------------------------

with open("students.txt", "w") as file:

    file.write("Trupti\n")
    file.write("Riya\n")
    file.write("Nensi\n")
    file.write("Priya\n")


# ------------------------------------------
# 12. READ MULTIPLE LINES
# ------------------------------------------

with open("students.txt", "r") as file:

    for student in file:
        print(student.strip())


# ------------------------------------------
# 13. CHECK FILE CONTENT
# ------------------------------------------

with open("student.txt", "r") as file:

    data = file.read()

    if "Python" in data:
        print("Python is present")
    else:
        print("Python is not present")


# ------------------------------------------
# 14. COUNT WORDS IN A FILE
# ------------------------------------------

with open("student.txt", "r") as file:

    data = file.read()

words = data.split()

print("Total Words:", len(words))


# ------------------------------------------
# 15. COUNT CHARACTERS
# ------------------------------------------

with open("student.txt", "r") as file:

    data = file.read()

print("Total Characters:", len(data))


# ------------------------------------------
# 16. FILE EXISTENCE CHECK
# ------------------------------------------

import os

if os.path.exists("student.txt"):
    print("File exists")
else:
    print("File does not exist")


# ------------------------------------------
# 17. DELETE A FILE
# ------------------------------------------

import os

if os.path.exists("student.txt"):
    os.remove("student.txt")
    print("File deleted")
else:
    print("File does not exist")


# ------------------------------------------
# 18. CREATE A NEW FILE
# ------------------------------------------

file = open("newfile.txt", "x")

file.close()

print("File created")


# ------------------------------------------
# 19. FILE POSITION – tell()
# ------------------------------------------

with open("students.txt", "r") as file:

    print("Position:", file.tell())

    data = file.read(5)

    print(data)

    print("Position:", file.tell())


# ------------------------------------------
# 20. MOVE FILE POSITION – seek()
# ------------------------------------------

with open("students.txt", "r") as file:

    print(file.read(5))

    file.seek(0)

    print(file.read(5))


# ==========================================
# PRACTICE QUESTIONS
# ==========================================

# ------------------------------------------
# Q1. Create a file "name.txt"
# and write your name into it.
# ------------------------------------------

with open("name.txt", "w") as file:
    file.write("Trupti")


# ------------------------------------------
# Q2. Create a file "college.txt"
# and write your college name.
# ------------------------------------------

with open("college.txt", "w") as file:
    file.write("RNGPIT")


# ------------------------------------------
# Q3. Read and print content of name.txt
# ------------------------------------------

with open("name.txt", "r") as file:
    data = file.read()

print("Name:", data)


# ------------------------------------------
# Q4. Add course name to college.txt
# using append mode.
# ------------------------------------------

with open("college.txt", "a") as file:
    file.write("\nB.Sc. IT")


# ------------------------------------------
# Q5. Create a file and write
# 5 student names.
# ------------------------------------------

with open("students.txt", "w") as file:

    file.write("Trupti\n")
    file.write("Riya\n")
    file.write("Nensi\n")
    file.write("Priya\n")
    file.write("Aisha\n")


# ------------------------------------------
# Q6. Read the file using a for loop.
# ------------------------------------------

with open("students.txt", "r") as file:

    for student in file:
        print(student.strip())


# ------------------------------------------
# Q7. Count the number of words in a file.
# ------------------------------------------

with open("college.txt", "r") as file:
    data = file.read()

words = data.split()

print("Total Words:", len(words))


# ------------------------------------------
# Q8. Count the number of characters
# in a file.
# ------------------------------------------

with open("name.txt", "r") as file:
    data = file.read()

print("Total Characters:", len(data))


# ------------------------------------------
# Q9. Check whether a file exists or not.
# ------------------------------------------

import os

if os.path.exists("name.txt"):
    print("File exists")
else:
    print("File does not exist")


# ------------------------------------------
# Q10. Delete a file using os.remove()
# ------------------------------------------

import os

if os.path.exists("name.txt"):

    os.remove("name.txt")

    print("File deleted successfully")

else:

    print("File does not exist")


# ==========================================
# EXTRA PRACTICE
# ==========================================


# ------------------------------------------
# Add multiple notes to a file
# ------------------------------------------

with open("notes.txt", "a") as file:

    file.write("Learn Python\n")
    file.write("Practice File Handling\n")
    file.write("Upload project to GitHub\n")


# ------------------------------------------
# Read notes
# ------------------------------------------

with open("notes.txt", "r") as file:

    notes = file.read()

print("\n----- NOTES -----")
print(notes)


# ------------------------------------------
# Check if "Python" exists in the file
# ------------------------------------------

with open("notes.txt", "r") as file:

    data = file.read()

if "Python" in data:
    print("Python is present")
else:
    print("Python is not present")


# ------------------------------------------
# Count number of lines
# ------------------------------------------

with open("notes.txt", "r") as file:

    lines = file.readlines()

print("Total Lines:", len(lines))

# ==========================================
# MINI PROJECT
# STUDENT NOTES MANAGER
# ==========================================

print("\n===== STUDENT NOTES MANAGER =====")

while True:

    print("\n1. Add Note")
    print("2. View Notes")
    print("3. Exit")

    choice = input("Enter your choice: ")

    # Add note
    if choice == "1":

        note = input("Enter your note: ")

        with open("notes.txt", "a") as file:
            file.write(note + "\n")

        print("Note saved successfully!")


    # View notes
    elif choice == "2":

        try:

            with open("notes.txt", "r") as file:
                notes = file.read()

            print("\n----- YOUR NOTES -----")
            print(notes)

        except FileNotFoundError:

            print("No notes found.")


    # Exit
    elif choice == "3":

        print("Thank you!")
        break


    else:

        print("Invalid choice!")

