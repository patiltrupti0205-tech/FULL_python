# ============================================================
# 🐍 DAY 24 – API + JSON REAL PROJECT
# ============================================================

import requests
import json


# ------------------------------------------------------------
# 1. FUNCTION TO GET USERS
# ------------------------------------------------------------

def get_users():

    url = "https://jsonplaceholder.typicode.com/users"

    try:

        response = requests.get(url, timeout=5)

        response.raise_for_status()

        return response.json()

    except requests.exceptions.RequestException as e:

        print("Error:", e)

        return []


# ------------------------------------------------------------
# 2. DISPLAY USERS
# ------------------------------------------------------------

def display_users(users):

    print("\n----- USERS -----")

    for user in users:

        print(
            user["id"],
            "|",
            user["name"],
            "|",
            user["email"]
        )


# ------------------------------------------------------------
# 3. SEARCH USER
# ------------------------------------------------------------

def search_user(users, name):

    for user in users:

        if user["name"].lower() == name.lower():

            return user

    return None


# ------------------------------------------------------------
# 4. SAVE DATA INTO JSON
# ------------------------------------------------------------

def save_json(data):

    with open("users.json", "w") as file:

        json.dump(data, file, indent=4)

    print("Data saved to users.json")


# ------------------------------------------------------------
# 5. MAIN PROGRAM
# ------------------------------------------------------------

users = get_users()

if users:

    display_users(users)

    name = input("\nEnter user name: ")

    user = search_user(users, name)

    if user:

        print("\n----- USER DETAILS -----")

        print("Name:", user["name"])
        print("Username:", user["username"])
        print("Email:", user["email"])
        print("Phone:", user["phone"])
        print("City:", user["address"]["city"])
        print("Company:", user["company"]["name"])

    else:

        print("User not found!")

    save_json(users)


# ============================================================
# 📝 PRACTICE QUESTIONS + ANSWERS
# ============================================================

# Q1. Create a function that returns API data.

def get_data():

    response = requests.get(
        "https://jsonplaceholder.typicode.com/posts/1"
    )

    return response.json()


print(get_data())


# Q2. Print only title.

data = get_data()

print(data["title"])


# Q3. Create a function to find a post by ID.

def find_post(posts, post_id):

    for post in posts:

        if post["id"] == post_id:
            return post

    return None


# Get posts
response = requests.get(
    "https://jsonplaceholder.typicode.com/posts"
)

posts = response.json()

result = find_post(posts, 5)

print(result)


# Q4. Save API data into JSON.

with open("posts.json", "w") as file:

    json.dump(posts, file, indent=4)

print("Posts saved!")


# Q5. Count total posts.

print("Total posts:", len(posts))


# Q6. Find posts of user ID 2.

user_posts = []

for post in posts:

    if post["userId"] == 2:

        user_posts.append(post)

print("User 2 posts:", len(user_posts))


# ============================================================
# 🚀 MINI PROJECT – API PRODUCT VIEWER
# ============================================================

# Fake Store API is used for practice.

url = "https://fakestoreapi.com/products"

try:

    response = requests.get(url, timeout=5)

    response.raise_for_status()

    products = response.json()

    print("\n===== PRODUCTS =====")

    for product in products:

        print("\nID:", product["id"])
        print("Title:", product["title"])
        print("Price:", product["price"])
        print("Category:", product["category"])


    # Save products
    with open("products.json", "w") as file:

        json.dump(products, file, indent=4)

    print("\nProducts saved successfully!")


except requests.exceptions.RequestException as e:

    print("Something went wrong:", e)


# ============================================================
# ⭐ DAY 24 INTERVIEW QUESTIONS
# ============================================================

# 1. What is HTTP?
# HTTP is a protocol used for communication between client and server.

# 2. What is REST API?
# REST API is an API architecture commonly used for web services.

# 3. What is JSON?
# JSON is a common format for exchanging data.

# 4. How do you get JSON from API?
# response.json()

# 5. How do you send JSON?
# requests.post(url, json=data)

# 6. Why use timeout?
# To prevent the program from waiting forever.

# 7. Why use try-except?
# To handle API/network errors.


# ============================================================
# 🧠 EASY REVISION
# ============================================================

# Day 22:
# JSON

# Day 23:
# API + requests

# Day 24:
# API + JSON + Functions + Exception Handling
#
# This combination is used in real Python projects.