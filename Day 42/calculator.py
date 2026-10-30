
def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b


def floor_divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a // b


def modulus(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot use modulus with zero.")
    return a % b


def power(a, b):
    return a ** b


def get_number(message):
    while True:
        try:
            return float(input(message))
        except ValueError:
            print("Invalid input! Please enter a number.")


def main():
    operations = {
        "1": ("Addition", add),
        "2": ("Subtraction", subtract),
        "3": ("Multiplication", multiply),
        "4": ("Division", divide),
        "5": ("Floor Division", floor_divide),
        "6": ("Modulus", modulus),
        "7": ("Power", power),
    }

    while True:
        print("\n===== ROBUST CALCULATOR =====")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Floor Division (//)")
        print("6. Modulus (%)")
        print("7. Power (**)")
        print("8. Exit")

        choice = input("Choose an operation (1-8): ").strip()

        if choice == "8":
            print("Calculator closed. Goodbye!")
            break

        if choice not in operations:
            print("Invalid choice! Select a number from 1 to 8.")
            continue

        a = get_number("Enter the first number: ")
        b = get_number("Enter the second number: ")

        name, operation = operations[choice]

        try:
            result = operation(a, b)
            print(f"{name} result: {result:g}")

        except ZeroDivisionError as error:
            print("Error:", error)

        except OverflowError:
            print("Error: The result is too large.")


if __name__ == "__main__":
    main()
