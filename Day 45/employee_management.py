class Employee:
    def __init__(self, name, employee_id):
        self.name = name
        self.employee_id = employee_id

    def calculate_salary(self):
        raise NotImplementedError(
            "Child classes must implement calculate_salary()."
        )

    def display_details(self):
        print(f"\nEmployee ID: {self.employee_id}")
        print(f"Name: {self.name}")
        print(f"Employee Type: {self.__class__.__name__}")
        print(f"Salary: ₹{self.calculate_salary():,.2f}")


class FullTimeEmployee(Employee):
    def __init__(self, name, employee_id, monthly_salary):
        super().__init__(name, employee_id)
        self.monthly_salary = monthly_salary

    def calculate_salary(self):
        return self.monthly_salary


class PartTimeEmployee(Employee):
    def __init__(self, name, employee_id, hours_worked, hourly_rate):
        super().__init__(name, employee_id)
        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate

    def calculate_salary(self):
        return self.hours_worked * self.hourly_rate


class CommissionEmployee(Employee):
    def __init__(self, name, employee_id, base_salary, sales, commission_rate):
        super().__init__(name, employee_id)
        self.base_salary = base_salary
        self.sales = sales
        self.commission_rate = commission_rate

    def calculate_salary(self):
        commission = self.sales * self.commission_rate / 100
        return self.base_salary + commission


def get_number(message, minimum=0):
    while True:
        try:
            value = float(input(message))

            if value < minimum:
                print(f"Please enter a number greater than or equal to {minimum}.")
                continue

            return value

        except ValueError:
            print("Invalid input! Please enter a number.")


def get_employee_id():
    while True:
        employee_id = input("Enter employee ID: ").strip()

        if not employee_id:
            print("Employee ID cannot be empty.")
        else:
            return employee_id


def main():
    employees = []

    while True:
        print("\n===== EMPLOYEE MANAGEMENT SYSTEM =====")
        print("1. Add Full-Time Employee")
        print("2. Add Part-Time Employee")
        print("3. Add Commission Employee")
        print("4. Display All Employees")
        print("5. Exit")

        choice = input("Choose an option (1-5): ").strip()

        if choice in ("1", "2", "3"):
            name = input("Enter employee name: ").strip()

            if not name:
                print("Employee name cannot be empty.")
                continue

            employee_id = get_employee_id()

            if any(e.employee_id == employee_id for e in employees):
                print("This employee ID already exists!")
                continue

            if choice == "1":
                salary = get_number("Enter monthly salary: ₹")

                employee = FullTimeEmployee(
                    name, employee_id, salary
                )

            elif choice == "2":
                hours = get_number("Enter hours worked: ", 0)
                rate = get_number("Enter hourly rate: ₹", 0)

                employee = PartTimeEmployee(
                    name, employee_id, hours, rate
                )

            else:
                base_salary = get_number("Enter base salary: ₹")
                sales = get_number("Enter total sales: ₹")
                commission_rate = get_number(
                    "Enter commission rate (%): ", 0
                )

                if commission_rate > 100:
                    print("Commission rate cannot exceed 100%.")
                    continue

                employee = CommissionEmployee(
                    name,
                    employee_id,
                    base_salary,
                    sales,
                    commission_rate
                )

            employees.append(employee)
            print("Employee added successfully!")

        elif choice == "4":
            if not employees:
                print("\nNo employees found.")
                continue

            print("\n===== EMPLOYEE DETAILS =====")

            for employee in employees:
                employee.display_details()

            print(f"\nTotal Employees: {len(employees)}")

        elif choice == "5":
            print("Thank you for using Employee Management System!")
            break

        else:
            print("Invalid choice! Please select an option from 1 to 5.")


if __name__ == "__main__":
    main()
