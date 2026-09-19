numbers = []

# Ask the user for 10 numbers
for i in range(10):
    number = int(input(f"Enter number {i + 1}: "))
    numbers.append(number)

# Display numbers
print("\nNumbers:", numbers)

# Total
total = sum(numbers)
print("Total:", total)

# Average
average = total / len(numbers)
print("Average:", average)

# Highest
print("Highest:", max(numbers))

# Lowest
print("Lowest:", min(numbers))

# Even and odd numbers
even_numbers = []
odd_numbers = []

for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number)
    else:
        odd_numbers.append(number)

print("Even numbers:", even_numbers)
print("Odd numbers:", odd_numbers)