import json
import os

FILE_NAME = "expenses.json"
expenses = []


def load_expenses():
    global expenses

    if not os.path.exists(FILE_NAME):
        expenses = []
        return

    try:
        with open(FILE_NAME, "r") as file:
            data = json.load(file)

        if isinstance(data, list):
            expenses = data
        else:
            expenses = []
            print("Invalid file format. Starting with empty expenses.")

    except (json.JSONDecodeError, OSError):
        expenses = []
        print("Could not load expenses. Starting fresh.")


def save_expenses():
    try:
        with open(FILE_NAME, "w") as file:
            json.dump(expenses, file, indent=4)
    except OSError:
        print("Error: Could not save expenses.")


def add_expense():
    name = input("Enter expense name: ").strip()
    if not name:
        print("Expense name cannot be empty.")
        return

    try:
        amount = float(input("Enter amount: ₹"))

        if amount <= 0:
            print("Amount must be greater than zero.")
            return

    except ValueError:
        print("Please enter a valid number.")
        return

    category = input("Enter category: ").strip().title()
    if not category:
        print("Category cannot be empty.")
        return

    expense = {
        "name": name,
        "amount": amount,
        "category": category
    }

    expenses.append(expense)
    save_expenses()

    print("Expense added successfully!")


def view_expenses():
    if not expenses:
        print("No expenses recorded yet.")
        return

    print("\n===== ALL EXPENSES =====")

    for number, expense in enumerate(expenses, start=1):
        print(
            f"{number}. {expense['name']} | "
            f"₹{expense['amount']:.2f} | "
            f"{expense['category']}"
        )


def show_total():
    total = sum(expense["amount"] for expense in expenses)
    print(f"Total spending: ₹{total:.2f}")


def category_summary():
    if not expenses:
        print("No expenses available for analysis.")
        return

    summary = {}

    for expense in expenses:
        category = expense["category"]
        amount = expense["amount"]

        summary[category] = summary.get(category, 0) + amount

    print("\n===== CATEGORY SUMMARY =====")

    for category, total in summary.items():
        print(f"{category}: ₹{total:.2f}")


def main():
    load_expenses()

    while True:
        print("\n===== SMART EXPENSE ANALYZER =====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Show Total Spending")
        print("4. Category Summary")
        print("5. Exit")

        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            show_total()
        elif choice == "4":
            category_summary()
        elif choice == "5":
            print("Thank you for using Smart Expense Analyzer!")
            break
        else:
            print("Invalid choice. Please select 1-5.")


if __name__ == "__main__":
    main()
