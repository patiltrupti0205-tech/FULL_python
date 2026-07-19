# Day 1 - Python Basics
# 1. Print Statement

print("Hello, World!")
print("Welcome to Python Programming , I am learning the Python programming language , so let's start! ")


# 2. Variables

myname = "Trupti"
myage = 19
myheight = 5.2
is_student = True

print("\nVariables")
print("Myself:", myname)
print("My Age:", myage)
print("Height:", myheight)
print("Student:", is_student)


# 3. Data Types

print("\nData Types")
print(type(myname))
print(type(myage))
print(type(myheight))
print(type(is_student))


# 4. User Input

user_name = input("\nEnter your name: ")
print("Hello ! , my self ", user_name)


# 5. Type Casting

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("Sum =", num1 + num2)


# 6. Arithmetic Operators

a = 20
b = 6

print("\nArithmetic Operators")
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Modulus:", a % b)
print("Power:", a ** b)


# 7. Comparison Operators

print("\nComparison Operators")
print(a == b)
print(a != b)
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)

# 8. Logical Operators


x = True
y = False

print("\nLogical Operators")
print("AND:", x and y)
print("OR:", x or y)
print("NOT:", not x)


# 9. Assignment Operators

num = 10
num += 5
print("\nAssignment Operator")
print(num)


# 10. Identity Operators


list1 = [1, 2, 3]
list2 = list1
list3 = [1, 2, 3]

print("\nIdentity Operators")
print(list1 is list2)
print(list1 is list3)


# 11. Membership Operators

fruits = ["Apple", "Banana", "Mango"]

print("\nMembership Operators")
print("Apple" in fruits)
print("Orange" not in fruits)


# 12. Escape Characters


print("\nEscape Characters")
print("Python\nProgramming")
print("Python\tProgramming")


# 13. String Operations


text = "Python"

print("\nString Operations")
print(text.upper())
print(text.lower())
print(len(text))
print(text[0])
print(text[-1])



# End of Day 1


print("\nCongratulations! Day 1 Python Completed.")