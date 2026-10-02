# ==========================================
# DAY 14 – ADVANCED STRINGS
# ==========================================

# ------------------------------------------
# 1. STRING METHODS
# ------------------------------------------

text = "Hello Python"

print(text.upper())
print(text.lower())
print(text.title())
print(text.capitalize())


# ------------------------------------------
# 2. strip()
# Removes spaces from beginning and end
# ------------------------------------------

name = "   Trupti   "

print(name.strip())


# ------------------------------------------
# 3. lstrip()
# Removes spaces from left side
# ------------------------------------------

name = "   Trupti"

print(name.lstrip())


# ------------------------------------------
# 4. rstrip()
# Removes spaces from right side
# ------------------------------------------

name = "Trupti   "

print(name.rstrip())


# ------------------------------------------
# 5. replace()
# ------------------------------------------

text = "I like Java"

new_text = text.replace("Java", "Python")

print(new_text)


# ------------------------------------------
# 6. count()
# ------------------------------------------

text = "Python is easy. Python is powerful."

print(text.count("Python"))


# ------------------------------------------
# 7. find()
# ------------------------------------------

text = "Hello Python"

print(text.find("Python"))


# ------------------------------------------
# 8. index()
# ------------------------------------------

text = "Hello Python"

print(text.index("Python"))


# ------------------------------------------
# 9. startswith()
# ------------------------------------------

name = "Trupti"

print(name.startswith("Tru"))
print(name.startswith("Pat"))


# ------------------------------------------
# 10. endswith()
# ------------------------------------------

filename = "student.py"

print(filename.endswith(".py"))
print(filename.endswith(".txt"))


# ------------------------------------------
# 11. split()
# Converts string into list
# ------------------------------------------

text = "Python is easy to learn"

words = text.split()

print(words)


# ------------------------------------------
# Split using comma
# ------------------------------------------

data = "Apple,Mango,Banana,Orange"

fruits = data.split(",")

print(fruits)


# ------------------------------------------
# 12. join()
# Converts list into string
# ------------------------------------------

fruits = ["Apple", "Mango", "Banana"]

result = ", ".join(fruits)

print(result)


# ------------------------------------------
# 13. isalpha()
# Checks only alphabets
# ------------------------------------------

text = "Trupti"

print(text.isalpha())


# ------------------------------------------
# 14. isdigit()
# Checks only digits
# ------------------------------------------

number = "12345"

print(number.isdigit())


# ------------------------------------------
# 15. isalnum()
# Checks alphabets + numbers
# ------------------------------------------

text = "Trupti123"

print(text.isalnum())


# ------------------------------------------
# 16. isspace()
# Checks only spaces
# ------------------------------------------

text = "     "

print(text.isspace())


# ------------------------------------------
# 17. String formatting
# ------------------------------------------

name = "Trupti"
age = 20

print("My name is", name, "and I am", age, "years old.")


# ------------------------------------------
# 18. f-string
# ------------------------------------------

name = "Trupti"
age = 20

print(f"My name is {name} and I am {age} years old.")


# ------------------------------------------
# 19. f-string with calculation
# ------------------------------------------

price = 100
quantity = 3

total = price * quantity

print(f"Total price: {total}")


# ------------------------------------------
# 20. String slicing
# ------------------------------------------

text = "Python Programming"

print(text[0:6])
print(text[7:])
print(text[:6])
print(text[::-1])


# ------------------------------------------
# 21. Check palindrome
# ------------------------------------------

word = input("Enter a word: ")

if word.lower() == word.lower()[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")


# ------------------------------------------
# 22. Count vowels
# ------------------------------------------

text = input("Enter a string: ")

vowels = "aeiou"
count = 0

for char in text.lower():

    if char in vowels:
        count += 1

print("Total Vowels:", count)


# ------------------------------------------
# 23. Count consonants
# ------------------------------------------

text = input("Enter a string: ")

vowels = "aeiou"
count = 0

for char in text.lower():

    if char.isalpha() and char not in vowels:
        count += 1

print("Total Consonants:", count)


# ------------------------------------------
# 24. Reverse a string
# ------------------------------------------

text = input("Enter a string: ")

reverse = text[::-1]

print("Reverse:", reverse)


# ------------------------------------------
# 25. Remove spaces
# ------------------------------------------

text = "Python is very easy"

new_text = text.replace(" ", "")

print(new_text)


# ==========================================
# PRACTICE QUESTIONS + ANSWERS
# ==========================================


# ------------------------------------------
# Q1. Convert a string into uppercase.
# ------------------------------------------

text = "hello python"

print(text.upper())


# ------------------------------------------
# Q2. Convert a string into lowercase.
# ------------------------------------------

text = "HELLO PYTHON"

print(text.lower())


# ------------------------------------------
# Q3. Remove extra spaces from a name.
# ------------------------------------------

name = "   Trupti   "

print(name.strip())


# ------------------------------------------
# Q4. Replace Java with Python.
# ------------------------------------------

text = "I am learning Java"

text = text.replace("Java", "Python")

print(text)


# ------------------------------------------
# Q5. Count how many times Python
# appears in a sentence.
# ------------------------------------------

text = "Python is easy. Python is useful."

print(text.count("Python"))


# ------------------------------------------
# Q6. Find the position of "Python".
# ------------------------------------------

text = "I love Python"

print(text.find("Python"))


# ------------------------------------------
# Q7. Check whether a filename
# ends with .py
# ------------------------------------------

filename = "program.py"

if filename.endswith(".py"):
    print("Python file")
else:
    print("Not a Python file")


# ------------------------------------------
# Q8. Split a sentence into words.
# ------------------------------------------

sentence = "Python is easy to learn"

words = sentence.split()

print(words)


# ------------------------------------------
# Q9. Join a list of fruits.
# ------------------------------------------

fruits = ["Apple", "Mango", "Banana"]

result = ", ".join(fruits)

print(result)


# ------------------------------------------
# Q10. Check whether a string
# contains only alphabets.
# ------------------------------------------

text = "Trupti"

if text.isalpha():
    print("Only alphabets")
else:
    print("Contains other characters")


# ------------------------------------------
# Q11. Check whether a string
# contains only numbers.
# ------------------------------------------

number = "12345"

if number.isdigit():
    print("Only numbers")
else:
    print("Not only numbers")


# ------------------------------------------
# Q12. Count vowels in a string.
# ------------------------------------------

text = input("Enter a string: ")

vowels = "aeiou"
count = 0

for char in text.lower():

    if char in vowels:
        count += 1

print("Vowels:", count)


# ------------------------------------------
# Q13. Reverse a string.
# ------------------------------------------

text = input("Enter a string: ")

print("Reverse:", text[::-1])


# ------------------------------------------
# Q14. Check whether a word is palindrome.
# ------------------------------------------

word = input("Enter a word: ")

if word.lower() == word.lower()[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")


# ------------------------------------------
# Q15. Count words in a sentence.
# ------------------------------------------

sentence = input("Enter a sentence: ")

words = sentence.split()

print("Total Words:", len(words))


# ==========================================
# MINI PROJECT
# TEXT ANALYZER
# ==========================================

print("\n===== TEXT ANALYZER =====")

text = input("Enter a sentence: ")

# Remove extra spaces
text = text.strip()

# Number of characters
characters = len(text)

# Number of words
words = text.split()
word_count = len(words)

# Count vowels
vowels = "aeiou"
vowel_count = 0

for char in text.lower():

    if char in vowels:
        vowel_count += 1


# Count consonants
consonant_count = 0

for char in text.lower():

    if char.isalpha() and char not in vowels:
        consonant_count += 1


# Reverse
reverse_text = text[::-1]


# Display result
print("\n----- RESULT -----")

print(f"Original Text: {text}")
print(f"Characters: {characters}")
print(f"Words: {word_count}")
print(f"Vowels: {vowel_count}")
print(f"Consonants: {consonant_count}")
print(f"Reverse: {reverse_text}")


# Check palindrome
if text.lower().replace(" ", "") == text.lower().replace(" ", "")[::-1]:

    print("Palindrome: Yes")

else:

    print("Palindrome: No")

