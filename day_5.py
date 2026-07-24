# string

name = "trupti"
print(name)

# Creating string 
name = "python"
city = 'surat'

print(name)
print(city)

# string indexing

text = "python"

print(text[0])
print(text[1])
print(text[5])

# Negative indexing

text = "python"

print(text[-1])
print(text[-2])
print(text[-6])

# string slicing
# string[start:end:step]
text = "python is easy to use"
print(text[0:6])
print(text[7:18])
print(text[:6])
print(text[7:])
print(text[::2])

# reverse string
text = "python"

print((text[::-1]))

# string length 

text = "python"
print(len(text))

#sring concatenation

first = "hello"
secound = "word"

print(first +" "+ secound)

# string repetition

print("Hi " * 3)

# Membership operators

text = "python"

print("p" in text)
print("x" in text)
print("x" not in text)

# Important string methods
# upper()

name= "python"
print(name.upper())

# lower()
name = "koyal"
print(name.lower())

# title()
name = "python programming learning"
print(name.title())

# capitalize()
name= "pro programing"
print(name.capitalize())

# strip()
name = "   python by tp "
print(name.strip())

# replace()
name = "easy lanuaguge is python ."
print(text.replace("python","php"))

# split()
text = " banana mango cheery"
print(text.split())

# join()
fruits = ["apple" , "banana" , "mango"]
print(",".join(fruits))

# find()
text = "python"
print(text.find("t"))

# startswith()
text = "python"
print(text.startswith("py"))

# endswith()
text="python"
print(text.endswith("on"))

# isalpha()
print("python".isalpha())
print("python1234".isalpha())

# isdigit()
print("1234".isdigit())
print("1233d".isdigit())

#isalnum()
print("python123".isalnum())

##escape characters

print("Hello\nWorld")
print("Hello\tWorld")
print("He said \"Python\"")

# string formating

name = "Trupti"
age = 20

print("My name is {} and age is {}".format(name, age))

# f-string 

name = "Trupti"
age = 20

print(f"My name is {name} and I am {age} years old.")

#loop through string

text ="python"

for ch in text:
    print(ch)

# reverse using loop

text = "Python"
reverse = ""

for ch in text:
    reverse = ch + reverse

print(reverse)

#count vowels

text = input("Enter a string: ")
count = 0

for ch in text.lower():
    if ch in "aeiou":
        count += 1

print("Vowels:", count)

# check palindrome

text = input("Enter a string: ")

if text == text[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")

# removes spaces

text = input("Enter a string: ")

print(text.replace(" ", ""))

# count characters 

text = input("Enter a string: ")

print(len(text))

# Mini project about password strength checker

password = input("Enter Password: ")

if len(password) >= 8:
    if any(ch.isupper() for ch in password) and any(ch.islower() for ch in password) and any(ch.isdigit() for ch in password):
        print("Strong Password")
    else:
        print("Weak Password")
else:
    print("Password too short")



# some practice quetions


# 1. Print each character of a string.

text = input("Enter a string: ")

for i in text:
    print(i)


# 2. Reverse a string.

text = input("Enter a string: ")

reverse = text[::-1]

print("Reverse String:", reverse)


# 3. Check whether a string is palindrome.

text = input("Enter a string: ")

if text == text[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")


# 4. Count vowels.

text = input("Enter a string: ")

vowels = 0

for i in text.lower():
    if i in "aeiou":
        vowels += 1

print("Total Vowels:", vowels)



# 5. Count consonants.

text = input("Enter a string: ")

consonants = 0

for i in text.lower():
    if i.isalpha() and i not in "aeiou":
        consonants += 1

print("Total Consonants:", consonants)



# 6. Count uppercase and lowercase letters.

text = input("Enter a string: ")

upper = 0
lower = 0

for i in text:
    if i.isupper():
        upper += 1
    elif i.islower():
        lower += 1

print("Uppercase Letters:", upper)
print("Lowercase Letters:", lower)


# 7. Replace spaces with underscore.

text = input("Enter a string: ")

new_text = text.replace(" ", "_")

print(new_text)


# 8. Remove duplicate characters.

text = input("Enter a string: ")

result = ""

for i in text:
    if i not in result:
        result = result + i

print("After Removing Duplicates:", result)


# 9. Find frequency of each character.

text = input("Enter a string: ")

checked = ""

for i in text:
    if i not in checked:
        print(i, "=", text.count(i))
        checked += i


# 10. Count words in a sentence.

sentence = input("Enter a sentence: ")

words = sentence.split()

print("Total Words:", len(words))


# 11. Check whether two strings are anagrams.

first = input("Enter first string: ")
second = input("Enter second string: ")

if sorted(first.lower()) == sorted(second.lower()):
    print("Strings are Anagrams")
else:
    print("Strings are Not Anagrams")


# 12. Find the longest word in a sentence.

sentence = input("Enter a sentence: ")

words = sentence.split()

longest = ""

for word in words:
    if len(word) > len(longest):
        longest = word

print("Longest Word:", longest)


# 13. Reverse every word in a sentence.

sentence = input("Enter a sentence: ")

words = sentence.split()

for word in words:
    print(word[::-1], end=" ")


# 14. Count digits, alphabets and special characters.

text = input("Enter a string: ")

digits = 0
alphabets = 0
special = 0

for i in text:
    if i.isdigit():
        digits += 1
    elif i.isalpha():
        alphabets += 1
    else:
        special += 1

print("Digits:", digits)
print("Alphabets:", alphabets)
print("Special Characters:", special)


# 15. Find the first non-repeating character.

text = input("Enter a string: ")

found = False

for i in text:
    if text.count(i) == 1:
        print("First Non-Repeating Character:", i)
        found = True
        break

if found == False:
    print("No Non-Repeating Character Found")