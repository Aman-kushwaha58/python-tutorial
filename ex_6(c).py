import tkinter as tk
from tkinter import messagebox

def generate_marksheet():
    name = name_entry.get()
    roll_no = roll_no_entry.get()
    subject1 = int(subject1_entry.get())
    subject2 = int(subject2_entry.get())
    subject3 = int(subject3_entry.get())
    subject4 = int(subject4_entry.get())
    subject5 = int(subject5_entry.get())

    total_marks = subject1 + subject2 + subject3 + subject4 + subject5
    percentage = (total_marks / 500) * 100
    result = "Pass" if percentage >= 40 else "Fail"

    marksheet = f"Marksheet\n\nName: {name}\nRoll No: {roll_no}\n\nSubject 1: {subject1}\nSubject 2: {subject2}\nSubject 3: {subject3}\nSubject 4: {subject4}\nSubject 5: {subject5}\n\nTotal Marks: {total_marks}\nPercentage: {percentage:.2f}%\nResult: {result}"

    messagebox.showinfo("Marksheet", marksheet)

root = tk.Tk()
root.title("Student Marksheet Generator")

root.geometry("400x400")

name_label = tk.Label(root, text="Student Name")
name_label.grid(row=0, column=0, padx=10, pady=10)
name_entry = tk.Entry(root, width=30)
name_entry.grid(row=0, column=1, padx=10, pady=10)

roll_no_label = tk.Label(root, text="Roll Number")
roll_no_label.grid(row=1, column=0, padx=10, pady=10)
roll_no_entry = tk.Entry(root, width=30)
roll_no_entry.grid(row=1, column=1, padx=10, pady=10)

subject1_label = tk.Label(root, text="Subject 1 Marks")
subject1_label.grid(row=2, column=0, padx=10, pady=10)
subject1_entry = tk.Entry(root, width=30)
subject1_entry.grid(row=2, column=1, padx=10, pady=10)

subject2_label = tk.Label(root, text="Subject 2 Marks")
subject2_label.grid(row=3, column=0, padx=10, pady=10)
subject2_entry = tk.Entry(root, width=30)
subject2_entry.grid(row=3, column=1, padx=10, pady=10)

subject3_label = tk.Label(root, text="Subject 3 Marks")
subject3_label.grid(row=4, column=0, padx=10, pady=10)
subject3_entry = tk.Entry(root, width=30)
subject3_entry.grid(row=4, column=1, padx=10, pady=10)

subject4_label = tk.Label(root, text="Subject 4 Marks")
subject4_label.grid(row=5, column=0, padx=10, pady=10)
subject4_entry = tk.Entry(root, width=30)
subject4_entry.grid(row=5, column=1, padx=10, pady=10)

subject5_label = tk.Label(root, text="Subject 5 Marks")
subject5_label.grid(row=6, column=0, padx=10, pady=10)
subject5_entry = tk.Entry(root, width=30)
subject5_entry.grid(row=6, column=1, padx=10, pady=10)

generate_button = tk.Button(root, text="Generate Marksheet", command=generate_marksheet)
generate_button.grid(row=7, column=0, columnspan=2, pady=20)

root.mainloop()
