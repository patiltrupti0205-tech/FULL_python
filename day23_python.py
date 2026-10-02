# ============================================================
# 🐍 DAY 23 – APIs & REQUESTS
# ============================================================

# First install requests if needed:
# pip install requests

import requests


# ------------------------------------------------------------
# 1. API KYA HAI?
# ------------------------------------------------------------

# API = Application Programming Interface
#
# Simple meaning:
# Python kisi server se data maangta hai
# aur server Python ko data return karta hai.
#
# Example:
# Python → API → Server
# Python ← API ← Data


# ------------------------------------------------------------
# 2. GET REQUEST
# ------------------------------------------------------------

url = "https://jsonplaceholder.typicode.com/posts/1"

response = requests.get(url)

print(response)
print(response.status_code)


# ------------------------------------------------------------
# 3. STATUS CODE
# ------------------------------------------------------------

# 200 = Success
# 201 = Created
# 400 = Bad Request
# 401 = Unauthorized
# 403 = Forbidden
# 404 = Not Found
# 500 = Server Error

if response.status_code == 200:
    print("Request successful!")
else:
    print("Request failed!")


# ------------------------------------------------------------
# 4. API DATA AS JSON
# ------------------------------------------------------------

data = response.json()

print(data)
print(type(data))


# ------------------------------------------------------------
# 5. ACCESS API DATA
# ------------------------------------------------------------

print("Post ID:", data["id"])
print("Title:", data["title"])
print("Body:", data["body"])


# ------------------------------------------------------------
# 6. GET MULTIPLE DATA
# ------------------------------------------------------------

url = "https://jsonplaceholder.typicode.com/posts"

response = requests.get(url)

if response.status_code == 200:

    posts = response.json()

    print("Total posts:", len(posts))

    for post in posts[:5]:
        print("\nID:", post["id"])
        print("Title:", post["title"])


# ------------------------------------------------------------
# 7. API WITH PARAMETERS
# ------------------------------------------------------------

url = "https://jsonplaceholder.typicode.com/posts"

params = {
    "userId": 1
}

response = requests.get(url, params=params)

print(response.url)

data = response.json()

for post in data:
    print(post["title"])


# ------------------------------------------------------------
# 8. POST REQUEST
# ------------------------------------------------------------

url = "https://jsonplaceholder.typicode.com/posts"

new_post = {
    "title": "My Python Project",
    "body": "Learning APIs in Python",
    "userId": 1
}

response = requests.post(url, json=new_post)

print(response.status_code)
print(response.json())


# ------------------------------------------------------------
# 9. PUT REQUEST
# ------------------------------------------------------------

url = "https://jsonplaceholder.typicode.com/posts/1"

updated_data = {
    "id": 1,
    "title": "Updated Title",
    "body": "Updated body",
    "userId": 1
}

response = requests.put(url, json=updated_data)

print(response.status_code)
print(response.json())


# ------------------------------------------------------------
# 10. DELETE REQUEST
# ------------------------------------------------------------

url = "https://jsonplaceholder.typicode.com/posts/1"

response = requests.delete(url)

print("Status:", response.status_code)


# ------------------------------------------------------------
# 11. ERROR HANDLING
# ------------------------------------------------------------

try:

    url = "https://jsonplaceholder.typicode.com/posts/1"

    response = requests.get(url, timeout=5)

    response.raise_for_status()

    data = response.json()

    print(data)

except requests.exceptions.Timeout:
    print("Request timed out!")

except requests.exceptions.RequestException as e:
    print("API Error:", e)


# ============================================================
# 📝 PRACTICE QUESTIONS + ANSWERS
# ============================================================

# Q1. Send GET request.

url = "https://jsonplaceholder.typicode.com/users/1"

response = requests.get(url)

print(response.json())


# Q2. Print user name.

data = response.json()

print(data["name"])


# Q3. Print user email.

print(data["email"])


# Q4. Check status code.

print(response.status_code)


# Q5. Get all users.

url = "https://jsonplaceholder.typicode.com/users"

response = requests.get(url)

users = response.json()

for user in users:
    print(user["name"])


# Q6. Count users.

print("Total users:", len(users))


# Q7. Find users from a particular city.

for user in users:

    if user["address"]["city"] == "Gwenborough":
        print(user["name"])


# Q8. Create a POST request.

new_user = {
    "name": "Trupti",
    "email": "trupti@example.com"
}

response = requests.post(
    "https://jsonplaceholder.typicode.com/users",
    json=new_user
)

print(response.json())


# Q9. Handle an error.

try:

    response = requests.get(
        "https://jsonplaceholder.typicode.com/invalid",
        timeout=5
    )

    response.raise_for_status()

except requests.exceptions.RequestException as e:
    print("Error:", e)


# ============================================================
# 🚀 MINI PROJECT – API USER FINDER
# ============================================================

import requests

url = "https://jsonplaceholder.typicode.com/users"

response = requests.get(url)

if response.status_code == 200:

    users = response.json()

    print("----- USER LIST -----")

    for user in users:
        print(
            user["id"],
            "-",
            user["name"],
            "-",
            user["email"]
        )

    search_name = input("\nEnter user name: ")

    found = False

    for user in users:

        if user["name"].lower() == search_name.lower():

            print("\nUser Found!")
            print("Name:", user["name"])
            print("Email:", user["email"])
            print("Phone:", user["phone"])
            print("City:", user["address"]["city"])

            found = True
            break

    if not found:
        print("User not found!")

else:
    print("API request failed!")


# ============================================================
# ⭐ INTERVIEW QUESTIONS
# ============================================================

# 1. What is an API?
# API allows applications to communicate with each other.

# 2. What is requests?
# Python library used for sending HTTP requests.

# 3. What is GET?
# Used to retrieve data.

# 4. What is POST?
# Used to send/create data.

# 5. What is PUT?
# Used to update data.

# 6. What is DELETE?
# Used to delete data.

# 7. What is status_code?
# It tells whether the request was successful or not.


# ============================================================
# 🧠 EASY REVISION
# ============================================================

# GET    → Data lena
# POST   → Data bhejna/create
# PUT    → Data update
# DELETE → Data delete
#
# response.json() → API response ko Python data me convert karta hai.