# Day 9 - Python Sets

# What is a Set?
# A set is used to store multiple items in a single variable.
# Sets are unordered and do not allow duplicate values.
# Sets are written using curly brackets {}.


# Creating a Set

fruits = {"apple", "banana", "mango", "orange"}

print(fruits)


# Duplicate Values in Set

numbers = {10, 20, 30, 20, 10, 40}

print(numbers)


# Length of Set

print(len(fruits))


# Check Item in Set

if "apple" in fruits:
    print("Apple is available")


# Add an Item

fruits.add("grapes")

print(fruits)


# Add Multiple Items

fruits.update(["watermelon", "kiwi"])

print(fruits)


# Remove an Item

fruits.remove("kiwi")

print(fruits)


# Discard an Item

fruits.discard("watermelon")

print(fruits)


# Loop Through a Set

for fruit in fruits:
    print(fruit)


# Set with Numbers

numbers = {10, 20, 30, 40, 50}

print(numbers)


# Union of Two Sets
# Union combines all items from both sets.

set1 = {"apple", "banana", "mango"}
set2 = {"orange", "grapes", "banana"}

result = set1.union(set2)

print(result)


# Intersection of Two Sets
# Intersection returns common items.

result = set1.intersection(set2)

print(result)


# Difference of Two Sets
# Difference returns items present in first set
# but not in second set.

result = set1.difference(set2)

print(result)


# Symmetric Difference
# Returns items that are not common.

result = set1.symmetric_difference(set2)

print(result)


# Set Operations Using Symbols

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

print(set1 | set2)       # Union
print(set1 & set2)       # Intersection
print(set1 - set2)       # Difference
print(set1 ^ set2)       # Symmetric Difference


# Convert List into Set

numbers = [10, 20, 10, 30, 20, 40, 30]

unique_numbers = set(numbers)

print(unique_numbers)


# Convert Set into List

numbers_list = list(unique_numbers)

print(numbers_list)


# Here are some questions:


# 1. Create a set of 5 fruits and print it

fruits = {"apple", "banana", "mango", "orange", "grapes"}

print(fruits)


# 2. Create a set with duplicate numbers
# Print the set and observe the result

numbers = {10, 20, 10, 30, 20, 40}

print(numbers)


# 3. Find the length of a set

print(len(numbers))


# 4. Add a new item to a set

numbers.add(50)

print(numbers)


# 5. Remove an item from a set

numbers.remove(20)

print(numbers)


# 6. Check whether 30 exists in the set

if 30 in numbers:
    print("30 is available")
else:
    print("30 is not available")


# 7. Print all items using a loop

for number in numbers:
    print(number)


# 8. Find the union of two sets

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print(a.union(b))


# 9. Find the intersection of two sets

print(a.intersection(b))


# 10. Find the difference between two sets

print(a.difference(b))

#=================================================
# Set Mini Project - Unique Student Subjects
#=================================================
students_subjects = {
    "Python",
    "Java",
    "Python",
    "Cloud Computing",
    "Database",
    "Java"
}

print("===== STUDENT SUBJECTS =====")

print(students_subjects)


# Total Unique Subjects

print("Total Unique Subjects:", len(students_subjects))


# Check Subject

if "Python" in students_subjects:
    print("Python is available")
else:
    print("Python is not available")


# Add New Subject

students_subjects.add("Cyber Security")

print("\nAfter Adding New Subject:")
print(students_subjects)


# Remove Subject

students_subjects.remove("Java")

print("\nAfter Removing Java:")
print(students_subjects)


# Two Students' Subjects

student1 = {
    "Python",
    "Java",
    "Cloud Computing",
    "Database"
}

student2 = {
    "Python",
    "Cloud Computing",
    "Cyber Security",
    "Networking"
}


# Common Subjects

common_subjects = student1.intersection(student2)

print("\n===== COMMON SUBJECTS =====")
print(common_subjects)


# All Subjects

all_subjects = student1.union(student2)

print("\n===== ALL SUBJECTS =====")
print(all_subjects)


# Subjects Only Student 1 Has

only_student1 = student1.difference(student2)

print("\n===== STUDENT 1 ONLY =====")
print(only_student1)


# Subjects Only Student 2 Has

only_student2 = student2.difference(student1)

print("\n===== STUDENT 2 ONLY =====")
print(only_student2)