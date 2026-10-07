
class Expense:
    def __init__(self, name, amount, category):
        self.name = name
        self.amount = amount
        self.category = category


expenses = []


def add_expense():
    name = input("Enter expense name: ").strip()
    category = input("Enter category: ").strip()

    if not name or not category:
        print("Name and category cannot be empty.")
        return

    try:
        amount = float(input("Enter amount: ₹"))

        if amount <= 0:
            print("Amount must be greater than zero.")
            return

        expense = Expense(name, amount, category)
        expenses.append(expense)

        print("Expense added successfully!")

    except ValueError:
        print("Invalid amount. Please enter a number.")


def view_expenses():
    if not expenses:
        print("No expenses found.")
        return

    print("\n===== EXPENSES =====")
    total = 0

    for i, expense in enumerate(expenses, start=1):
        print(f"\nExpense {i}")
        print("Name:", expense.name)
        print(f"Amount: ₹{expense.amount:.2f}")
        print("Category:", expense.category)
        total += expense.amount

    print("\n--------------------")
    print(f"Total Expense: ₹{total:.2f}")


def category_summary():
    if not expenses:
        print("No expenses available.")
        return

    category_totals = {}

    for expense in expenses:
        category = expense.category

        if category in category_totals:
            category_totals[category] += expense.amount
        else:
            category_totals[category] = expense.amount

    print("\n===== CATEGORY SUMMARY =====")

    for category, amount in category_totals.items():
        print(f"{category}: ₹{amount:.2f}")


def search_by_category():
    if not expenses:
        print("No expenses available.")
        return

    category = input("Enter category to search: ").strip()
    found = False
    total = 0

    print(f"\n===== {category.upper()} EXPENSES =====")

    for expense in expenses:
        if expense.category.lower() == category.lower():
            print(f"{expense.name} - ₹{expense.amount:.2f}")
            total += expense.amount
            found = True

    if found:
        print("--------------------")
        print(f"Category Total: ₹{total:.2f}")
    else:
        print("No expenses found for this category.")


while True:
    print("\n===== EXPENSE TRACKER PRO =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Category Summary")
    print("4. Search by Category")
    print("5. Exit")

    choice = input("Enter your choice: ").strip()

    if choice == "1":
        add_expense()

    elif choice == "2":
        view_expenses()

    elif choice == "3":
        category_summary()

    elif choice == "4":
        search_by_category()

    elif choice == "5":
        print("Thank you for using Expense Tracker Pro!")
        break

    else:
        print("Invalid choice. Please select 1–5.")
