
import os

transactions = []
monthly_budget = 0.0
FILE_NAME = "budget_transactions.txt"


def load_transactions():
    global monthly_budget

    if not os.path.exists(FILE_NAME):
        return

    try:
        with open(FILE_NAME, "r") as file:
            for line in file:
                data = line.strip().split("|")

                if data[0] == "BUDGET":
                    monthly_budget = float(data[1])

                elif data[0] == "TRANSACTION" and len(data) == 5:
                    transactions.append({
                        "type": data[1],
                        "category": data[2],
                        "description": data[3],
                        "amount": float(data[4])
                    })

    except (ValueError, IndexError):
        print("Warning: Some saved data could not be loaded.")


def save_data():
    with open(FILE_NAME, "w") as file:
        file.write(f"BUDGET|{monthly_budget}\n")

        for transaction in transactions:
            file.write(
                f"TRANSACTION|{transaction['type']}|"
                f"{transaction['category']}|"
                f"{transaction['description']}|"
                f"{transaction['amount']}\n"
            )


def set_budget():
    global monthly_budget

    try:
        amount = float(input("Enter monthly budget: ₹"))

        if amount <= 0:
            print("Budget must be greater than zero.")
            return

        monthly_budget = amount
        save_data()
        print("Monthly budget set successfully!")

    except ValueError:
        print("Please enter a valid amount.")


def add_transaction():
    transaction_type = input(
        "Enter type (income/expense): "
    ).strip().lower()

    if transaction_type not in ("income", "expense"):
        print("Invalid type! Enter income or expense.")
        return

    category = input("Enter category: ").strip()
    description = input("Enter description: ").strip()

    try:
        amount = float(input("Enter amount: ₹"))

        if amount <= 0:
            print("Amount must be greater than zero.")
            return

        transaction = {
            "type": transaction_type,
            "category": category,
            "description": description,
            "amount": amount
        }

        transactions.append(transaction)
        save_data()

        print("Transaction added successfully!")

    except ValueError:
        print("Please enter a valid amount.")


def view_transactions():
    if not transactions:
        print("No transactions recorded yet.")
        return

    print("\n--- ALL TRANSACTIONS ---")

    for number, transaction in enumerate(transactions, start=1):
        print(f"\nTransaction {number}")
        print(f"Type: {transaction['type'].title()}")
        print(f"Category: {transaction['category']}")
        print(f"Description: {transaction['description']}")
        print(f"Amount: ₹{transaction['amount']:.2f}")


def show_summary():
    total_income = sum(
        t["amount"] for t in transactions
        if t["type"] == "income"
    )

    total_expenses = sum(
        t["amount"] for t in transactions
        if t["type"] == "expense"
    )

    balance = total_income - total_expenses
    remaining_budget = monthly_budget - total_expenses

    print("\n--- BUDGET SUMMARY ---")
    print(f"Monthly Budget: ₹{monthly_budget:.2f}")
    print(f"Total Income: ₹{total_income:.2f}")
    print(f"Total Expenses: ₹{total_expenses:.2f}")
    print(f"Current Balance: ₹{balance:.2f}")
    print(f"Remaining Budget: ₹{remaining_budget:.2f}")

    if remaining_budget < 0:
        print("Warning: You have exceeded your budget!")
    elif monthly_budget > 0:
        print("You are within your budget.")


def main():
    load_transactions()

    while True:
        print("\n===== PERSONAL BUDGET PLANNER =====")
        print("1. Set Monthly Budget")
        print("2. Add Income or Expense")
        print("3. View Transactions")
        print("4. Show Budget Summary")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            set_budget()
        elif choice == "2":
            add_transaction()
        elif choice == "3":
            view_transactions()
        elif choice == "4":
            show_summary()
        elif choice == "5":
            print("Budget Planner closed. Goodbye!")
            break
        else:
            print("Invalid choice! Please enter 1-5.")


if __name__ == "__main__":
    main()
