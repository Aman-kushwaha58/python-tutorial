import tkinter as tk
from tkinter import messagebox, filedialog
from tkinter import ttk
from datetime import datetime

class CourseRegistrationForm:
    def __init__(self, root):
        self.root = root
        self.root.title("Course Registration Form")

        tk.Label(root, text="Name:").grid(row=0, column=0, padx=10, pady=10)
        self.name_entry = tk.Entry(root)
        self.name_entry.grid(row=0, column=1, padx=10, pady=10)

        tk.Label(root, text="Email:").grid(row=1, column=0, padx=10, pady=10)
        self.email_entry = tk.Entry(root)
        self.email_entry.grid(row=1, column=1, padx=10, pady=10)

        tk.Label(root, text="Phone Number:").grid(row=2, column=0, padx=10, pady=10)
        self.phone_entry = tk.Entry(root)
        self.phone_entry.grid(row=2, column=1, padx=10, pady=10)

        tk.Label(root, text="Date of Birth:").grid(row=3, column=0, padx=10, pady=10)
        self.dob_entry = tk.Entry(root)
        self.dob_entry.grid(row=3, column=1, padx=10, pady=10)
        self.dob_entry.insert(0, "YYYY-MM-DD")

        tk.Label(root, text="Preferred Course:").grid(row=4, column=0, padx=10, pady=10)
        self.course_combobox = ttk.Combobox(root, values=["Python Programming", "Data Science", "Web Development", "Machine Learning"])
        self.course_combobox.grid(row=4, column=1, padx=10, pady=10)

        tk.Label(root, text="Preferred Time:").grid(row=5, column=0, padx=10, pady=10)
        self.time_entry = tk.Entry(root)
        self.time_entry.grid(row=5, column=1, padx=10, pady=10)
        self.time_entry.insert(0, "HH:MM")

        tk.Label(root, text="Upload Resume:").grid(row=6, column=0, padx=10, pady=10)
        self.resume_path = tk.StringVar()
        self.resume_entry = tk.Entry(root, textvariable=self.resume_path, state='readonly')
        self.resume_entry.grid(row=6, column=1, padx=10, pady=10)
        self.upload_button = tk.Button(root, text="Browse", command=self.upload_file)
        self.upload_button.grid(row=6, column=2, padx=10, pady=10)

        self.submit_button = tk.Button(root, text="Submit", command=self.submit_form)
        self.submit_button.grid(row=7, column=0, columnspan=3, pady=20)

    def upload_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf"), ("Word files", "*.docx"), ("All files", "*.*")])
        if file_path:
            self.resume_path.set(file_path)

    def submit_form(self):
        name = self.name_entry.get()
        email = self.email_entry.get()
        phone = self.phone_entry.get()
        dob = self.dob_entry.get()
        course = self.course_combobox.get()
        preferred_time = self.time_entry.get()
        resume = self.resume_path.get()

        if not name or not email or not phone or not dob or not course or not preferred_time or not resume:
            messagebox.showerror("Error", "Please fill in all fields.")
            return

        try:
            datetime.strptime(dob, "%Y-%m-%d")
        except ValueError:
            messagebox.showerror("Error", "Date of Birth must be in YYYY-MM-DD format.")
            return

        try:
            datetime.strptime(preferred_time, "%H:%M")
        except ValueError:
            messagebox.showerror("Error", "Preferred Time must be in HH:MM format.")
            return

        messagebox.showinfo("Success", f"Registration Successful!\nName: {name}\nEmail: {email}\nPhone: {phone}\nDOB: {dob}\nCourse: {course}\nPreferred Time: {preferred_time}\nResume: {resume}")

if __name__ == "__main__":
    root = tk.Tk()
    app = CourseRegistrationForm(root)
    root.mainloop()