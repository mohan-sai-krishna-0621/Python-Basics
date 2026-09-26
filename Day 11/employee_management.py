
# employee_management.py

class Employee:
    def __init__(self, emp_id, name, salary, department):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary
        self.department = department

    def display(self):
        print("Employee ID:", self.emp_id)
        print("Name:", self.name)
        print("Salary:", self.salary)
        print("Department:", self.department)
        print("-" * 30)


class EmployeeManagement:
    def __init__(self):
        self.employees = []

    def add_employee(self):
        emp_id = input("Enter Employee ID: ")
        name = input("Enter Employee Name: ")
        salary = float(input("Enter Salary: "))
        department = input("Enter Department: ")

        employee = Employee(emp_id, name, salary, department)
        self.employees.append(employee)

        print("Employee added successfully!")

    def display_employees(self):
        if not self.employees:
            print("No employees found.")
        else:
            for employee in self.employees:
                employee.display()

    def search_employee(self):
        emp_id = input("Enter Employee ID to search: ")

        for employee in self.employees:
            if employee.emp_id == emp_id:
                print("Employee Found!")
                employee.display()
                return

        print("Employee not found.")


# Main program
management = EmployeeManagement()

while True:
    print("\n===== Employee Management System =====")
    print("1. Add Employee")
    print("2. Display Employees")
    print("3. Search Employee")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        management.add_employee()

    elif choice == "2":
        management.display_employees()

    elif choice == "3":
        management.search_employee()

    elif choice == "4":
        print("Exiting Employee Management System.")
        break

    else:
        print("Invalid choice. Try again.")