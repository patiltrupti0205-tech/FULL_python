# Day 4 - Python Loops

# Topics:
# 1. for Loop
# 2. range()
# 3. while Loop
# 4. break
# 5. continue
# 6. pass
# 7. Nested Loop
# 8. Pattern Printing


# ==========================================================
# FOR LOOP
# ==========================================================

print("===== FOR LOOP =====")

# Example 1

for i in range(5):
    print("Hello")

print()


# Example 2

for i in range(1, 6):
    print(i)

print()


# ==========================================================
# RANGE()
# ==========================================================

print("===== RANGE() =====")

# range(stop)

for i in range(5):
    print(i)

print()


# range(start, stop)

for i in range(1, 6):
    print(i)

print()


# range(start, stop, step)

for i in range(2, 11, 2):
    print(i)

print()


# ==========================================================
# EVEN NUMBERS
# ==========================================================

print("===== EVEN NUMBERS =====")

for i in range(2, 21, 2):
    print(i)

print()


# ==========================================================
# ODD NUMBERS
# ==========================================================

print("===== ODD NUMBERS =====")

for i in range(1, 20, 2):
    print(i)

print()


# ==========================================================
# SUM OF NUMBERS
# ==========================================================

print("===== SUM OF NUMBERS =====")

total = 0

for i in range(1, 11):
    total += i

print("Sum =", total)

print()


# ==========================================================
# MULTIPLICATION TABLE
# ==========================================================

print("===== MULTIPLICATION TABLE =====")

num = int(input("Enter a Number: "))

for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")

print()


# ==========================================================
# WHILE LOOP
# ==========================================================

print("===== WHILE LOOP =====")

i = 1

while i <= 5:
    print(i)
    i += 1

print()


# ==========================================================
# REVERSE COUNTING
# ==========================================================

print("===== REVERSE COUNTING =====")

i = 10

while i >= 1:
    print(i)
    i -= 1

print()


# ==========================================================
# BREAK
# ==========================================================

print("===== BREAK =====")

for i in range(1, 11):

    if i == 6:
        break

    print(i)

print()


# ==========================================================
# CONTINUE
# ==========================================================

print("===== CONTINUE =====")

for i in range(1, 6):

    if i == 3:
        continue

    print(i)

print()


# ==========================================================
# PASS
# ==========================================================

print("===== PASS =====")

for i in range(5):

    if i == 3:
        pass

    print(i)

print()


# ==========================================================
# NESTED LOOP
# ==========================================================

print("===== NESTED LOOP =====")

for i in range(1, 4):

    for j in range(1, 4):
        print(i, j)

print()


# ==========================================================
# STAR PATTERN
# ==========================================================

print("===== STAR PATTERN =====")

for i in range(1, 6):
    print("*" * i)

print()


# ==========================================================
# NUMBER PATTERN
# ==========================================================

print("===== NUMBER PATTERN =====")

for i in range(1, 6):

    for j in range(1, i + 1):
        print(j, end="")

    print()

print()


# ==========================================================
# PRACTICE QUESTIONS
# ==========================================================


# 1. Print numbers from 1 to 100

print("===== 1. NUMBERS 1 TO 100 =====")

for i in range(1, 101):
    print(i)

print()


# 2. Print even numbers from 1 to 100

print("===== 2. EVEN NUMBERS =====")

for i in range(2, 101, 2):
    print(i)

print()


# 3. Print odd numbers from 1 to 100

print("===== 3. ODD NUMBERS =====")

for i in range(1, 101, 2):
    print(i)

print()


# 4. Multiplication table

print("===== 4. MULTIPLICATION TABLE =====")

num = int(input("Enter a number: "))

for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")

print()


# 5. Sum of numbers from 1 to N

print("===== 5. SUM OF 1 TO N =====")

n = int(input("Enter N: "))

total = 0

for i in range(1, n + 1):
    total += i

print("Sum =", total)

print()


# 6. Factorial

print("===== 6. FACTORIAL =====")

num = int(input("Enter a number: "))

if num < 0:
    print("Factorial is not possible for negative numbers")

else:

    fact = 1

    for i in range(1, num + 1):
        fact *= i

    print("Factorial =", fact)

print()


# 7. Print numbers from 100 to 1

print("===== 7. REVERSE COUNTING =====")

for i in range(100, 0, -1):
    print(i)

print()


# 8. Count the number of digits

print("===== 8. COUNT DIGITS =====")

num = int(input("Enter a number: "))

num = abs(num)

if num == 0:

    count = 1

else:

    count = 0

    while num > 0:
        count += 1
        num //= 10

print("Digits =", count)

print()


# 9. Reverse a number

print("===== 9. REVERSE NUMBER =====")

num = int(input("Enter a number: "))

sign = -1 if num < 0 else 1

num = abs(num)

reverse = 0

while num > 0:

    digit = num % 10

    reverse = reverse * 10 + digit

    num //= 10

reverse = reverse * sign

print("Reverse =", reverse)

print()


# 10. Check whether a number is palindrome

print("===== 10. PALINDROME =====")

num = int(input("Enter a number: "))

if num < 0:

    print("Negative numbers are not considered palindrome")

else:

    original = num

    reverse = 0

    while num > 0:

        digit = num % 10

        reverse = reverse * 10 + digit

        num //= 10

    if original == reverse:
        print("Palindrome")
    else:
        print("Not Palindrome")

print()


# 11. Numbers divisible by 5

print("===== 11. DIVISIBLE BY 5 =====")

for i in range(1, 101):

    if i % 5 == 0:
        print(i)

print()


# 12. Numbers divisible by both 3 and 5

print("===== 12. DIVISIBLE BY 3 AND 5 =====")

for i in range(1, 101):

    if i % 3 == 0 and i % 5 == 0:
        print(i)

print()


# 13. Sum of digits

print("===== 13. SUM OF DIGITS =====")

num = int(input("Enter a number: "))

num = abs(num)

sum_digits = 0

while num > 0:

    sum_digits += num % 10

    num //= 10

print("Sum of digits =", sum_digits)

print()


# 14. Largest digit

print("===== 14. LARGEST DIGIT =====")

num = int(input("Enter a number: "))

num = abs(num)

if num == 0:

    largest = 0

else:

    largest = 0

    while num > 0:

        digit = num % 10

        if digit > largest:
            largest = digit

        num //= 10

print("Largest digit =", largest)

print()


# 15. Count even and odd numbers from 1 to 100

print("===== 15. EVEN AND ODD COUNT =====")

even = 0
odd = 0

for i in range(1, 101):

    if i % 2 == 0:
        even += 1

    else:
        odd += 1

print("Even =", even)
print("Odd =", odd)

print()


# 16. Multiplication tables from 1 to 10

print("===== 16. MULTIPLICATION TABLES =====")

for i in range(1, 11):

    print(f"\nTable of {i}")

    for j in range(1, 11):

        print(f"{i} x {j} = {i * j}")

print()


# 17. Star Pattern

print("===== 17. STAR PATTERN =====")

for i in range(1, 6):
    print("*" * i)

print()


# 18. Reverse Star Pattern

print("===== 18. REVERSE STAR PATTERN =====")

for i in range(5, 0, -1):
    print("*" * i)

print()


# 19. Number Pattern

print("===== 19. NUMBER PATTERN =====")

for i in range(1, 6):

    for j in range(1, i + 1):
        print(j, end="")

    print()

print()


# 20. Repeated Number Pattern

print("===== 20. REPEATED NUMBER PATTERN =====")

for i in range(1, 6):
    print(str(i) * i)

print()


# ==========================================================
# MINI PROJECT - STUDENT MARKS ANALYZER
# ==========================================================

print("===== STUDENT MARKS ANALYZER =====")

while True:

    print("\n========== STUDENT MARKS ANALYZER ==========")

    name = input("Enter Student Name: ")

    marks = []

    for i in range(1, 6):

        while True:

            mark = int(input(f"Enter Marks of Subject {i}: "))

            if 0 <= mark <= 100:
                marks.append(mark)
                break

            else:
                print("Please enter marks between 0 and 100.")


    # Total Marks

    total = sum(marks)


    # Average Marks

    average = total / len(marks)


    # Highest Marks

    highest = max(marks)


    # Lowest Marks

    lowest = min(marks)


    # Grade

    if average >= 90:
        grade = "A"

    elif average >= 80:
        grade = "B"

    elif average >= 70:
        grade = "C"

    elif average >= 60:
        grade = "D"

    elif average >= 35:
        grade = "E"

    else:
        grade = "F"


    # Result

    if average >= 35:
        result = "PASS"

    else:
        result = "FAIL"


    # Student Report

    print("\n========== STUDENT REPORT ==========")

    print("Student Name :", name)

    print("Marks        :", marks)

    print("Total Marks  :", total)

    print("Average      :", average)

    print("Highest Mark :", highest)

    print("Lowest Mark  :", lowest)

    print("Grade        :", grade)

    print("Result       :", result)


    # Ask for another student

    choice = input(
        "\nDo you want to enter another student's marks? (Y/N): "
    )


    if choice.upper() != "Y":

        print("\nThank You for using Student Marks Analyzer!")

        break


print("\n========== END OF DAY 4 ==========")