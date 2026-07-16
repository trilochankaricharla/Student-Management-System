import tkinter as tk
import sqlite3

def open_add_student():

    window = tk.Toplevel()
    window.title("Add Student")
    window.geometry("500x500")

    tk.Label(window, text="Add Student", font=("Arial", 18, "bold")).pack(pady=10)

    tk.Label(window, text="Student Name").pack()
    name = tk.Entry(window, width=30)
    name.pack()

    tk.Label(window, text="Roll Number").pack()
    roll = tk.Entry(window, width=30)
    roll.pack()

    tk.Label(window, text="Age").pack()
    age = tk.Entry(window, width=30)
    age.pack()

    tk.Label(window, text="Department").pack()
    department = tk.Entry(window, width=30)
    department.pack()

    tk.Label(window, text="Phone Number").pack()
    phone = tk.Entry(window, width=30)
    phone.pack()

    # Save Function
    def save_student():
        conn = sqlite3.connect("student.db")
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO students(name, roll, age, department, phone) VALUES (?, ?, ?, ?, ?)",
            (
                name.get(),
                roll.get(),
                age.get(),
                department.get(),
                phone.get()
            )
        )

        conn.commit()
        conn.close()

        print("Student Saved Successfully")

    tk.Button(
        window,
        text="Save",
        width=20,
        command=save_student
    ).pack(pady=20)