import sqlite3

def create_database():
    conn = sqlite3.connect("student.db")

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS students(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        roll TEXT,
        age INTEGER,
        department TEXT,
        phone TEXT
    )
    """)

    conn.commit()
    conn.close()