class Expense:
    def __init__(self, name, amount, category):
        self.name = name
        self.amount = amount
        self.category = category


expenses = []


def add_expense():
    name = input("Enter expense name: ")
    amount = float(input("Enter amount: ₹"))
    category = input("Enter category: ")

    expense = Expense(name, amount, category)
    expenses.append(expense)

    print("Expense added successfully!")


def save_expense():
    with open("expenses.txt", "w") as file:
        for expense in expenses:
            file.write(
                f"{expense.name},{expense.amount},{expense.category}\n"
            )

    print("Expenses saved to file successfully!")


# Main program
while True:
    print("\n===== EXPENSE FILE MANAGER =====")
    print("1. Add Expense")
    print("2. Save Expenses")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        save_expense()

    elif choice == "3":
        print("Thank you!")
        break

    else:
        print("Invalid choice!")