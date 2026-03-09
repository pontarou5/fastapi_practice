from fastapi import FastAPI
import requests
import sqlite3
from pydantic import BaseModel
from database import init_db, get_connection

class UserCreate(BaseModel):
    name: str
    followers: int

app = FastAPI()

init_db()

DB_NAME = "users.db"

@app.get("/")
def root():
    return {"message": "API running"}

@app.get("/fetch_user")
def fetch_user():
    #GitHub API
    url = "https://api.github.com/users/octocat"
    res = requests.get(url)

    data = res.json()

    name = data["login"]
    followers = data["followers"]

    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO users (name, followers) VALUES (?, ?)",
        (name, followers)
    )

    conn.commit()
    conn.close()

    return {
        "name": name,
        "followers": followers
    }

@app.get("/users")
def get_users(limit: int = 10, offset: int = 0):

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM users LIMIT ? OFFSET ?", (limit, offset))
    
    rows = cur.fetchall()

    conn.close()

    return {
        "limit": limit,
        "offset": offset,
        "users": rows}

@app.delete("/users/{user_id}")
def delete_user(user_id: int):

    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "DELETE FROM users WHERE id = ?", 
        (user_id,)
    )
    conn.commit()
    conn.close()
    
    return {"message": "user deleted"}


@app.put("/users/{user_id}")
def update_user(user_id: int, name: str, followers: int):

    conn = get_connection()
    cur = conn.cursor()
    
    cur.execute(
        "UPDATE users SET name = ?, followers = ? WHERE id = ?",
        (name, followers, user_id)
    )
    conn.commit()
    conn.close()
    return {"message": "user updated"}

@app.post("/users")
def create_user(user: UserCreate):
    
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO users (name, followers) VALUES (?, ?)",
        (user.name, user.followers)
    )
    conn.commit()
    conn.close()

    return {"message": "user created"}