# Day 09 - Expense Tracker

expenses = []

while True:
    print("\n--- Expense Tracker ---")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Show Total Expense")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter expense name: ")

        try:
            amount = float(input("Enter amount: "))

            if amount < 0:
                print("Amount cannot be negative.")
            else:
                expense = {
                    "name": name,
                    "amount": amount
                }

                expenses.append(expense)

                print("Expense added successfully.")

        except ValueError:
            print("Please enter a valid amount.")

    elif choice == "2":
        if len(expenses) == 0:
            print("No expenses recorded.")
        else:
            print("\nYour Expenses:")

            for expense in expenses:
                print("--------------------")
                print("Expense:", expense["name"])
                print("Amount: ₹", expense["amount"])

    elif choice == "3":
        total = 0

        for expense in expenses:
            total += expense["amount"]

        print("\nTotal Expense: ₹", total)

    elif choice == "4":
        print("Thank you for using Expense Tracker.")
        break

    else:
        print("Invalid choice. Please try again.")