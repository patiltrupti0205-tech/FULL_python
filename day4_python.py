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

print("FOR LOOP")

# Example 1
for i in range(5):
    print("Hello")

print()

# Example 2
for i in range(1, 6):
    print(i)

print()



print(" RANGE()")

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

print("EVEN NUMBERS")

for i in range(2, 21, 2):
    print(i)

print()

print("ODD NUMBERS ")

for i in range(1, 20, 2):
    print(i)

print()

print("SUM OF NUMBERS ")

total = 0

for i in range(1, 11):
    total += i

print("Sum =", total)

print()


print(" MULTIPLICATION TABLE ")

num = int(input("Enter a Number: "))

for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")

print()



print(" LOOP ")

i = 1

while i <= 5:
    print(i)
    i += 1

print()


print("REVERSE COUNTING ")

i = 10

while i >= 1:
    print(i)
    i -= 1

print()

print(" BREAK ")

for i in range(1, 11):
    if i == 6:
        break
    print(i)

print()


print(" CONTINUE ")

for i in range(1, 6):
    if i == 3:
        continue
    print(i)

print()

print("PASS")

for i in range(5):
    if i == 3:
        pass
    print(i)

print()

print(" NESTED LOOP ")

for i in range(1, 4):
    for j in range(1, 4):
        print(i, j)

print()


print(" STAR PATTERN ")

for i in range(1, 6):
    print("*" * i)

print()

print(" NUMBER PATTERN ")

for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end="")
    print()

print()

print(" HOMEWORK EXAMPLES ")

# 1. Print 1 to 100
for i in range(1, 101):
    print(i)

print()

# 2. Even Numbers
for i in range(2, 101, 2):
    print(i)

print()

# 3. Odd Numbers
for i in range(1, 101, 2):
    print(i)

print()

# 4. Sum of 1 to N
n = int(input("Enter N: "))

total = 0

for i in range(1, n + 1):
    total += i

print("Sum =", total)

print()

# 5. Factorial
num = int(input("Enter Number: "))

fact = 1

for i in range(1, num + 1):
    fact *= i

print("Factorial =", fact)

print()

# 6. Reverse Counting
for i in range(100, 0, -1):
    print(i)

print()

# 7. Count Digits
num = int(input("Enter Number: "))

count = 0

while num > 0:
    count += 1
    num //= 10

print("Digits =", count)

print()

# 8. Reverse Number
num = int(input("Enter Number: "))

reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num //= 10

print("Reverse =", reverse)

print()

# 9. Palindrome Number
num = int(input("Enter Number: "))

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


print("========== END OF DAY 4 ==========")

# 1. Print numbers from 1 to 100.
for i in range(1, 101):
    print(i)


# 2. Print even numbers from 1 to 100.
for i in range(2, 101, 2):
    print(i)



# 3. Print odd numbers from 1 to 100.
for i in range(1, 101, 2):
    print(i)



# 4. Print the multiplication table of any number.
num = int(input("Enter a number: "))

for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")



# 5. Find the sum of numbers from 1 to N.
n = int(input("Enter N: "))

total = 0

for i in range(1, n + 1):
    total += i

print("Sum =", total)



# 6. Find the factorial of a number.
num = int(input("Enter a number: "))

fact = 1

for i in range(1, num + 1):
    fact *= i

print("Factorial =", fact)



# 7. Print numbers from 100 to 1.
for i in range(100, 0, -1):
    print(i)



# 8. Count the number of digits in a number.
num = int(input("Enter a number: "))

count = 0

while num > 0:
    count += 1
    num //= 10

print("Digits =", count)


# 9. Reverse a number.
num = int(input("Enter a number: "))

reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num //= 10

print("Reverse =", reverse)



# 10. Check whether a number is a palindrome.
num = int(input("Enter a number: "))

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



# 11. Print all numbers between 1 and 100 that are divisible by 5.
for i in range(1, 101):
    if i % 5 == 0:
        print(i)



# 12. Print all numbers between 1 and 100 that are divisible by both 3 and 5.
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print(i)


# 13. Find the sum of digits of a number.
num = int(input("Enter a number: "))

sum_digits = 0

while num > 0:
    sum_digits += num % 10
    num //= 10

print("Sum of digits =", sum_digits)


# 14. Find the largest digit in a number.
num = int(input("Enter a number: "))

largest = 0

while num > 0:
    digit = num % 10

    if digit > largest:
        largest = digit

    num //= 10

print("Largest digit =", largest)



# 15. Count how many even and odd numbers are between 1 and 100.
even = 0
odd = 0

for i in range(1, 101):
    if i % 2 == 0:
        even += 1
    else:
        odd += 1

print("Even =", even)
print("Odd =", odd)


# 16. Print all multiplication tables from 1 to 10.
for i in range(1, 11):
    print(f"\nTable of {i}")

    for j in range(1, 11):
        print(f"{i} x {j} = {i * j}")



# 17. Star Pattern
for i in range(1, 6):
    print("*" * i)



# 18. Reverse Star Pattern
for i in range(5, 0, -1):
    print("*" * i)



# 19. Number Pattern
for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end="")
    print()



# 20. Repeated Number Pattern
for i in range(1, 6):
    print(str(i) * i)


# Mini Project - Student Marks Analyzer

while True:

    print("\n========== Student Marks Analyzer ==========")

    name = input("Enter Student Name: ")

    marks = []

    for i in range(1, 6):
        mark = int(input(f"Enter Marks of Subject {i}: "))
        marks.append(mark)

    total = sum(marks)
    average = total / 5
    highest = max(marks)
    lowest = min(marks)

    if average >= 90:
        grade = "A"
    elif average >= 80:
        grade = "B"
    elif average >= 70:
        grade = "C"
    elif average >= 60:
        grade = "D"
    else:
        grade = "F"

    if average >= 35:
        result = "PASS"
    else:
        result = "FAIL"

    print("\n Student Report ")
    print("Student Name :", name)
    print("Marks        :", marks)
    print("Total Marks  :", total)
    print("Average      :", average)
    print("Highest Mark :", highest)
    print("Lowest Mark  :", lowest)
    print("Grade        :", grade)
    print("Result       :", result)
   
    choice = input("\nDo you want to enter another student's marks? (Y/N): ")

    if choice.upper() != "Y":
        print("\nThank You for using Student Marks Analyzer!")
        break