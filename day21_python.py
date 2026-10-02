# ============================================================
# 🐍 DAY 21 – REGULAR EXPRESSIONS (REGEX)
# ============================================================

# Regex = Regular Expression
#
# Regex ka use:
# ✔ Text search
# ✔ Pattern matching
# ✔ Email validation
# ✔ Phone number validation
# ✔ Find numbers
# ✔ Find words
# ✔ Replace text
# ✔ Data cleaning


# ============================================================
# 1️⃣ IMPORT re
# ============================================================

import re


# ============================================================
# 2️⃣ re.search()
# ============================================================

# search() text ke andar pattern ko search karta hai.

text = "I am learning Python"

result = re.search("Python", text)

if result:
    print("Python found")
else:
    print("Python not found")


# ============================================================
# 3️⃣ re.match()
# ============================================================

# match() sirf STRING ke START mein pattern check karta hai.

text = "Python is easy"

result = re.match("Python", text)

if result:
    print("Match found")
else:
    print("No match")


# Example

text = "I love Python"

result = re.match("Python", text)

print(result)

# None because Python string ke beginning mein nahi hai.


# ============================================================
# 4️⃣ re.findall()
# ============================================================

# findall() pattern ke saare matches ki list deta hai.

text = "Python is easy. Python is powerful."

result = re.findall("Python", text)

print(result)

# Output:
# ['Python', 'Python']


# ============================================================
# 5️⃣ FIND ALL NUMBERS
# ============================================================

text = "I have 2 laptops and 3 phones."

numbers = re.findall(r"\d+", text)

print(numbers)


# ============================================================
# 6️⃣ \d – DIGIT
# ============================================================

# \d = any digit (0-9)

text = "My marks are 85 and 90"

result = re.findall(r"\d", text)

print(result)

# Every individual digit


# \d+ = complete number

result = re.findall(r"\d+", text)

print(result)


# ============================================================
# 7️⃣ \w – WORD CHARACTER
# ============================================================

# \w = letters, digits and underscore

text = "Python_123"

result = re.findall(r"\w+", text)

print(result)


# ============================================================
# 8️⃣ \s – SPACE
# ============================================================

# \s = whitespace

text = "Hello World Python"

result = re.findall(r"\s", text)

print(result)


# ============================================================
# 9️⃣ DOT .
# ============================================================

# . = any character except newline

text = "cat cot cut"

result = re.findall(r"c.t", text)

print(result)

# Matches:
# cat
# cot
# cut


# ============================================================
# 🔟 ^ START OF STRING
# ============================================================

text = "Python is easy"

result = re.findall(r"^Python", text)

print(result)


# ============================================================
# 1️⃣1️⃣ $ END OF STRING
# ============================================================

text = "I love Python"

result = re.findall(r"Python$", text)

print(result)


# ============================================================
# 1️⃣2️⃣ * ZERO OR MORE
# ============================================================

text = "coool"

result = re.findall(r"co*l", text)

print(result)


# ============================================================
# 1️⃣3️⃣ + ONE OR MORE
# ============================================================

text = "coool"

result = re.findall(r"co+l", text)

print(result)


# ============================================================
# 1️⃣4️⃣ ? ZERO OR ONE
# ============================================================

text = "color colour"

result = re.findall(r"colou?r", text)

print(result)


# ============================================================
# 1️⃣5️⃣ {n} EXACT NUMBER
# ============================================================

text = "12345 123 12"

result = re.findall(r"\d{3}", text)

print(result)


# ============================================================
# 1️⃣6️⃣ {n,m} RANGE
# ============================================================

text = "12 123 1234 12345"

result = re.findall(r"\d{3,4}", text)

print(result)


# ============================================================
# 1️⃣7️⃣ [] CHARACTER SET
# ============================================================

text = "cat bat rat"

result = re.findall(r"[cb]at", text)

print(result)

# cat
# bat


# ============================================================
# 1️⃣8️⃣ [a-z]
# ============================================================

text = "apple Banana mango"

result = re.findall(r"[a-z]+", text)

print(result)


# ============================================================
# 1️⃣9️⃣ [A-Z]
# ============================================================

text = "Hello PYTHON World"

result = re.findall(r"[A-Z]+", text)

print(result)


# ============================================================
# 2️⃣0️⃣ [0-9]
# ============================================================

text = "My numbers are 123 and 456"

result = re.findall(r"[0-9]+", text)

print(result)


# ============================================================
# 2️⃣1️⃣ NEGATIVE CHARACTER SET [^]
# ============================================================

# [^0-9] = anything except digits

text = "Python123"

result = re.findall(r"[^0-9]+", text)

print(result)


# ============================================================
# 2️⃣2️⃣ re.sub()
# ============================================================

# sub() text ko replace karta hai.

text = "I love Java"

result = re.sub("Java", "Python", text)

print(result)


# ============================================================
# 2️⃣3️⃣ REMOVE SPACES
# ============================================================

text = "Hello World Python"

result = re.sub(r"\s", "", text)

print(result)


# ============================================================
# 2️⃣4️⃣ EXTRACT EMAIL
# ============================================================

text = """
Contact:
patiltrupti@gmail.com
hello@gmail.com
test@yahoo.com
"""

emails = re.findall(
    r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}",
    text
)

print(emails)


# ============================================================
# 2️⃣5️⃣ EMAIL VALIDATION
# ============================================================

email = "patiltrupti@gmail.com"

pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

if re.fullmatch(pattern, email):
    print("Valid Email")
else:
    print("Invalid Email")


# ============================================================
# 2️⃣6️⃣ PHONE NUMBER VALIDATION
# ============================================================

phone = "9316862084"

pattern = r"^[0-9]{10}$"

if re.fullmatch(pattern, phone):
    print("Valid Phone Number")
else:
    print("Invalid Phone Number")


# ============================================================
# 2️⃣7️⃣ INDIAN PHONE NUMBER
# ============================================================

phone = "9316862084"

pattern = r"^[6-9][0-9]{9}$"

if re.fullmatch(pattern, phone):
    print("Valid Indian Mobile Number")
else:
    print("Invalid Mobile Number")


# ============================================================
# 2️⃣8️⃣ FIND HASHTAGS
# ============================================================

text = "I love #Python #Cloud #Coding"

hashtags = re.findall(r"#\w+", text)

print(hashtags)


# ============================================================
# 2️⃣9️⃣ FIND USERNAMES
# ============================================================

text = "@trupti @python @cloud"

usernames = re.findall(r"@\w+", text)

print(usernames)


# ============================================================
# 3️⃣0️⃣ re.split()
# ============================================================

text = "Python,Java,C++,Cloud"

result = re.split(",", text)

print(result)


# ============================================================
# 📝 PRACTICE QUESTIONS + ANSWERS
# ============================================================


# Q1. Find all numbers from a string.

text = "I have 10 apples and 20 bananas."

result = re.findall(r"\d+", text)

print(result)


# ------------------------------------------------------------
# Q2. Find all words starting with "P".
# ------------------------------------------------------------

text = "Python Programming is Powerful"

result = re.findall(r"\bP\w*", text)

print(result)


# ------------------------------------------------------------
# Q3. Find all email addresses.
# ------------------------------------------------------------

text = """
trupti@gmail.com
hello@yahoo.com
test@outlook.com
"""

result = re.findall(
    r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}",
    text
)

print(result)


# ------------------------------------------------------------
# Q4. Validate a 10-digit phone number.
# ------------------------------------------------------------

phone = "9316862084"

if re.fullmatch(r"[0-9]{10}", phone):
    print("Valid")
else:
    print("Invalid")


# ------------------------------------------------------------
# Q5. Find hashtags.
# ------------------------------------------------------------

text = "Learning #Python and #Cloud #AWS"

result = re.findall(r"#\w+", text)

print(result)


# ------------------------------------------------------------
# Q6. Replace Python with Java.
# ------------------------------------------------------------

text = "Python is easy. I love Python."

result = re.sub("Python", "Java", text)

print(result)


# ------------------------------------------------------------
# Q7. Remove all numbers.
# ------------------------------------------------------------

text = "Python123 is easy456"

result = re.sub(r"\d+", "", text)

print(result)


# ------------------------------------------------------------
# Q8. Find words containing "cloud".
# ------------------------------------------------------------

text = "cloud computing and cloud security"

result = re.findall(r"\bcloud\w*", text)

print(result)


# ------------------------------------------------------------
# Q9. Check if string starts with Python.
# ------------------------------------------------------------

text = "Python is powerful"

if re.search(r"^Python", text):
    print("Starts with Python")
else:
    print("Does not start with Python")


# ------------------------------------------------------------
# Q10. Check if string ends with Python.
# ------------------------------------------------------------

text = "I am learning Python"

if re.search(r"Python$", text):
    print("Ends with Python")
else:
    print("Does not end with Python")


# ============================================================
# 🚀 MINI PROJECT – CONTACT INFORMATION EXTRACTOR
# ============================================================

text = """
Hello!

My name is Trupti.

Email: patiltrupti@gmail.com
Email: trupti123@yahoo.com

Phone: 9316862084
Phone: 9876543210

I am learning #Python #CloudComputing #AWS
"""


# ------------------------------------------------------------
# Extract Emails
# ------------------------------------------------------------

emails = re.findall(
    r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}",
    text
)


# ------------------------------------------------------------
# Extract Phone Numbers
# ------------------------------------------------------------

phones = re.findall(
    r"\b[6-9][0-9]{9}\b",
    text
)


# ------------------------------------------------------------
# Extract Hashtags
# ------------------------------------------------------------

hashtags = re.findall(
    r"#\w+",
    text
)


# ------------------------------------------------------------
# Display Result
# ------------------------------------------------------------

print("\n========== CONTACT INFORMATION ==========")

print("Emails:")
for email in emails:
    print(email)

print("\nPhone Numbers:")
for phone in phones:
    print(phone)

print("\nHashtags:")
for hashtag in hashtags:
    print(hashtag)


# ============================================================
# 🚀 MINI PROJECT 2 – PASSWORD VALIDATOR
# ============================================================

password = input("\nEnter password: ")

# Conditions:
# At least 8 characters
# At least one uppercase
# At least one lowercase
# At least one digit

if len(password) < 8:
    print("Password must contain at least 8 characters.")

elif not re.search(r"[A-Z]", password):
    print("Password must contain an uppercase letter.")

elif not re.search(r"[a-z]", password):
    print("Password must contain a lowercase letter.")

elif not re.search(r"\d", password):
    print("Password must contain a number.")

else:
    print("Password format is valid.")


# ============================================================
# ⭐ IMPORTANT REGEX SYMBOLS
# ============================================================

# \d      → Digit
# \w      → Word character
# \s      → Space
# .       → Any character
# ^       → Start
# $       → End
# *       → 0 or more
# +       → 1 or more
# ?       → 0 or 1
# {n}     → Exactly n
# {n,m}   → Between n and m
# []      → Character set
# [^]     → NOT
#
# ------------------------------------------------------------
#
# re.search()    → Search pattern
# re.match()     → Match from beginning
# re.findall()   → Find all matches
# re.sub()       → Replace
# re.split()     → Split
# re.fullmatch() → Match complete string


# ============================================================
# ⭐ IMPORTANT INTERVIEW QUESTIONS
# ============================================================

# Q1. What is Regex?
#
# Answer:
# Regex is a pattern used to search, match, extract,
# validate and replace text.


# Q2. Which module is used for Regex in Python?
#
# Answer:
# re module.


# Q3. Difference between search() and match()?
#
# search() → Searches anywhere in the string.
# match()  → Checks from the beginning.


# Q4. What does findall() return?
#
# Answer:
# It returns a list containing all matches.


# Q5. What does \d mean?
#
# Answer:
# Any digit from 0 to 9.


# Q6. What does + mean?
#
# Answer:
# One or more occurrences.


# Q7. What does ^ mean?
#
# Answer:
# Beginning of the string.


# Q8. What does $ mean?
#
# Answer:
# End of the string.

