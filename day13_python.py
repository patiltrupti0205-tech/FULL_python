# ==========================================
# DAY 13 – PYTHON EXCEPTION HANDLING
# ==========================================


# ------------------------------------------
# 1. WHAT IS EXCEPTION HANDLING?
# ------------------------------------------

# Exception means an error that occurs
# while the program is running.

# Example:

# number = int(input("Enter number: "))
# print(number)


# If user enters "abc", program will give an error.


# ------------------------------------------
# 2. try AND except
# ------------------------------------------

try:

    number = int(input("Enter a number: "))
    print("Number:", number)

except:

    print("Invalid input!")


# ------------------------------------------
# 3. VALUEERROR
# ------------------------------------------

try:

    number = int(input("Enter a number: "))

    print(number)

except ValueError:

    print("Please enter a valid number!")


# ------------------------------------------
# 4. ZERO DIVISION ERROR
# ------------------------------------------

try:

    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    result = a / b

    print("Result:", result)

except ZeroDivisionError:

    print("Cannot divide by zero!")


# ------------------------------------------
# 5. MULTIPLE EXCEPTIONS
# ------------------------------------------

try:

    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    result = a / b

    print("Result:", result)

except ValueError:

    print("Please enter numbers only!")

except ZeroDivisionError:

    print("Cannot divide by zero!")


# ------------------------------------------
# 6. EXCEPTION AS e
# ------------------------------------------

try:

    number = int("hello")

except ValueError as e:

    print("Error:", e)


# ------------------------------------------
# 7. ELSE
# ------------------------------------------

# else runs when there is NO error.

try:

    number = int(input("Enter a number: "))

except ValueError:

    print("Invalid number!")

else:

    print("You entered:", number)


# ------------------------------------------
# 8. FINALLY
# ------------------------------------------

# finally always runs.

try:

    number = int(input("Enter a number: "))

    print(number)

except ValueError:

    print("Invalid input!")

finally:

    print("Program completed.")


# ------------------------------------------
# 9. TRY + EXCEPT + ELSE + FINALLY
# ------------------------------------------

try:

    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    result = a / b

except ValueError:

    print("Please enter numbers only!")

except ZeroDivisionError:

    print("Cannot divide by zero!")

else:

    print("Result:", result)

finally:

    print("Thank you!")


# ------------------------------------------
# 10. FILE NOT FOUND ERROR
# ------------------------------------------

try:

    file = open("abc.txt", "r")

    data = file.read()

    print(data)

    file.close()

except FileNotFoundError:

    print("File not found!")


# ------------------------------------------
# 11. INDEX ERROR
# ------------------------------------------

numbers = [10, 20, 30]

try:

    print(numbers[5])

except IndexError:

    print("Index does not exist!")


# ------------------------------------------
# 12. KEY ERROR
# ------------------------------------------

student = {
    "name": "Trupti",
    "age": 20
}

try:

    print(student["marks"])

except KeyError:

    print("Key does not exist!")


# ------------------------------------------
# 13. TYPE ERROR
# ------------------------------------------

try:

    result = 10 + "20"

    print(result)

except TypeError:

    print("Cannot add different data types!")


# ------------------------------------------
# 14. RAISE
# ------------------------------------------

# raise is used to create an error
# manually.

age = 15

try:

    if age < 18:

        raise ValueError("Age must be 18 or above")

    print("Eligible")

except ValueError as e:

    print("Error:", e)


# ------------------------------------------
# 15. CUSTOM VALIDATION
# ------------------------------------------

marks = int(input("Enter marks: "))

try:

    if marks < 0 or marks > 100:

        raise ValueError("Marks must be between 0 and 100")

    print("Valid marks:", marks)

except ValueError as e:

    print("Error:", e)


# ==========================================
# PRACTICE QUESTIONS + ANSWERS
# ==========================================


# ------------------------------------------
# Q1. Take a number from user.
# Handle ValueError.
# ------------------------------------------

try:

    number = int(input("Enter a number: "))

    print("Number:", number)

except ValueError:

    print("Please enter a valid number!")


# ------------------------------------------
# Q2. Take two numbers and divide them.
# Handle ZeroDivisionError.
# ------------------------------------------

try:

    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    result = a / b

    print("Result:", result)

except ZeroDivisionError:

    print("Cannot divide by zero!")


# ------------------------------------------
# Q3. Handle both ValueError
# and ZeroDivisionError.
# ------------------------------------------

try:

    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    result = a / b

    print("Result:", result)

except ValueError:

    print("Enter numbers only!")

except ZeroDivisionError:

    print("Cannot divide by zero!")


# ------------------------------------------
# Q4. Use else with try-except.
# ------------------------------------------

try:

    number = int(input("Enter a number: "))

except ValueError:

    print("Invalid input!")

else:

    print("Number is:", number)


# ------------------------------------------
# Q5. Use finally.
# ------------------------------------------

try:

    number = int(input("Enter a number: "))

    print(number)

except ValueError:

    print("Invalid input!")

finally:

    print("This will always execute.")


# ------------------------------------------
# Q6. Open a file and handle
# FileNotFoundError.
# ------------------------------------------

try:

    with open("data.txt", "r") as file:

        data = file.read()

    print(data)

except FileNotFoundError:

    print("File does not exist!")


# ------------------------------------------
# Q7. Handle IndexError.
# ------------------------------------------

numbers = [10, 20, 30]

try:

    print(numbers[10])

except IndexError:

    print("Invalid index!")


# ------------------------------------------
# Q8. Handle KeyError.
# ------------------------------------------

student = {
    "name": "Trupti",
    "course": "B.Sc IT"
}

try:

    print(student["marks"])

except KeyError:

    print("Marks key is not available!")


# ------------------------------------------
# Q9. Use raise to check age.
# ------------------------------------------

age = int(input("Enter your age: "))

try:

    if age < 18:

        raise ValueError("You must be 18 or above")

    print("You are eligible.")

except ValueError as e:

    print("Error:", e)


# ------------------------------------------
# Q10. Validate marks.
# Marks should be between 0 and 100.
# ------------------------------------------

marks = int(input("Enter marks: "))

try:

    if marks < 0 or marks > 100:

        raise ValueError("Marks must be between 0 and 100")

    print("Valid marks:", marks)

except ValueError as e:

    print("Error:", e)


# ==========================================
# MINI PROJECT
# STUDENT MARKS CALCULATOR
# ==========================================

print("\n===== STUDENT MARKS CALCULATOR =====")

try:

    name = input("Enter student name: ")

    marks1 = float(input("Enter subject 1 marks: "))
    marks2 = float(input("Enter subject 2 marks: "))
    marks3 = float(input("Enter subject 3 marks: "))

    marks = [marks1, marks2, marks3]

    # Check marks
    for mark in marks:

        if mark < 0 or mark > 100:

            raise ValueError("Marks must be between 0 and 100")

    total = sum(marks)

    average = total / len(marks)

    print("\n----- STUDENT RESULT -----")

    print("Name:", name)
    print("Total:", total)
    print("Average:", average)

    if average >= 90:
        print("Grade: A+")

    elif average >= 80:
        print("Grade: A")

    elif average >= 70:
        print("Grade: B")

    elif average >= 60:
        print("Grade: C")

    elif average >= 50:
        print("Grade: D")

    else:
        print("Grade: F")


except ValueError as e:

    print("Error:", e)

finally:

    print("\nResult checking completed.")


