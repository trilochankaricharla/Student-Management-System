import os
import tkinter as tk
from tkinter import messagebox
from dashboard import open_dashboard
from database import create_database

create_database()

root = tk.Tk()
root.title("Student Management System")
root.geometry("900x600")
root.configure(bg="lightblue")

title = tk.Label(root,
                 text="Student Management System",
                 font=("Arial", 24, "bold"),
                 bg="lightblue",
                 fg="darkblue")
title.pack(pady=20)

login_frame = tk.Frame(root, bg="white", padx=20, pady=20)
login_frame.pack(pady=30)

username_label = tk.Label(login_frame, text="Username", font=("Arial", 12), bg="white")
username_label.grid(row=0, column=0, pady=10, sticky="w")

username_entry = tk.Entry(login_frame, width=30)
username_entry.grid(row=0, column=1, pady=10)

password_label = tk.Label(login_frame, text="Password", font=("Arial", 12), bg="white")
password_label.grid(row=1, column=0, pady=10, sticky="w")

password_entry = tk.Entry(login_frame, show="*", width=30)
password_entry.grid(row=1, column=1, pady=10)
def login():
    username = username_entry.get()
    password = password_entry.get()

    if username == os.getenv("ADMIN_USERNAME") and password == os.getenv("ADMIN_PASSWORD"): 
        root.destroy()
        open_dashboard()
    else:
        messagebox.showerror("Error", "Invalid Username or Password")
login_button = tk.Button(login_frame,
                         text="Login",
                         font=("Arial", 12, "bold"),
                         bg="blue",
                         fg="white",
                         width=15,
                         command=login)
login_button.grid(row=2, column=0, columnspan=2, pady=20)

root.mainloop()
