
# ============================================================
# 🐍 DAY 19 – ITERATORS & GENERATORS
# ============================================================

# Today we learn:
# 1. Iterable
# 2. Iterator
# 3. iter()
# 4. next()
# 5. Generator
# 6. yield
# 7. Generator with loop
# 8. Generator expressions
# 9. Practical mini project


# ============================================================
# 1️⃣ ITERABLE
# ============================================================

# Iterable = jis object ke elements ko loop se access kar sakte hain.
#
# Examples:
# list
# tuple
# string
# dictionary
# set

numbers = [10, 20, 30, 40]

for number in numbers:
    print(number)


# ============================================================
# 2️⃣ ITERATOR
# ============================================================

# Iterator ek object hai jo values ko ek-ek karke deta hai.

numbers = [10, 20, 30]

iterator = iter(numbers)

print(next(iterator))
print(next(iterator))
print(next(iterator))


# Output:
# 10
# 20
# 30


# ============================================================
# 3️⃣ iter() FUNCTION
# ============================================================

numbers = [100, 200, 300]

iterator = iter(numbers)

print(iterator)


# ============================================================
# 4️⃣ next() FUNCTION
# ============================================================

numbers = [10, 20, 30]

iterator = iter(numbers)

print(next(iterator))   # 10
print(next(iterator))   # 20
print(next(iterator))   # 30

# Agar aur next() karenge:
# print(next(iterator))
#
# StopIteration error aayega.


# ============================================================
# 5️⃣ ITERATOR WITH WHILE LOOP
# ============================================================

numbers = [10, 20, 30, 40]

iterator = iter(numbers)

while True:

    try:
        value = next(iterator)
        print(value)

    except StopIteration:
        break


# ============================================================
# 6️⃣ STRING ITERATOR
# ============================================================

name = "Trupti"

iterator = iter(name)

print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))


# ============================================================
# 7️⃣ TUPLE ITERATOR
# ============================================================

data = ("Python", "Cloud", "AI")

iterator = iter(data)

print(next(iterator))
print(next(iterator))
print(next(iterator))


# ============================================================
# 8️⃣ CUSTOM ITERATOR
# ============================================================

class MyNumbers:

    def __iter__(self):
        self.number = 1
        return self

    def __next__(self):

        if self.number <= 5:
            value = self.number
            self.number += 1
            return value

        else:
            raise StopIteration


numbers = MyNumbers()

for number in numbers:
    print(number)


# ============================================================
# 9️⃣ GENERATOR
# ============================================================

# Generator ek special type ka function hota hai.
#
# Generator mein "yield" use hota hai.
#
# yield value ko ek-ek karke return karta hai.


def numbers():

    yield 1
    yield 2
    yield 3
    yield 4


result = numbers()

print(next(result))
print(next(result))
print(next(result))
print(next(result))


# ============================================================
# 🔟 GENERATOR WITH FOR LOOP
# ============================================================

def count_numbers():

    yield 1
    yield 2
    yield 3
    yield 4
    yield 5


for number in count_numbers():
    print(number)


# ============================================================
# 1️⃣1️⃣ GENERATOR USING RANGE
# ============================================================

def numbers(n):

    for i in range(1, n + 1):
        yield i


for number in numbers(5):
    print(number)


# ============================================================
# 1️⃣2️⃣ GENERATOR FOR EVEN NUMBERS
# ============================================================

def even_numbers(n):

    for i in range(1, n + 1):

        if i % 2 == 0:
            yield i


for number in even_numbers(10):
    print(number)


# ============================================================
# 1️⃣3️⃣ GENERATOR FOR SQUARES
# ============================================================

def squares(n):

    for i in range(1, n + 1):
        yield i * i


for value in squares(5):
    print(value)


# ============================================================
# 1️⃣4️⃣ GENERATOR FOR ODD NUMBERS
# ============================================================

def odd_numbers(n):

    for i in range(1, n + 1):

        if i % 2 != 0:
            yield i


for number in odd_numbers(10):
    print(number)


# ============================================================
# 1️⃣5️⃣ GENERATOR EXPRESSION
# ============================================================

# List comprehension:
squares_list = [x * x for x in range(1, 6)]

print(squares_list)


# Generator expression:
squares_generator = (x * x for x in range(1, 6))

print(squares_generator)

print(next(squares_generator))
print(next(squares_generator))
print(next(squares_generator))


# ============================================================
# 1️⃣6️⃣ GENERATOR VS LIST
# ============================================================

# List stores all values in memory.

numbers_list = [x for x in range(1, 6)]

print(numbers_list)


# Generator gives values one-by-one.

numbers_generator = (x for x in range(1, 6))

for number in numbers_generator:
    print(number)


# ============================================================
# 1️⃣7️⃣ LARGE DATA EXAMPLE
# ============================================================

# Generator large data ke liye useful hota hai.

def large_numbers():

    for i in range(1, 1000000):
        yield i


numbers = large_numbers()

print(next(numbers))
print(next(numbers))
print(next(numbers))

# Puri list ek saath memory mein store nahi hoti.


# ============================================================
# 📝 PRACTICE QUESTIONS + ANSWERS
# ============================================================

# Q1. Create an iterator from a list.

numbers = [10, 20, 30, 40]

iterator = iter(numbers)

print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))


# ------------------------------------------------------------
# Q2. Create iterator from a string.
# ------------------------------------------------------------

name = "Python"

iterator = iter(name)

print(next(iterator))
print(next(iterator))
print(next(iterator))


# ------------------------------------------------------------
# Q3. Create a generator that gives 1 to 5.
# ------------------------------------------------------------

def numbers():

    for i in range(1, 6):
        yield i


for number in numbers():
    print(number)


# ------------------------------------------------------------
# Q4. Create a generator for even numbers.
# ------------------------------------------------------------

def even_numbers(n):

    for i in range(1, n + 1):

        if i % 2 == 0:
            yield i


for number in even_numbers(20):
    print(number)


# ------------------------------------------------------------
# Q5. Create a generator for squares.
# ------------------------------------------------------------

def squares(n):

    for i in range(1, n + 1):
        yield i * i


for value in squares(10):
    print(value)


# ------------------------------------------------------------
# Q6. Create a generator for odd numbers.
# ------------------------------------------------------------

def odd_numbers(n):

    for i in range(1, n + 1):

        if i % 2 != 0:
            yield i


for number in odd_numbers(10):
    print(number)


# ------------------------------------------------------------
# Q7. Create a generator for multiplication table.
# ------------------------------------------------------------

def table(number):

    for i in range(1, 11):
        yield number * i


for value in table(5):
    print(value)


# ------------------------------------------------------------
# Q8. Create a generator that counts from 10 to 1.
# ------------------------------------------------------------

def countdown():

    for i in range(10, 0, -1):
        yield i


for number in countdown():
    print(number)


# ------------------------------------------------------------
# Q9. Create a generator for numbers divisible by 5.
# ------------------------------------------------------------

def divisible_by_5(n):

    for i in range(1, n + 1):

        if i % 5 == 0:
            yield i


for number in divisible_by_5(50):
    print(number)


# ------------------------------------------------------------
# Q10. Create a generator that returns names one by one.
# ------------------------------------------------------------

def names():

    data = ["Trupti", "Riya", "Nensi", "Priya"]

    for name in data:
        yield name


for name in names():
    print(name)


# ============================================================
# 🚀 MINI PROJECT – NUMBER GENERATOR
# ============================================================

def number_generator(start, end):

    for number in range(start, end + 1):
        yield number


print("\n========== NUMBER GENERATOR ==========")

start = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))

for number in number_generator(start, end):
    print(number)


# ============================================================
# 🚀 MINI PROJECT 2 – STUDENT MARKS GENERATOR
# ============================================================

def marks_generator():

    marks = [85, 90, 78, 92, 88]

    for mark in marks:
        yield mark


print("\n========== STUDENT MARKS ==========")

total = 0
count = 0

for mark in marks_generator():

    print("Mark:", mark)

    total += mark
    count += 1


average = total / count

print("Total:", total)
print("Average:", average)


# ============================================================
# ⭐ IMPORTANT INTERVIEW QUESTIONS
# ============================================================

# Q1. What is an Iterable?
#
# Answer:
# An object whose elements can be accessed one by one.
#
# Example:
# list, tuple, string


# Q2. What is an Iterator?
#
# Answer:
# An object that gives values one at a time.
#
# iter() and next() are commonly used.


# Q3. What is Generator?
#
# Answer:
# A special function that produces values one at a time
# using yield.


# Q4. What is yield?
#
# Answer:
# yield returns a value from a generator and pauses
# the function until the next value is requested.


# Q5. Difference between return and yield?
#
# return:
# Function ends.
#
# yield:
# Function pauses and can continue later.


# Q6. Why use generators?
#
# Answer:
# Generators are memory efficient because they produce
# values one at a time instead of storing all values.



# ============================================================
# 📌 ITERATOR VS GENERATOR
# ============================================================

# Iterator:
# Usually created using iter()
# Uses next()
# Can also create custom iterator using __iter__ and __next__


# Generator:
# Created using a function with yield
# Easier to write
# Memory efficient
# Produces values one by one

