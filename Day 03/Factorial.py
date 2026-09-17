# Factorial Challenge

number = int(input("Enter a number: "))

factorial = 1

if number < 0:
    print("Factorial is not possible for negative numbers")
else:
    for i in range(1, number + 1):
        factorial = factorial * i

    print("Factorial of", number, "is:", factorial)