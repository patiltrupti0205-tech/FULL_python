# function

def greet():
    print("hello world")
greet()

# function with prameters

def greet (name):
    print("hello",name)

greet("Trupti")

# multiple parameters
def add(a,b):
   print(a+b)

add(10,20)

# return statement

def add(a,b):
    return a+b

result = add(5,7)
print(result)

# default parameter

def country(name="India"):
    print(name)

country()
country("USA")

# keyword arguments

def student(name,age):
    print(name,age)

student(age=20,name="Rahul")

# arbitrary arguments(*args)

def numbers(*num):
    print(num)

numbers(1,2,3,4)

# keyword arbitrary arguments(**kwargs)

def info(**data):
    print(data)
info(name="rahul",age=21)

# lambda function

square = lambda x: x * x
print(square(5))

# scope

x =100

def test():
    x = 50
    print(x)

test()
print(x)

# student result management system

def calculate_total(marks):
    return sum(marks)


def calculate_percentage(total, subjects):
    return total / subjects


def calculate_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    else:
        return "F"


def display_result(name, marks):
    total = calculate_total(marks)
    percentage = calculate_percentage(total, len(marks))
    grade = calculate_grade(percentage)

    print("\n------------ STUDENT RESULT -------------")
    print("Student Name :", name)
    print("Marks        :", marks)
    print("Total        :", total)
    print("Percentage   :", round(percentage, 2), "%")
    print("Grade        :", grade)
    print("--------------------------------------")

# Main Program
name = input("Enter Student Name: ")

subjects = int(input("Enter Number of Subjects: "))

marks = []

for i in range(subjects):
    mark = float(input(f"Enter Marks of Subject {i+1}: "))
    marks.append(mark)

display_result(name, marks)

print("we cover this all topics!") 
# function
# calling a function
# parameters & arguments
# return statement
# default parameters
# keyword arguments
# *args
# **kwargs
# lambda function
# vaariable scope
# mini project
    #  Functions
    #  Parameters & Return
    #  Lists
    #  Loops (for)    
    #  Conditions (if-elif-else)
    #  User Input
    #  Built-in Functions (sum(), len(), round())
