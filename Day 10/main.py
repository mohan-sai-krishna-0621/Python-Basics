# main.py

import calculator

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

print("Addition:", calculator.add(a, b))
print("Subtraction:", calculator.subtract(a, b))
print("Multiplication:", calculator.multiply(a, b))
print("Division:", calculator.divide(a, b))