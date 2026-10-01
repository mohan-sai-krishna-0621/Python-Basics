expenses = []

def add_expense():
    name = input("Enter expense name: ")
    amount = float(input("Enter amount: "))

    expense = {
        "name": name,
        "amount": amount
    }

    expenses.append(expense)
    print("Expense added successfully!")


def view_expenses():
    if len(expenses) == 0:
        print("No expenses recorded.")
        return

    print("\n--- Expense List ---")

    total = 0

    for expense in expenses:
        print(f"{expense['name']} : ₹{expense['amount']}")
        total += expense["amount"]

    print(f"Total Expense: ₹{total}")


while True:
    print("\n===== EXPENSE TRACKER =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        view_expenses()

    elif choice == "3":
        print("Thank you for using Expense Tracker!")
        break

    else:
        print("Invalid choice. Please try again.")