
class BankAccount:
    def __init__(self, account_holder, initial_balance=0):
        if initial_balance < 0:
            raise ValueError("Initial balance cannot be negative.")

        self.account_holder = account_holder
        self.balance = initial_balance
        self.transactions = []

        self.transactions.append(
            f"Account created with balance: ₹{initial_balance:.2f}"
        )

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be greater than zero.")
            return

        self.balance += amount
        self.transactions.append(f"Deposited: ₹{amount:.2f}")
        print("Deposit successful!")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be greater than zero.")
            return

        if amount > self.balance:
            print("Insufficient balance!")
            return

        self.balance -= amount
        self.transactions.append(f"Withdrawn: ₹{amount:.2f}")
        print("Withdrawal successful!")

    def check_balance(self):
        print(f"\nAccount holder: {self.account_holder}")
        print(f"Current balance: ₹{self.balance:.2f}")

    def show_transactions(self):
        print("\n===== TRANSACTION HISTORY =====")

        for number, transaction in enumerate(self.transactions, start=1):
            print(f"{number}. {transaction}")


def get_amount(message):
    while True:
        try:
            amount = float(input(message))

            if amount <= 0:
                print("Enter an amount greater than zero.")
                continue

            return amount

        except ValueError:
            print("Invalid input! Please enter a numeric amount.")


def main():
    print("===== BANK ACCOUNT SIMULATOR =====")

    account_holder = input("Enter account holder name: ").strip()

    if not account_holder:
        print("Account holder name cannot be empty.")
        return

    account = BankAccount(account_holder)

    while True:
        print("\n===== MENU =====")
        print("1. Deposit Money")
        print("2. Withdraw Money")
        print("3. Check Balance")
        print("4. Transaction History")
        print("5. Exit")

        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            amount = get_amount("Enter deposit amount: ₹")
            account.deposit(amount)

        elif choice == "2":
            amount = get_amount("Enter withdrawal amount: ₹")
            account.withdraw(amount)

        elif choice == "3":
            account.check_balance()

        elif choice == "4":
            account.show_transactions()

        elif choice == "5":
            print("Thank you for using Bank Account Simulator!")
            break

        else:
            print("Invalid choice! Select an option from 1 to 5.")


if __name__ == "__main__":
    main()
