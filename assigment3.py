import tkinter as tk
from tkinter import messagebox

def add_task():
    task = task_entry.get()
    if task != "":
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def delete_task():
    try:
        selected_task_index = task_listbox.curselection()[0]
        task_listbox.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete.")

def mark_done():
    try:
        selected_task_index = task_listbox.curselection()[0]
        task = task_listbox.get(selected_task_index)
        task_listbox.delete(selected_task_index)
        task_listbox.insert(tk.END, f"{task} ✅")
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to mark as done.")

# Create the main application window
app = tk.Tk()
app.title("To-Do List")
app.geometry("400x500")

# Input field and buttons
task_entry = tk.Entry(app, width=30, font=("Arial", 14))
task_entry.pack(pady=10)

add_button = tk.Button(app, text="Add Task", width=15, command=add_task)
add_button.pack(pady=5)

delete_button = tk.Button(app, text="Delete Task", width=15, command=delete_task)
delete_button.pack(pady=5)

mark_done_button = tk.Button(app, text="Mark as Done", width=15, command=mark_done)
mark_done_button.pack(pady=5)

# Task list
task_listbox = tk.Listbox(app, width=40, height=15, font=("Arial", 14))
task_listbox.pack(pady=20)

# Run the application
app.mainloop()