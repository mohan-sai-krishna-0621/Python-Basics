
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be greater than zero.")
        else:
            self.__balance += amount
            print(f"₹{amount:.2f} deposited successfully.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be greater than zero.")
        elif amount > self.__balance:
            print("Insufficient balance.")
        else:
            self.__balance -= amount
            print(f"₹{amount:.2f} withdrawn successfully.")

    def check_balance(self):
        print(f"Account holder: {self.owner}")
        print(f"Current balance: ₹{self.__balance:.2f}")


def main():
    owner = input("Enter account holder name: ").strip()

    if not owner:
        print("Name cannot be empty.")
        return

    account = BankAccount(owner)

    while True:
        print("\n--- Bank Account Menu ---")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            try:
                amount = float(input("Enter deposit amount: ₹"))
                account.deposit(amount)
            except ValueError:
                print("Please enter a valid number.")

        elif choice == "2":
            try:
                amount = float(input("Enter withdrawal amount: ₹"))
                account.withdraw(amount)
            except ValueError:
                print("Please enter a valid number.")

        elif choice == "3":
            account.check_balance()

        elif choice == "4":
            print("Thank you for using the Bank Account System!")
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
