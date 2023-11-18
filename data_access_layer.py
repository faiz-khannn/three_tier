# data_access_layer.py

import pyodbc

class EmployeeDatabase:
    def __init__(self):
        self.conn = pyodbc.connect('DRIVER={SQL Server};SERVER=your_server_name;DATABASE=EmployeeDB;UID=your_username;PWD=your_password')

    def add_employee(self, name, department):
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO Employees (Name, Department) VALUES (?, ?)", name, department)
        self.conn.commit()

    def get_employees(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM Employees")
        return cursor.fetchall()

    def update_employee(self, employee_id, name, department):
        cursor = self.conn.cursor()
        cursor.execute("UPDATE Employees SET Name = ?, Department = ? WHERE EmployeeID = ?", name, department, employee_id)
        self.conn.commit()

    def delete_employee(self, employee_id):
        cursor = self.conn.cursor()
        cursor.execute("DELETE FROM Employees WHERE EmployeeID = ?", employee_id)
        self.conn.commit()
