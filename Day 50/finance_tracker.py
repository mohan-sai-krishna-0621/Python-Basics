
import csv
import os
from datetime import date

FILE_NAME = "transactions.csv"

transactions = []


# Create CSV file if it does not exist
def create_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([
                "ID", "Type", "Amount",
                "Category", "Description", "Date"
            ])


# Load transactions from CSV
def load_transactions():
    global transactions

    transactions = []

    create_file()

    with open(FILE_NAME, "r", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            transactions.append(row)


# Save transactions to CSV
def save_transactions():
    with open(FILE_NAME, "w", newline="") as file:
        fieldnames = [
            "ID", "Type", "Amount",
            "Category", "Description", "Date"
        ]

        writer = csv.DictWriter(
            file,
            fieldnames=fieldnames
        )

        writer.writeheader()
        writer.writerows(transactions)


# Get valid amount
def get_amount():
    while True:
        try:
            amount = float(input("Enter amount: ₹"))

            if amount <= 0:
                print("Amount must be greater than zero!")
                continue

            return amount

        except ValueError:
            print("Please enter a valid amount!")


# Add income or expense
def add_transaction(transaction_type):
    print(f"\n===== ADD {transaction_type.upper()} =====")

    amount = get_amount()

    category = input("Enter category: ").strip()
    description = input("Enter description: ").strip()

    if not category or not description:
        print("Category and description cannot be empty!")
        return

    transaction_id = max(
        [int(t["ID"]) for t in transactions],
        default=0
    ) + 1

    transaction = {
        "ID": str(transaction_id),
        "Type": transaction_type,
        "Amount": str(amount),
        "Category": category,
        "Description": description,
        "Date": date.today().isoformat()
    }

    transactions.append(transaction)

    save_transactions()

    print(f"{transaction_type} added successfully!")


# Display all transactions
def view_transactions():
    print("\n===== ALL TRANSACTIONS =====")

    if not transactions:
        print("No transactions found!")
        return

    for t in transactions:
        print("\n--------------------------")
        print(f"ID: {t['ID']}")
        print(f"Type: {t['Type']}")
        print(f"Amount: ₹{float(t['Amount']):.2f}")
        print(f"Category: {t['Category']}")
        print(f"Description: {t['Description']}")
        print(f"Date: {t['Date']}")

    print("\nTotal transactions:", len(transactions))


# Calculate financial summary
def financial_summary():
    income = sum(
        float(t["Amount"])
        for t in transactions
        if t["Type"] == "Income"
    )

    expenses = sum(
        float(t["Amount"])
        for t in transactions
        if t["Type"] == "Expense"
    )

    balance = income - expenses

    print("\n===== FINANCIAL SUMMARY =====")
    print(f"Total Income: ₹{income:.2f}")
    print(f"Total Expenses: ₹{expenses:.2f}")
    print(f"Current Balance: ₹{balance:.2f}")


# Show category-wise expenses
def category_summary():
    categories = {}

    for t in transactions:
        if t["Type"] == "Expense":
            category = t["Category"]

            categories[category] = (
                categories.get(category, 0)
                + float(t["Amount"])
            )

    print("\n===== CATEGORY SUMMARY =====")

    if not categories:
        print("No expenses available!")
        return

    for category, amount in categories.items():
        print(f"{category}: ₹{amount:.2f}")


# Delete transaction
def delete_transaction():
    transaction_id = input(
        "\nEnter transaction ID to delete: "
    ).strip()

    for t in transactions:
        if t["ID"] == transaction_id:
            transactions.remove(t)
            save_transactions()

            print("Transaction deleted successfully!")
            return

    print("Transaction ID not found!")


# Main menu
def main():

    load_transactions()

    while True:

        print("\n===== PERSONAL FINANCE TRACKER =====")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. View All Transactions")
        print("4. Financial Summary")
        print("5. Category-wise Expenses")
        print("6. Delete Transaction")
        print("7. Exit")

        choice = input("\nChoose an option (1-7): ").strip()

        if choice == "1":
            add_transaction("Income")

        elif choice == "2":
            add_transaction("Expense")

        elif choice == "3":
            view_transactions()

        elif choice == "4":
            financial_summary()

        elif choice == "5":
            category_summary()

        elif choice == "6":
            delete_transaction()

        elif choice == "7":
            print("Thank you for using Personal Finance Tracker!")
            break

        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()
