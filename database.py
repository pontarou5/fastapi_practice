import sqlite3

DB_NAME ="users.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            followers INTEGER
            )
            """)
    conn.commit()
    conn.close()
    