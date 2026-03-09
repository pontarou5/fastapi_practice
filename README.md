# FastAPI User Management API

A simple REST API built with **FastAPI** that stores GitHub user information in a **SQLite database**.

This project was built as a backend practice project to learn:

* **FastAPI**
* **REST API design**
* **SQLite database integration**
* **Git / GitHub workflow**
* **API deployment preparation**

---

# Features

* Fetch user data from the **GitHub API**
* Store user data in a **SQLite database**
* Create new users
* Retrieve all users with **pagination**
* Retrieve a **specific user**
* Update user information
* Delete users

---

# Tech Stack

* **Python**
* **FastAPI**
* **SQLite**
* **Pydantic**
* **Uvicorn**
* **Requests**

---

# Project Structure

```
fastapi_practice/
│
├── main.py          # FastAPI application and API endpoints
├── database.py      # SQLite database initialization and connection
├── users.db         # SQLite database (created automatically)
├── requirements.txt
└── README.md
```

---

# Installation

Clone the repository:

```
git clone https://github.com/YOUR_USERNAME/fastapi_practice.git
cd fastapi_practice
```

Create a virtual environment:

```
python -m venv venv
source venv/bin/activate
```

Install dependencies:

```
pip install -r requirements.txt
```

---

# Running the API

Start the server using **Uvicorn**:

```
uvicorn main:app --reload
```

The API will be available at:

```
http://127.0.0.1:8000
```

Interactive API documentation:

```
http://127.0.0.1:8000/docs
```

---

# API Endpoints

## Root

```
GET /
```

Response:

```
{
  "message": "API running"
}
```

---

## Fetch GitHub User

Fetches a sample GitHub user (**octocat**) and stores it in the database.

```
GET /fetch_user
```

Response example:

```
{
  "name": "octocat",
  "followers": 10000
}
```

---

## Get All Users

Retrieve users with pagination.

```
GET /users
```

Query parameters:

| Parameter | Description               | Default |
| --------- | ------------------------- | ------- |
| limit     | Number of users to return | 10      |
| offset    | Pagination offset         | 0       |

Example:

```
GET /users?limit=5&offset=0
```

---

## Get User by ID

```
GET /users/{user_id}
```

Example:

```
GET /users/1
```

---

## Create User

```
POST /users
```

Request body:

```
{
  "name": "alice",
  "followers": 120
}
```

---

## Update User

```
PUT /users/{user_id}
```

Request body:

```
{
  "name": "alice_updated",
  "followers": 200
}
```

---

## Delete User

```
DELETE /users/{user_id}
```

Example:

```
DELETE /users/1
```

---

# 🗄 Database

The application uses **SQLite**.

The database file is automatically created when the application starts.

Schema:

```
users
│
├── id (INTEGER PRIMARY KEY AUTOINCREMENT)
├── name (TEXT)
└── followers (INTEGER)
```

---

# Example Workflow

1. Fetch a GitHub user

```
GET /fetch_user
```

2. Retrieve stored users

```
GET /users
```

3. Update user information

```
PUT /users/1
```

4. Delete a user

```
DELETE /users/1
```

---

# Future Improvements

Possible improvements for this project:

* Add **unit tests**
* Add **environment variable configuration**
* Improve **error handling**
* Add **authentication**
* Deploy the API

---

# License

This project is for **educational purposes**.
