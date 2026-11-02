
def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")

    return a / b


def factorial(number):
    if number < 0:
        raise ValueError("Factorial is not defined for negative integers.")

    if not isinstance(number, int):
        raise TypeError("Factorial requires an integer.")

    result = 1

    for value in range(1, number + 1):
        result *= value

    return result
