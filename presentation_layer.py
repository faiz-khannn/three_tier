# presentation_layer.py

from business_logic_layer import EmployeeManager

def main():
    employee_manager = EmployeeManager()

    while True:
        print("\nEmployee Management System")
        print("1. Add Employee")
        print("2. View Employees")
        print("3. Update Employee")
        print("4. Delete Employee")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter employee name: ")
            department = input("Enter employee department: ")
            employee_manager.add_employee(name, department)
        elif choice == "2":
            employee_manager.view_employees()
        elif choice == "3":
            employee_id = input("Enter employee ID to update: ")
            name = input("Enter updated name: ")
            department = input("Enter updated department: ")
            employee_manager.update_employee(employee_id, name, department)
        elif choice == "4":
            employee_id = input("Enter employee ID to delete: ")
            employee_manager.delete_employee(employee_id)
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
