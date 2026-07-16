import tkinter as tk
import sqlite3

def open_search_student():

    window = tk.Toplevel()
    window.title("Search Student")
    window.geometry("400x300")

    tk.Label(window, text="Enter Roll Number", font=("Arial", 12)).pack(pady=10)

    roll_entry = tk.Entry(window, width=30)
    roll_entry.pack()

    result = tk.Label(window, text="", justify="left", font=("Arial", 11))
    result.pack(pady=20)

    def search():

        conn = sqlite3.connect("student.db")
        cursor = conn.cursor()

        cursor.execute(
            "SELECT * FROM students WHERE roll=?",
            (roll_entry.get(),)
        )

        student = cursor.fetchone()

        conn.close()

        if student:
            result.config(
                text=f"Name : {student[1]}\n"
                     f"Roll : {student[2]}\n"
                     f"Age : {student[3]}\n"
                     f"Department : {student[4]}\n"
                     f"Phone : {student[5]}"
            )
        else:
            result.config(text="Student Not Found")

    tk.Button(window, text="Search", command=search).pack(pady=10)