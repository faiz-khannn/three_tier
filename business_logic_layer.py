# business_logic_layer.py

from data_access_layer import EmployeeDatabase

class EmployeeManager:
    def __init__(self):
        self.db = EmployeeDatabase()

    def add_employee(self, name, department):
        self.db.add_employee(name, department)

    def view_employees(self):
        employees = self.db.get_employees()
        for employee in employees:
            print(f"ID: {employee[0]}, Name: {employee[1]}, Department: {employee[2]}")

    def update_employee(self, employee_id, name, department):
        self.db.update_employee(employee_id, name, department)

    def delete_employee(self, employee_id):
        self.db.delete_employee(employee_id)
