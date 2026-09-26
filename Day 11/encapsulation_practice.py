
# encapsulation_practice.py

class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print("Deposit successful!")
        else:
            print("Invalid deposit amount")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print("Withdrawal successful!")
        else:
            print("Insufficient balance or invalid amount")

    def display_balance(self):
        print("Account Holder:", self.name)
        print("Balance:", self.__balance)


account = BankAccount("Mohan", 5000)

account.display_balance()

account.deposit(2000)
account.withdraw(1000)

account.display_balance()