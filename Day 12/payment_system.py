class Payment:
    def pay(self, amount):
        pass


class UPI(Payment):
    def pay(self, amount):
        print(f"Paid Rs.{amount} using UPI")


class CreditCard(Payment):
    def pay(self, amount):
        print(f"Paid Rs.{amount} using Credit Card")


class Cash(Payment):
    def pay(self, amount):
        print(f"Paid Rs.{amount} using Cash")


payments = [UPI(), CreditCard(), Cash()]

for payment in payments:
    payment.pay(500)