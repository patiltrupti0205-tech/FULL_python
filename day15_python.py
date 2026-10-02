# ==========================================
# DAY 15 – ADVANCED LISTS
# ==========================================

# ------------------------------------------
# 1. LIST METHODS
# ------------------------------------------

fruits = ["Apple", "Mango", "Banana"]

print(fruits)


# ------------------------------------------
# 2. append()
# Adds one item at the end
# ------------------------------------------

fruits.append("Orange")

print(fruits)


# ------------------------------------------
# 3. insert()
# Adds item at a specific position
# ------------------------------------------

fruits.insert(1, "Grapes")

print(fruits)


# ------------------------------------------
# 4. extend()
# Adds multiple items
# ------------------------------------------

fruits.extend(["Kiwi", "Papaya"])

print(fruits)


# ------------------------------------------
# 5. remove()
# Removes a specific item
# ------------------------------------------

fruits.remove("Banana")

print(fruits)


# ------------------------------------------
# 6. pop()
# Removes item using index
# ------------------------------------------

fruits.pop()

print(fruits)

fruits.pop(1)

print(fruits)


# ------------------------------------------
# 7. clear()
# Removes all items
# ------------------------------------------

numbers = [10, 20, 30]

numbers.clear()

print(numbers)


# ------------------------------------------
# 8. index()
# Finds position of an item
# ------------------------------------------

fruits = ["Apple", "Mango", "Banana"]

print(fruits.index("Mango"))


# ------------------------------------------
# 9. count()
# Counts an item
# ------------------------------------------

numbers = [10, 20, 10, 30, 10, 40]

print(numbers.count(10))


# ------------------------------------------
# 10. sort()
# Sorts in ascending order
# ------------------------------------------

numbers = [50, 10, 40, 20, 30]

numbers.sort()

print(numbers)


# ------------------------------------------
# 11. sort(reverse=True)
# Sorts in descending order
# ------------------------------------------

numbers = [50, 10, 40, 20, 30]

numbers.sort(reverse=True)

print(numbers)


# ------------------------------------------
# 12. reverse()
# Reverses the list
# ------------------------------------------

numbers = [10, 20, 30, 40]

numbers.reverse()

print(numbers)


# ------------------------------------------
# 13. sorted()
# Creates a sorted copy
# ------------------------------------------

numbers = [40, 10, 30, 20]

new_numbers = sorted(numbers)

print("Original:", numbers)
print("Sorted:", new_numbers)


# ------------------------------------------
# 14. min(), max(), sum()
# ------------------------------------------

numbers = [10, 20, 30, 40, 50]

print("Minimum:", min(numbers))
print("Maximum:", max(numbers))
print("Total:", sum(numbers))


# ------------------------------------------
# 15. len()
# ------------------------------------------

students = ["Trupti", "Riya", "Nensi", "Priya"]

print("Total Students:", len(students))


# ------------------------------------------
# 16. List slicing
# ------------------------------------------

numbers = [10, 20, 30, 40, 50]

print(numbers[1:4])
print(numbers[:3])
print(numbers[2:])
print(numbers[::-1])


# ------------------------------------------
# 17. Copy a list
# ------------------------------------------

numbers = [10, 20, 30]

new_numbers = numbers.copy()

print(new_numbers)


# ------------------------------------------
# 18. Nested list
# ------------------------------------------

students = [
    ["Trupti", 85],
    ["Riya", 90],
    ["Nensi", 78]
]

print(students)

print(students[0])
print(students[0][0])
print(students[0][1])


# ------------------------------------------
# 19. Loop through nested list
# ------------------------------------------

for student in students:

    print(student[0], student[1])


# ------------------------------------------
# 20. List comprehension
# ------------------------------------------

numbers = [1, 2, 3, 4, 5]

squares = [number * number for number in numbers]

print(squares)


# ------------------------------------------
# 21. List comprehension with condition
# ------------------------------------------

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_numbers = [number for number in numbers if number % 2 == 0]

print(even_numbers)


# ------------------------------------------
# 22. Odd numbers using comprehension
# ------------------------------------------

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

odd_numbers = [number for number in numbers if number % 2 != 0]

print(odd_numbers)


# ------------------------------------------
# 23. Convert strings to uppercase
# ------------------------------------------

names = ["trupti", "riya", "nensi"]

upper_names = [name.upper() for name in names]

print(upper_names)


# ------------------------------------------
# 24. Find numbers greater than 50
# ------------------------------------------

numbers = [20, 60, 40, 80, 30, 90]

large_numbers = [number for number in numbers if number > 50]

print(large_numbers)


# ------------------------------------------
# 25. Remove duplicates
# ------------------------------------------

numbers = [10, 20, 10, 30, 20, 40, 30]

unique_numbers = list(set(numbers))

print(unique_numbers)


# ==========================================
# PRACTICE QUESTIONS + ANSWERS
# ==========================================


# ------------------------------------------
# Q1. Add "Orange" to a fruit list.
# ------------------------------------------

fruits = ["Apple", "Mango", "Banana"]

fruits.append("Orange")

print(fruits)


# ------------------------------------------
# Q2. Insert "Grapes" at index 1.
# ------------------------------------------

fruits = ["Apple", "Mango", "Banana"]

fruits.insert(1, "Grapes")

print(fruits)


# ------------------------------------------
# Q3. Remove "Mango" from the list.
# ------------------------------------------

fruits = ["Apple", "Mango", "Banana"]

fruits.remove("Mango")

print(fruits)


# ------------------------------------------
# Q4. Find the maximum number.
# ------------------------------------------

numbers = [25, 10, 75, 40, 60]

print("Maximum:", max(numbers))


# ------------------------------------------
# Q5. Find the minimum number.
# ------------------------------------------

numbers = [25, 10, 75, 40, 60]

print("Minimum:", min(numbers))


# ------------------------------------------
# Q6. Find the total of all numbers.
# ------------------------------------------

numbers = [10, 20, 30, 40, 50]

print("Total:", sum(numbers))


# ------------------------------------------
# Q7. Sort numbers in ascending order.
# ------------------------------------------

numbers = [50, 10, 40, 20, 30]

numbers.sort()

print(numbers)


# ------------------------------------------
# Q8. Sort numbers in descending order.
# ------------------------------------------

numbers = [50, 10, 40, 20, 30]

numbers.sort(reverse=True)

print(numbers)


# ------------------------------------------
# Q9. Find all even numbers using
# list comprehension.
# ------------------------------------------

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_numbers = [
    number for number in numbers
    if number % 2 == 0
]

print(even_numbers)


# ------------------------------------------
# Q10. Find all odd numbers using
# list comprehension.
# ------------------------------------------

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

odd_numbers = [
    number for number in numbers
    if number % 2 != 0
]

print(odd_numbers)


# ------------------------------------------
# Q11. Create squares of numbers
# using list comprehension.
# ------------------------------------------

numbers = [1, 2, 3, 4, 5]

squares = [number ** 2 for number in numbers]

print(squares)


# ------------------------------------------
# Q12. Convert names to uppercase.
# ------------------------------------------

names = ["trupti", "riya", "nensi"]

upper_names = [name.upper() for name in names]

print(upper_names)


# ------------------------------------------
# Q13. Find numbers greater than 50.
# ------------------------------------------

numbers = [20, 60, 45, 80, 30, 90]

result = [number for number in numbers if number > 50]

print(result)


# ------------------------------------------
# Q14. Remove duplicate values.
# ------------------------------------------

numbers = [10, 20, 10, 30, 20, 40, 30]

unique_numbers = list(set(numbers))

print(unique_numbers)


# ------------------------------------------
# Q15. Find total and average marks.
# ------------------------------------------

marks = [85, 78, 92, 88, 90]

total = sum(marks)

average = total / len(marks)

print("Total:", total)
print("Average:", average)


# ==========================================
# MINI PROJECT
# STUDENT MARKS ANALYZER
# ==========================================

print("\n===== STUDENT MARKS ANALYZER =====")

students = []

number_of_students = int(
    input("Enter number of students: ")
)


for i in range(number_of_students):

    name = input("\nEnter student name: ")

    marks = []

    for j in range(3):

        mark = float(
            input(f"Enter subject {j + 1} marks: ")
        )

        marks.append(mark)

    students.append([name, marks])


# ------------------------------------------
# Display student results
# ------------------------------------------

print("\n===== STUDENT RESULTS =====")

for student in students:

    name = student[0]
    marks = student[1]

    total = sum(marks)

    average = total / len(marks)

    highest = max(marks)

    lowest = min(marks)

    print("\nName:", name)
    print("Marks:", marks)
    print("Total:", total)
    print("Average:", average)
    print("Highest:", highest)
    print("Lowest:", lowest)

    if average >= 50:
        print("Result: PASS")
    else:
        print("Result: FAIL")


# ------------------------------------------
# Find highest average student
# ------------------------------------------

highest_average = 0
top_student = ""

for student in students:

    name = student[0]
    marks = student[1]

    average = sum(marks) / len(marks)

    if average > highest_average:

        highest_average = average
        top_student = name


print("\n===== TOP STUDENT =====")

print("Name:", top_student)
print("Average:", highest_average)

