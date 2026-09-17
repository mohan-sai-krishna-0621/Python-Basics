# Number Analyzer

number = int(input("Enter a number: "))

# Positive, negative or zero
if number > 0:
    print("The number is Positive")
elif number < 0:
    print("The number is Negative")
else:
    print("The number is Zero")

# Even or odd
if number % 2 == 0:
    print("The number is Even")
else:
    print("The number is Odd")

# Square
print("Square:", number ** 2)