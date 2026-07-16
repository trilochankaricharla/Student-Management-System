import tkinter as tk
from add_student import open_add_student
from view_student import open_view_students
from search_student import open_search_student
from update_student import open_update_student
from delete_student import open_delete_student

def open_dashboard():
    dashboard = tk.Tk()
    dashboard.title("Student Management System")
    dashboard.geometry("900x600")
    dashboard.configure(bg="white")

    title = tk.Label(
        dashboard,
        text="Student Management System",
        font=("Arial", 24, "bold"),
        fg="blue",
        bg="white"
    )
    title.pack(pady=20)

    tk.Button(
        dashboard,
        text="Add Student",
        width=25,
        height=2,
        command=open_add_student
    ).pack(pady=10)

    tk.Button(
        dashboard,
        text="View Students",
        width=25,
        height=2,
        command=open_view_students
    ).pack(pady=10)

    tk.Button(
        dashboard,
        text="Search Student",
        width=25,
        height=2,
        command=open_search_student
    ).pack(pady=10)

    tk.Button(
        dashboard,
        text="Update Student",
        width=25,
        height=2,
        command=open_update_student
    ).pack(pady=10)

    tk.Button(
    dashboard,
    text="Delete Student",
    width=25,
    height=2,
    command=open_delete_student
).pack(pady=10)

    tk.Button(
        dashboard,
        text="Exit",
        width=25,
        height=2,
        command=dashboard.destroy
    ).pack(pady=10)

    dashboard.mainloop()