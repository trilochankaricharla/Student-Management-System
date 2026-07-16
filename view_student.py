import tkinter as tk
import sqlite3
from tkinter import ttk

def open_view_students():

    window = tk.Toplevel()
    window.title("View Students")
    window.geometry("700x400")

    tree = ttk.Treeview(
        window,
        columns=("ID", "Name", "Roll", "Age", "Department", "Phone"),
        show="headings"
    )

    tree.heading("ID", text="ID")
    tree.heading("Name", text="Name")
    tree.heading("Roll", text="Roll")
    tree.heading("Age", text="Age")
    tree.heading("Department", text="Department")
    tree.heading("Phone", text="Phone")

    tree.pack(fill="both", expand=True)

    conn = sqlite3.connect("student.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM students")

    rows = cursor.fetchall()

    for row in rows:
        tree.insert("", tk.END, values=row)

    conn.close()