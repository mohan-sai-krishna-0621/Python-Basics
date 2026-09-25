class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Deposited:", amount)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawn:", amount)
        else:
            print("Insufficient balance")

    def display_balance(self):
        print("Account Holder:", self.name)
        print("Balance:", self.balance)


account = BankAccount("Mohan", 5000)

account.display_balance()

account.deposit(2000)
account.display_balance()

account.withdraw(1500)
account.display_balance()