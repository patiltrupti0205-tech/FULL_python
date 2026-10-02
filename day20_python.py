# ============================================================
# DAY 20 – MAP, FILTER, REDUCE & LAMBDA
# ============================================================

# Today we learn:
#
# 1. Lambda Function
# 2. map()
# 3. filter()
# 4. reduce()
# 5. Combining map + filter
# 6. Practical Mini Project


# ============================================================
# 1️⃣ NORMAL FUNCTION
# ============================================================

def square(number):
    return number * number

print(square(5))


# ============================================================
# 2️⃣ LAMBDA FUNCTION
# ============================================================

# Lambda = small one-line anonymous function
#
# Syntax:
# lambda arguments: expression

square = lambda x: x * x

print(square(5))


# Another example

add = lambda a, b: a + b

print(add(10, 20))


# Subtraction

subtract = lambda a, b: a - b

print(subtract(20, 5))


# Multiplication

multiply = lambda a, b: a * b

print(multiply(5, 4))


# Division

divide = lambda a, b: a / b

print(divide(20, 5))


# ============================================================
# 3️⃣ LAMBDA WITH IF-ELSE
# ============================================================

check = lambda x: "Even" if x % 2 == 0 else "Odd"

print(check(10))
print(check(7))


# Find maximum

maximum = lambda a, b: a if a > b else b

print(maximum(10, 20))


# ============================================================
# 4️⃣ map()
# ============================================================

# map() kisi function ko list ke har element par apply karta hai.
#
# Syntax:
# map(function, iterable)


numbers = [1, 2, 3, 4, 5]

result = map(lambda x: x * x, numbers)

print(list(result))


# Output:
# [1, 4, 9, 16, 25]


# ============================================================
# 5️⃣ map() – DOUBLE NUMBERS
# ============================================================

numbers = [10, 20, 30, 40]

double = map(lambda x: x * 2, numbers)

print(list(double))


# ============================================================
# 6️⃣ map() – ADD 10
# ============================================================

numbers = [10, 20, 30, 40]

result = map(lambda x: x + 10, numbers)

print(list(result))


# ============================================================
# 7️⃣ map() – UPPERCASE
# ============================================================

names = ["trupti", "riya", "nensi"]

upper_names = map(lambda name: name.upper(), names)

print(list(upper_names))


# ============================================================
# 8️⃣ map() – CONVERT STRING TO INTEGER
# ============================================================

numbers = ["10", "20", "30", "40"]

result = map(int, numbers)

print(list(result))


# ============================================================
# 9️⃣ filter()
# ============================================================

# filter() condition ke according elements select karta hai.
#
# Syntax:
# filter(function, iterable)


numbers = [1, 2, 3, 4, 5, 6]

even = filter(lambda x: x % 2 == 0, numbers)

print(list(even))


# ============================================================
# 🔟 FILTER ODD NUMBERS
# ============================================================

numbers = [1, 2, 3, 4, 5, 6, 7, 8]

odd = filter(lambda x: x % 2 != 0, numbers)

print(list(odd))


# ============================================================
# 1️⃣1️⃣ FILTER NUMBERS GREATER THAN 50
# ============================================================

numbers = [20, 45, 60, 75, 30, 90]

result = filter(lambda x: x > 50, numbers)

print(list(result))


# ============================================================
# 1️⃣2️⃣ FILTER PASSING MARKS
# ============================================================

marks = [35, 45, 67, 20, 89, 30, 76]

passed = filter(lambda mark: mark >= 40, marks)

print(list(passed))


# ============================================================
# 1️⃣3️⃣ FILTER NAMES
# ============================================================

names = ["Trupti", "Riya", "Nensi", "Priya"]

result = filter(lambda name: len(name) > 5, names)

print(list(result))


# ============================================================
# 1️⃣4️⃣ reduce()
# ============================================================

# reduce() multiple values ko combine karke
# ek final value deta hai.
#
# reduce() functools module mein hota hai.

from functools import reduce


numbers = [1, 2, 3, 4, 5]

total = reduce(lambda a, b: a + b, numbers)

print(total)

# 1 + 2 + 3 + 4 + 5 = 15


# ============================================================
# 1️⃣5️⃣ REDUCE – MULTIPLICATION
# ============================================================

numbers = [1, 2, 3, 4, 5]

result = reduce(lambda a, b: a * b, numbers)

print(result)

# 1 * 2 * 3 * 4 * 5 = 120


# ============================================================
# 1️⃣6️⃣ REDUCE – FIND MAXIMUM
# ============================================================

numbers = [10, 50, 20, 90, 40]

maximum = reduce(
    lambda a, b: a if a > b else b,
    numbers
)

print(maximum)


# ============================================================
# 1️⃣7️⃣ MAP + FILTER
# ============================================================

# First filter even numbers
# Then square them.

numbers = [1, 2, 3, 4, 5, 6]

even = filter(lambda x: x % 2 == 0, numbers)

squares = map(lambda x: x * x, even)

print(list(squares))


# Output:
# [4, 16, 36]


# ============================================================
# 1️⃣8️⃣ FILTER + MAP
# ============================================================

marks = [30, 45, 60, 25, 80, 90]

# Only passing marks
passed = filter(lambda x: x >= 40, marks)

# Add 5 bonus marks
updated = map(lambda x: x + 5, passed)

print(list(updated))


# ============================================================
# 1️⃣9️⃣ MAP + FILTER + REDUCE
# ============================================================

numbers = [1, 2, 3, 4, 5, 6]

# Step 1: even numbers
even = filter(lambda x: x % 2 == 0, numbers)

# Step 2: square
squares = map(lambda x: x * x, even)

# Step 3: total
total = reduce(lambda a, b: a + b, squares)

print("Total:", total)

# 2² + 4² + 6²
# = 4 + 16 + 36
# = 56


# ============================================================
# 📝 PRACTICE QUESTIONS + ANSWERS
# ============================================================


# Q1. Create a lambda function to find square.

square = lambda x: x * x

print(square(7))


# ------------------------------------------------------------
# Q2. Create lambda function to find cube.
# ------------------------------------------------------------

cube = lambda x: x ** 3

print(cube(3))


# ------------------------------------------------------------
# Q3. Use map() to double all numbers.
# ------------------------------------------------------------

numbers = [1, 2, 3, 4, 5]

result = map(lambda x: x * 2, numbers)

print(list(result))


# ------------------------------------------------------------
# Q4. Use map() to convert names into uppercase.
# ------------------------------------------------------------

names = ["trupti", "riya", "nensi"]

result = map(lambda name: name.upper(), names)

print(list(result))


# ------------------------------------------------------------
# Q5. Use filter() to find even numbers.
# ------------------------------------------------------------

numbers = [1, 2, 3, 4, 5, 6, 7, 8]

result = filter(lambda x: x % 2 == 0, numbers)

print(list(result))


# ------------------------------------------------------------
# Q6. Use filter() to find numbers greater than 50.
# ------------------------------------------------------------

numbers = [20, 60, 40, 80, 90]

result = filter(lambda x: x > 50, numbers)

print(list(result))


# ------------------------------------------------------------
# Q7. Use filter() to find passing marks.
# ------------------------------------------------------------

marks = [25, 45, 67, 30, 80]

result = filter(lambda x: x >= 40, marks)

print(list(result))


# ------------------------------------------------------------
# Q8. Use reduce() to find total.
# ------------------------------------------------------------

from functools import reduce

numbers = [10, 20, 30, 40]

total = reduce(lambda a, b: a + b, numbers)

print(total)


# ------------------------------------------------------------
# Q9. Use reduce() to multiply all numbers.
# ------------------------------------------------------------

numbers = [1, 2, 3, 4]

result = reduce(lambda a, b: a * b, numbers)

print(result)


# ------------------------------------------------------------
# Q10. Find square of only even numbers.
# ------------------------------------------------------------

numbers = [1, 2, 3, 4, 5, 6]

even = filter(lambda x: x % 2 == 0, numbers)

squares = map(lambda x: x * x, even)

print(list(squares))


# ------------------------------------------------------------
# Q11. Add 10 to numbers greater than 50.
# ------------------------------------------------------------

numbers = [30, 55, 70, 40, 90]

greater = filter(lambda x: x > 50, numbers)

result = map(lambda x: x + 10, greater)

print(list(result))


# ------------------------------------------------------------
# Q12. Find total of squares of even numbers.
# ------------------------------------------------------------

numbers = [1, 2, 3, 4, 5, 6]

even = filter(lambda x: x % 2 == 0, numbers)

squares = map(lambda x: x * x, even)

total = reduce(lambda a, b: a + b, squares)

print(total)


# ============================================================
# 🚀 MINI PROJECT – STUDENT MARKS ANALYZER
# ============================================================

from functools import reduce


marks = [35, 45, 67, 80, 25, 90, 55, 30]


print("\n========== STUDENT MARKS ANALYZER ==========")

print("Original Marks:", marks)


# ------------------------------------------------------------
# 1. Passing students
# ------------------------------------------------------------

passed = filter(lambda x: x >= 40, marks)

passed_marks = list(passed)

print("Passing Marks:", passed_marks)


# ------------------------------------------------------------
# 2. Add 5 bonus marks
# ------------------------------------------------------------

bonus_marks = map(lambda x: x + 5, passed_marks)

bonus_marks = list(bonus_marks)

print("After Bonus:", bonus_marks)


# ------------------------------------------------------------
# 3. Calculate total
# ------------------------------------------------------------

total = reduce(lambda a, b: a + b, bonus_marks)

print("Total:", total)


# ------------------------------------------------------------
# 4. Find highest mark
# ------------------------------------------------------------

highest = reduce(
    lambda a, b: a if a > b else b,
    bonus_marks
)

print("Highest:", highest)


# ------------------------------------------------------------
# 5. Find lowest mark
# ------------------------------------------------------------

lowest = reduce(
    lambda a, b: a if a < b else b,
    bonus_marks
)

print("Lowest:", lowest)


# ------------------------------------------------------------
# 6. Calculate average
# ------------------------------------------------------------

average = total / len(bonus_marks)

print("Average:", average)


# ============================================================
# ⭐ IMPORTANT INTERVIEW QUESTIONS
# ============================================================

# Q1. What is lambda?
#
# Answer:
# Lambda is a small anonymous function that can be written
# in one line.


# Q2. What does map() do?
#
# Answer:
# map() applies a function to every item of an iterable.


# Q3. What does filter() do?
#
# Answer:
# filter() selects items based on a condition.


# Q4. What does reduce() do?
#
# Answer:
# reduce() combines multiple values into one final value.


# Q5. Where is reduce() available?
#
# Answer:
# reduce() is available in the functools module.


