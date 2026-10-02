# ============================================================
# 🐍 DAY 18 – OOP ADVANCED
# ============================================================

# OOP ke important concepts:
#
# 1. Inheritance
# 2. Encapsulation
# 3. Polymorphism
# 4. super()
# 5. Method Overriding


# ============================================================
# 1️⃣ INHERITANCE
# ============================================================

# Inheritance ka matlab:
# Ek class dusri class ke properties aur methods use kar sakti hai.

# Parent Class
class Animal:

    def eat(self):
        print("Animal is eating")


# Child Class
class Dog(Animal):

    def bark(self):
        print("Dog is barking")


dog = Dog()

dog.eat()     # Parent class method
dog.bark()    # Child class method


# ============================================================
# 2️⃣ INHERITANCE WITH __init__()
# ============================================================

class Person:

    def __init__(self, name):
        self.name = name

    def display_name(self):
        print("Name:", self.name)


class Student(Person):

    def __init__(self, name, course):
        self.name = name
        self.course = course

    def display_course(self):
        print("Course:", self.course)


student = Student("Trupti", "B.Sc IT")

student.display_name()
student.display_course()


# ============================================================
# 3️⃣ super()
# ============================================================

# super() ka use parent class ke constructor/method ko
# call karne ke liye hota hai.

class Person:

    def __init__(self, name):
        self.name = name


class Student(Person):

    def __init__(self, name, course):

        # Parent class ka __init__()
        super().__init__(name)

        self.course = course


student = Student("Trupti", "B.Sc IT")

print(student.name)
print(student.course)


# ============================================================
# 4️⃣ METHOD OVERRIDING
# ============================================================

# Child class parent ke same method ko apne according
# define kare = Method Overriding

class Animal:

    def sound(self):
        print("Animal makes sound")


class Dog(Animal):

    def sound(self):
        print("Dog says Woof")


class Cat(Animal):

    def sound(self):
        print("Cat says Meow")


dog = Dog()
cat = Cat()

dog.sound()
cat.sound()


# ============================================================
# 5️⃣ POLYMORPHISM
# ============================================================

# Polymorphism = Same method name,
# different behavior.

class Dog:

    def sound(self):
        print("Woof")


class Cat:

    def sound(self):
        print("Meow")


class Cow:

    def sound(self):
        print("Moo")


animals = [Dog(), Cat(), Cow()]

for animal in animals:
    animal.sound()


# ============================================================
# 6️⃣ POLYMORPHISM WITH FUNCTION
# ============================================================

class Student:

    def info(self):
        print("This is Student")


class Teacher:

    def info(self):
        print("This is Teacher")


def show_info(person):
    person.info()


student = Student()
teacher = Teacher()

show_info(student)
show_info(teacher)


# ============================================================
# 7️⃣ ENCAPSULATION
# ============================================================

# Encapsulation = Data ko class ke andar protect karna.
#
# Python mein:
#
# Public    → name
# Protected → _name
# Private   → __name


# Public
class Student:

    def __init__(self):
        self.name = "Trupti"


student = Student()

print(student.name)


# Protected
class Student:

    def __init__(self):
        self._name = "Trupti"


student = Student()

print(student._name)


# Private
class Student:

    def __init__(self):
        self.__name = "Trupti"

    def get_name(self):
        return self.__name


student = Student()

print(student.get_name())


# Direct access:
# print(student.__name)
#
# This normally gives AttributeError.


# ============================================================
# 8️⃣ GETTER AND SETTER
# ============================================================

class Student:

    def __init__(self, name):
        self.__name = name

    # Getter
    def get_name(self):
        return self.__name

    # Setter
    def set_name(self, name):
        self.__name = name


student = Student("Trupti")

print(student.get_name())

student.set_name("Riya")

print(student.get_name())


# ============================================================
# 9️⃣ PRACTICAL EXAMPLE – BANK ACCOUNT
# ============================================================

class BankAccount:

    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):

        if amount > 0:
            self.__balance += amount
            print("Amount deposited")

    def withdraw(self, amount):

        if amount <= self.__balance:
            self.__balance -= amount
            print("Withdrawal successful")

        else:
            print("Insufficient balance")

    def get_balance(self):
        return self.__balance


account = BankAccount(5000)

account.deposit(2000)

print("Balance:", account.get_balance())

account.withdraw(1000)

print("Balance:", account.get_balance())


# ============================================================
# 🔟 MULTILEVEL INHERITANCE
# ============================================================

# Grandparent → Parent → Child

class Grandparent:

    def family(self):
        print("Grandparent")


class Parent(Grandparent):

    def parents(self):
        print("Parent")


class Child(Parent):

    def child(self):
        print("Child")


obj = Child()

obj.family()
obj.parents()
obj.child()


# ============================================================
# 1️⃣1️⃣ MULTIPLE INHERITANCE
# ============================================================

# One child class can inherit from multiple classes.

class Father:

    def father_property(self):
        print("Father's property")


class Mother:

    def mother_property(self):
        print("Mother's property")


class Child(Father, Mother):

    def child_property(self):
        print("Child's property")


child = Child()

child.father_property()
child.mother_property()
child.child_property()


# ============================================================
# 📝 PRACTICE QUESTIONS + ANSWERS
# ============================================================

# Q1. Create a parent class Vehicle and child class Car.

class Vehicle:

    def start(self):
        print("Vehicle started")


class Car(Vehicle):

    def drive(self):
        print("Car is driving")


car = Car()

car.start()
car.drive()


# ------------------------------------------------------------
# Q2. Create Person and Student using inheritance.
# ------------------------------------------------------------

class Person:

    def __init__(self, name):
        self.name = name


class Student(Person):

    def __init__(self, name, course):
        super().__init__(name)
        self.course = course


student = Student("Trupti", "B.Sc IT")

print(student.name)
print(student.course)


# ------------------------------------------------------------
# Q3. Demonstrate method overriding.
# ------------------------------------------------------------

class Animal:

    def sound(self):
        print("Animal sound")


class Dog(Animal):

    def sound(self):
        print("Woof")


dog = Dog()

dog.sound()


# ------------------------------------------------------------
# Q4. Demonstrate polymorphism.
# ------------------------------------------------------------

class Bike:

    def move(self):
        print("Bike is moving")


class Car:

    def move(self):
        print("Car is moving")


vehicles = [Bike(), Car()]

for vehicle in vehicles:
    vehicle.move()


# ------------------------------------------------------------
# Q5. Create private variable.
# ------------------------------------------------------------

class Employee:

    def __init__(self, salary):
        self.__salary = salary

    def get_salary(self):
        return self.__salary


employee = Employee(30000)

print(employee.get_salary())


# ------------------------------------------------------------
# Q6. Create setter and getter.
# ------------------------------------------------------------

class Student:

    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name


student = Student("Trupti")

print(student.get_name())

student.set_name("Nensi")

print(student.get_name())


# ------------------------------------------------------------
# Q7. Create multilevel inheritance.
# ------------------------------------------------------------

class A:

    def method_a(self):
        print("Class A")


class B(A):

    def method_b(self):
        print("Class B")


class C(B):

    def method_c(self):
        print("Class C")


obj = C()

obj.method_a()
obj.method_b()
obj.method_c()


# ------------------------------------------------------------
# Q8. Create multiple inheritance.
# ------------------------------------------------------------

class Father:

    def father(self):
        print("Father")


class Mother:

    def mother(self):
        print("Mother")


class Child(Father, Mother):

    pass


child = Child()

child.father()
child.mother()


# ------------------------------------------------------------
# Q9. Use super() to call parent constructor.
# ------------------------------------------------------------

class Employee:

    def __init__(self, name):
        self.name = name


class Manager(Employee):

    def __init__(self, name, department):

        super().__init__(name)

        self.department = department


manager = Manager("Trupti", "IT")

print(manager.name)
print(manager.department)


# ------------------------------------------------------------
# Q10. Create BankAccount using encapsulation.
# ------------------------------------------------------------

class BankAccount:

    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance


account = BankAccount(5000)

account.deposit(1500)

print(account.get_balance())


# ============================================================
# 🚀 MINI PROJECT – EMPLOYEE MANAGEMENT SYSTEM
# ============================================================

class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display(self):
        print("Name:", self.name)
        print("Salary:", self.salary)


class Developer(Employee):

    def __init__(self, name, salary, language):

        super().__init__(name, salary)

        self.language = language

    def display(self):

        print("\n===== DEVELOPER =====")

        print("Name:", self.name)
        print("Salary:", self.salary)
        print("Language:", self.language)


class Manager(Employee):

    def __init__(self, name, salary, team_size):

        super().__init__(name, salary)

        self.team_size = team_size

    def display(self):

        print("\n===== MANAGER =====")

        print("Name:", self.name)
        print("Salary:", self.salary)
        print("Team Size:", self.team_size)


# Create objects

developer = Developer(
    "Trupti",
    40000,
    "Python"
)

manager = Manager(
    "Riya",
    60000,
    8
)


# Display information

developer.display()
manager.display()


# ============================================================
# ⭐ IMPORTANT INTERVIEW QUESTIONS
# ============================================================

# Q1. What is Inheritance?
# Answer:
# Inheritance allows a child class to use properties
# and methods of a parent class.


# Q2. What is Polymorphism?
# Answer:
# Same method/interface can behave differently
# for different objects.


# Q3. What is Encapsulation?
# Answer:
# Encapsulation means keeping data and methods together
# and controlling access to the data.


# Q4. What is Method Overriding?
# Answer:
# When a child class provides its own implementation
# of a parent class method.


# Q5. What is super()?
# Answer:
# super() is used to access parent class methods
# or constructor.

# 🧠 EASY REVISION

# Inheritance
# Parent → Child
#
# Encapsulation
# Data protection
#
# Polymorphism
# Same method → Different behavior
#
# super()
# Child → Parent
#
# Method Overriding
# Child changes parent's method

