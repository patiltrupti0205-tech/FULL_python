#operators
#arethmrtic operators

a = 10
b = 3

print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)
print(a**b)
print(a//b)

#comparison operators

x = 10
y = 20

print(x==y)
print(x!=y)
print(x>y)
print(x<y)
print(x<=y)
print(x>=y)

#Logical operators

age = 20

print(age>18 and age<30)
print(age>18 or age>50)
print(not(age>18))

#assignment operators 

x = 10

x += 5
print(x)

x -= 2
print(x)

x *= 3
print(x)

x /= 2
print(x)

#taking input from user

name = input("Enter your name:")

print("hy", name)

age = input("enter your age:")

print("My age is:", age)

#Type conversion

num = "100"
print(type(num))

num=int(num)
print(type(num))

#example

a= float(20)
b= str(50)
c= bool(1)

print(a)
print(b)
print(c)

#Conditional statments

#if

age =int(input("Enter your age:"))

if age >= 18 :
    print("you can vote.")

# # if else
 
marks = int(input("Enter marks:"))

if marks >=35:
    print("you are pass")
else:
    print("you are fail")

# Nested if

age =  int(input("Enter age:"))
license = input("do you have license?")

if age >= 18:
    if license =="yes":
        print("you can drive.")
    else:
        print("get a driving license first")
else:
     print("you are underage")

# if-elif-alse

marks = int(input("Enter marks: "))

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Fail")

#todays practice programs 

# even or odd

num = int(input("enter a number:"))

if num % 2 == 0:
    print("the number is even!")

else: 
    print("the number is odd!")

#largest of two numbers

a = int(input("enter a first number:"))
b = int(input("enter a secound number:"))

if a > b:
    print(a,"is greater then b!")
else :  
    print(b,"is greater than a! ")   

#simple calculator

a = int(input("enter firsst number: "))
b= int(input("Enter a secound number:"))

print("1.add")
print("2.sub")
print("3.mul")
print("4.div")

choice = int (input("ENTER YOUR CHOICE: "))

if choice == 1:
    print(a+b)
elif choice == 2:
    print(a-b)
elif choice == 3:
    print(a*b)
elif  choice == 4:
    print(a/b)
else:
    print("invalid choice!")

#votinng eligibility
age =  int(input("enter your age:"))

if age >=18:
    print("eligible")
else :
    print("not eligible")

#find the largest of three numbers

a=int(input("enter 1 number:"))
b=int(input("enter 2 number:"))
c=int(input("enter 3 number:"))

if a >= b and a>=c:
    print("a is big number")

elif b>=a and b>=c:
    print("b is big")

else:
    print("c is big")

#leap year

year = int(input("Enter a year: "))

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print("Leap Year")
else:
    print("Not a Leap Year")


# positive,nagative or zero

num = float(input("Enter a number: "))

if num > 0:
    print("Positive Number")
elif num < 0:
    print("Negative Number")
else:
    print("Zero")

#    simple ATM menu

balance = 5000

print("1. Check Balance")
print("2. Deposit")
print("3. Withdraw")

choice = int(input("Enter your choice: "))

if choice == 1:
    print("Your balance is:", balance)

elif choice == 2:
    amount = float(input("Enter deposit amount: "))
    balance += amount
    print("Updated balance:", balance)

elif choice == 3:
    amount = float(input("Enter withdraw amount: "))

    if amount <= balance:
        balance -= amount
        print("Please collect your cash.")
        print("Remaining balance:", balance)
    else:
        print("Insufficient Balance")

else:
    print("Invalid Choice")

# vowelor consonant

ch = input("Enter a character: ")

if ch == "a" or ch == "e" or ch == "i" or ch == "o" or ch == "u" or ch == "A" or ch == "E" or ch == "I" or ch == "O" or ch == "U":
    print("Vowel")
else:
    print("Consonant")

# calculator

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

operator = input("Enter operator (+, -, *, /): ")

if operator == "+":
    print("Answer =", num1 + num2)

elif operator == "-":
    print("Answer =", num1 - num2)

elif operator == "*":
    print("Answer =", num1 * num2)

elif operator == "/":
    if num2 != 0:
        print("Answer =", num1 / num2)
    else:
        print("Cannot divide by zero")

else:
    print("Invalid Operator")