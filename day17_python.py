# ============================================================
# 🐍 DAY 17 – OOP BASICS
# ============================================================

# OOP = Object-Oriented Programming
#
# Main concepts:
# 1. Class
# 2. Object
# 3. Attributes
# 4. Methods
# 5. __init__()


# ------------------------------------------------------------
# 1️⃣ CLASS
# ------------------------------------------------------------

# Class ek blueprint/template hoti hai.

class Student:
    pass


# ------------------------------------------------------------
# 2️⃣ OBJECT
# ------------------------------------------------------------

# Class se object create karte hain.

student1 = Student()
student2 = Student()

print(student1)
print(student2)


# ------------------------------------------------------------
# 3️⃣ ATTRIBUTES
# ------------------------------------------------------------

class Student:

    name = "Trupti"
    course = "B.Sc IT"
    age = 20


student1 = Student()

print(student1.name)
print(student1.course)
print(student1.age)


# ------------------------------------------------------------
# 4️⃣ __init__() METHOD
# ------------------------------------------------------------

# __init__() object create hote hi automatically run hota hai.

class Student:

    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course


student1 = Student("Trupti", 20, "B.Sc IT")

print(student1.name)
print(student1.age)
print(student1.course)


# ------------------------------------------------------------
# 5️⃣ self KYA HAI?
# ------------------------------------------------------------

# self current object ko represent karta hai.

class Student:

    def __init__(self, name):
        self.name = name


student1 = Student("Trupti")
student2 = Student("Riya")

print(student1.name)
print(student2.name)


# ------------------------------------------------------------
# 6️⃣ METHODS
# ------------------------------------------------------------

# Class ke andar function ko METHOD kehte hain.

class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print("Name:", self.name)
        print("Marks:", self.marks)


student1 = Student("Trupti", 85)

student1.display()


# ------------------------------------------------------------
# 7️⃣ METHOD WITH CALCULATION
# ------------------------------------------------------------

class Student:

    def __init__(self, name, marks1, marks2, marks3):
        self.name = name
        self.marks1 = marks1
        self.marks2 = marks2
        self.marks3 = marks3

    def total(self):
        return self.marks1 + self.marks2 + self.marks3

    def average(self):
        return self.total() / 3


student1 = Student("Trupti", 85, 90, 80)

print("Name:", student1.name)
print("Total:", student1.total())
print("Average:", student1.average())


# ------------------------------------------------------------
# 8️⃣ MULTIPLE OBJECTS
# ------------------------------------------------------------

class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print(self.name, "-", self.marks)


student1 = Student("Trupti", 85)
student2 = Student("Riya", 92)
student3 = Student("Nensi", 78)

student1.display()
student2.display()
student3.display()


# ------------------------------------------------------------
# 9️⃣ MODIFY OBJECT DATA
# ------------------------------------------------------------

student1.marks = 95

print(student1.marks)


# ------------------------------------------------------------
# 🔟 DELETE ATTRIBUTE
# ------------------------------------------------------------

del student1.marks

# print(student1.marks)
# This will give AttributeError because marks was deleted.


# ------------------------------------------------------------
# 1️⃣1️⃣ STRING METHOD __str__()
# ------------------------------------------------------------

class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def __str__(self):
        return f"{self.name} - {self.marks}"


student1 = Student("Trupti", 85)

print(student1)


# ============================================================
# 📝 PRACTICE QUESTIONS + ANSWERS
# ============================================================

# Q1. Create a class named Car.

class Car:
    pass

car1 = Car()

print(car1)


# Q2. Create a Student class with name and age.

class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age


student = Student("Trupti", 20)

print(student.name)
print(student.age)


# Q3. Create a class Employee with name and salary.

class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


employee = Employee("Trupti", 30000)

print(employee.name)
print(employee.salary)


# Q4. Create a method to display employee information.

class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display(self):
        print("Name:", self.name)
        print("Salary:", self.salary)


employee = Employee("Trupti", 30000)

employee.display()


# Q5. Create a Rectangle class and calculate area.

class Rectangle:

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


rectangle = Rectangle(10, 5)

print("Area:", rectangle.area())


# Q6. Create a Circle class and calculate area.

class Circle:

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius


circle = Circle(5)

print("Area:", circle.area())


# Q7. Create a Student class and calculate average marks.

class Student:

    def __init__(self, name, m1, m2, m3):
        self.name = name
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def average(self):
        return (self.m1 + self.m2 + self.m3) / 3


student = Student("Trupti", 80, 90, 85)

print("Average:", student.average())


# Q8. Create a method that checks Pass/Fail.

class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def result(self):

        if self.marks >= 40:
            return "Pass"
        else:
            return "Fail"


student = Student("Trupti", 75)

print(student.result())


# Q9. Create a BankAccount class with deposit.

class BankAccount:

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount


account = BankAccount("Trupti", 5000)

account.deposit(2000)

print("Balance:", account.balance)


# Q10. Create a method to withdraw money.

class BankAccount:

    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):

        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawal successful")
        else:
            print("Insufficient balance")


account = BankAccount(5000)

account.withdraw(2000)

print("Remaining:", account.balance)


# ============================================================
# 🚀 MINI PROJECT – STUDENT MANAGEMENT SYSTEM
# ============================================================

class Student:

    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course
        self.marks = []

    # Add marks
    def add_marks(self, mark):
        self.marks.append(mark)

    # Calculate total
    def total(self):
        return sum(self.marks)

    # Calculate average
    def average(self):

        if len(self.marks) == 0:
            return 0

        return self.total() / len(self.marks)

    # Check result
    def result(self):

        if self.average() >= 40:
            return "PASS"
        else:
            return "FAIL"

    # Display student information
    def display(self):

        print("\n========== STUDENT DETAILS ==========")

        print("Name:", self.name)
        print("Age:", self.age)
        print("Course:", self.course)
        print("Marks:", self.marks)
        print("Total:", self.total())
        print("Average:", round(self.average(), 2))
        print("Result:", self.result())


# ------------------------------------------------------------
# Create Student Object
# ------------------------------------------------------------

student = Student(
    "Trupti",
    20,
    "B.Sc IT"
)


# ------------------------------------------------------------
# Add Marks
# ------------------------------------------------------------

student.add_marks(85)
student.add_marks(90)
student.add_marks(78)


# ------------------------------------------------------------
# Display Result
# ------------------------------------------------------------

student.display()


# ============================================================
# ⭐ IMPORTANT INTERVIEW QUESTIONS
# ============================================================

# Q1. What is OOP?
# Answer:
# OOP means Object-Oriented Programming.
# It organizes programs using classes and objects.


# Q2. What is a class?
# Answer:
# A class is a blueprint/template for creating objects.


# Q3. What is an object?
# Answer:
# An object is an instance of a class.


# Q4. What is __init__()?
# Answer:
# __init__() is a constructor-like method.
# It automatically runs when an object is created.


# Q5. What is self?
# Answer:
# self refers to the current object.


# Q6. What is a method?
# Answer:
# A function defined inside a class is called a method.
