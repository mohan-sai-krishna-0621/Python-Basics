def analyze_numbers(numbers):
    total = sum(numbers)
    average = total / len(numbers)

    even_numbers = [n for n in numbers if n % 2 == 0]
    odd_numbers = [n for n in numbers if n % 2 != 0]

    print("\n--- Number Analysis ---")
    print("Numbers:", numbers)
    print("Total:", total)
    print("Average:", average)
    print("Largest:", max(numbers))
    print("Smallest:", min(numbers))
    print("Even numbers:", even_numbers)
    print("Odd numbers:", odd_numbers)


try:
    numbers = []

    count = int(input("How many numbers? "))

    if count <= 0:
        print("Enter a count greater than zero.")
    else:
        for i in range(count):
            number = int(input(f"Enter number {i + 1}: "))
            numbers.append(number)

        analyze_numbers(numbers)

except ValueError:
    print("Invalid input. Please enter integers only.")