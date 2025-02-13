class Employee:
    def __init__(self, emp_id, name):
        self.emp_id = emp_id
        self.name = name
        self.attendance = 0

    def mark_attendance(self):
        self.attendance += 1
        return f"Attendance marked for {self.name}. Total days present: {self.attendance}"

    def get_attendance(self):
        return f"Employee: {self.name}, ID: {self.emp_id}, Attendance: {self.attendance}"

class ApparelStore:
    def __init__(self):
        self.employees = {}

    def add_employee(self, emp_id, name):
        if emp_id not in self.employees:
            self.employees[emp_id] = Employee(emp_id, name)
            return f"Employee {name} added."
        return "Employee already exists"

    def mark_employee_attendance(self, emp_id):
        if emp_id in self.employees:
            return self.employees[emp_id].mark_attendance()
        return "Employee not found"

store = ApparelStore()
print(store.add_employee(101, "Aman kushwaha"))
print(store.mark_employee_attendance(101))
print(store.mark_employee_attendance(101))
