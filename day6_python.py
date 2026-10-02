# Day 6 - Python Lists
# What is a List?
# A list is used to store multiple items in a single variable.

# Creating a List

fruits = ["Apple", "Banana", "Mango"]
print(fruits)

# Accessing List Elements

print(fruits[0])
print(fruits[1])
print(fruits[2])


# Negative Indexing

print(fruits[-1])
print(fruits[-2])


# List Slicing

numbers = [10, 20, 30, 40, 50, 60]

print(numbers[1:4])
print(numbers[:3])
print(numbers[2:])
print(numbers[::2])


# Change List Item

fruits = ["Apple", "Banana", "Mango"]

fruits[1] = "Orange"

print(fruits)


# Add Elements

numbers = [10, 20, 30]

numbers.append(40)

print(numbers)


# Insert Element

numbers = [10, 20, 30]

numbers.insert(1, 15)

print(numbers)


# Extend List

list1 = [1, 2, 3]
list2 = [4, 5, 6]

list1.extend(list2)

print(list1)


# Remove Element

numbers = [10, 20, 30]

numbers.remove(20)

print(numbers)


# Pop Element

numbers = [10, 20, 30]

numbers.pop()

print(numbers)


# Delete Element

numbers = [10, 20, 30]

del numbers[1]

print(numbers)


# Clear List

numbers = [1, 2, 3]

numbers.clear()

print(numbers)


# Length of List

numbers = [10, 20, 30, 40]

print(len(numbers))


# Membership Operator

fruits = ["Apple", "Banana", "Mango"]

print("Apple" in fruits)
print("Orange" in fruits)
print("Orange" not in fruits)


# Loop Through List

fruits = ["Apple", "Banana", "Mango"]

for fruit in fruits:
    print(fruit)


# Sort List

numbers = [5, 2, 9, 1, 7]

numbers.sort()

print(numbers)


# Reverse List

numbers = [10, 20, 30]

numbers.reverse()

print(numbers)


# Copy List

numbers = [10, 20, 30]

new_list = numbers.copy()

print(new_list)


# Count Method

numbers = [1, 2, 2, 3, 2]

print(numbers.count(2))


# Index Method

fruits = ["Apple", "Banana", "Mango"]

print(fruits.index("Banana"))


# Nested List

matrix = [
    [1, 2],
    [3, 4]
]

print(matrix)
print(matrix[0])
print(matrix[0][1])


# List Comprehension

numbers = [1, 2, 3, 4, 5]

square = [num * num for num in numbers]

print(square)

# some practice quetions.

# 1. Print all elements of a list.

numbers = [10, 20, 30, 40, 50]

for num in numbers:
    print(num)


# 2. Find the largest number.

numbers = [15, 25, 8, 42, 30]

largest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num

print("Largest Number:", largest)


# 3. Find the smallest number.

numbers = [15, 25, 8, 42, 30]

smallest = numbers[0]

for num in numbers:
    if num < smallest:
        smallest = num

print("Smallest Number:", smallest)


# 4. Find the sum of all elements.

numbers = [10, 20, 30, 40]

total = 0

for num in numbers:
    total += num

print("Sum:", total)


# 5. Count even and odd numbers.

numbers = [1, 2, 3, 4, 5, 6, 7, 8]

even = 0
odd = 0

for num in numbers:
    if num % 2 == 0:
        even += 1
    else:
        odd += 1

print("Even Numbers:", even)
print("Odd Numbers:", odd)


# 6. Reverse a list without using reverse().

numbers = [10, 20, 30, 40, 50]

reverse = []

for i in range(len(numbers) - 1, -1, -1):
    reverse.append(numbers[i])

print("Reversed List:", reverse)


# 7. Remove duplicate values.

numbers = [1, 2, 2, 3, 4, 4, 5]

unique = []

for num in numbers:
    if num not in unique:
        unique.append(num)

print("After Removing Duplicates:", unique)


# 8. Search an element in a list.

numbers = [10, 20, 30, 40, 50]

search = int(input("Enter number to search: "))

if search in numbers:
    print("Number Found")
else:
    print("Number Not Found")


# 9. Find the second largest number.

numbers = [10, 50, 30, 70, 40]

largest = second = float("-inf")

for num in numbers:
    if num > largest:
        second = largest
        largest = num
    elif num > second and num != largest:
        second = num

print("Second Largest Number:", second)


# 10. Take 5 numbers from the user and store them in a list.

numbers = []

for i in range(5):
    num = int(input(f"Enter Number {i + 1}: "))
    numbers.append(num)

print("User List:", numbers)


# 11. Merge two lists.

list1 = [1, 2, 3]
list2 = [4, 5, 6]

merged = list1 + list2

print("Merged List:", merged)


# 12. Count positive and negative numbers.

numbers = [-2, 5, -7, 4, -1, 8]

positive = 0
negative = 0

for num in numbers:
    if num >= 0:
        positive += 1
    else:
        negative += 1

print("Positive Numbers:", positive)
print("Negative Numbers:", negative)


# 13. Find the average of list elements.

numbers = [10, 20, 30, 40]

total = 0

for num in numbers:
    total += num

average = total / len(numbers)

print("Average:", average)


# 14. Print elements at even index.

numbers = [10, 20, 30, 40, 50, 60]

for i in range(0, len(numbers), 2):
    print(numbers[i])


# 15. Rotate a list by one position.

numbers = [1, 2, 3, 4, 5]

rotated = [numbers[-1]] + numbers[:-1]

print("Rotated List:", rotated)

# 1 mini project 

# Day 6 Mini Project - Student Marks Manager

marks = []

# Take marks from user
for i in range(5):
    mark = int(input(f"Enter marks of Student {i + 1}: "))
    marks.append(mark)

print("\n========== RESULT ==========")
print("Student Marks:", marks)

# Highest Marks
highest = marks[0]
for mark in marks:
    if mark > highest:
        highest = mark

print("Highest Marks:", highest)

# Lowest Marks
lowest = marks[0]
for mark in marks:
    if mark < lowest:
        lowest = mark

print("Lowest Marks:", lowest)

# Total Marks
total = 0
for mark in marks:
    total += mark

print("Total Marks:", total)

# Average Marks
average = total / len(marks)
print("Average Marks:", average)

# Pass and Fail Count
pass_count = 0
fail_count = 0

for mark in marks:
    if mark >= 35:
        pass_count += 1
    else:
        fail_count += 1

print("Passed Students:", pass_count)
print("Failed Students:", fail_count)

# Grade of Each Student
print("\n========== GRADES ==========")

for i in range(len(marks)):
    if marks[i] >= 90:
        grade = "A+"
    elif marks[i] >= 75:
        grade = "A"
    elif marks[i] >= 60:
        grade = "B"
    elif marks[i] >= 35:
        grade = "C"
    else:
        grade = "F"

    print(f"Student {i + 1}: {marks[i]} Marks -> Grade {grade}")

