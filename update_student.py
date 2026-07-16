import tkinter as tk
from tkinter import messagebox
import sqlite3

def open_update_student():

    window = tk.Toplevel()
    window.title("Update Student")
    window.geometry("500x500")

    tk.Label(window, text="Update Student", font=("Arial", 18, "bold")).pack(pady=10)

    tk.Label(window, text="Roll Number").pack()
    roll = tk.Entry(window, width=30)
    roll.pack()

    tk.Label(window, text="Student Name").pack()
    name = tk.Entry(window, width=30)
    name.pack()

    tk.Label(window, text="Age").pack()
    age = tk.Entry(window, width=30)
    age.pack()

    tk.Label(window, text="Department").pack()
    department = tk.Entry(window, width=30)
    department.pack()

    tk.Label(window, text="Phone").pack()
    phone = tk.Entry(window, width=30)
    phone.pack()

    def load_student():
        conn = sqlite3.connect("student.db")
        cursor = conn.cursor()

        cursor.execute(
            "SELECT * FROM students WHERE roll=?",
            (roll.get(),)
        )

        student = cursor.fetchone()
        conn.close()

        if student:
            name.delete(0, tk.END)
            age.delete(0, tk.END)
            department.delete(0, tk.END)
            phone.delete(0, tk.END)

            name.insert(0, student[1])
            age.insert(0, student[3])
            department.insert(0, student[4])
            phone.insert(0, student[5])
        else:
            messagebox.showerror("Error", "Student Not Found")

    def update_student():
        conn = sqlite3.connect("student.db")
        cursor = conn.cursor()

        cursor.execute(
            """
            UPDATE students
            SET name=?, age=?, department=?, phone=?
            WHERE roll=?
            """,
            (
                name.get(),
                age.get(),
                department.get(),
                phone.get(),
                roll.get()
            )
        )

        conn.commit()
        conn.close()

        messagebox.showinfo("Success", "Student Updated Successfully")

    tk.Button(
        window,
        text="Load Student",
        width=20,
        command=load_student
    ).pack(pady=10)

    tk.Button(
        window,
        text="Update",
        width=20,
        command=update_student
    ).pack(pady=10)