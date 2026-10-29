
def get_numbers():
    numbers = []

    for i in range(5):
        while True:
            try:
                number = int(input(f"Enter number {i + 1}: "))
                numbers.append(number)
                break
            except ValueError:
                print("Invalid input! Please enter an integer.")

    return numbers


def analyze_numbers(numbers):
    total = sum(numbers)
    average = total / len(numbers)
    largest = max(numbers)
    smallest = min(numbers)

    even_count = 0
    odd_count = 0

    for number in numbers:
        if number % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

    print("\n===== NUMBER ANALYZER RESULTS =====")
    print("Numbers:", numbers)
    print("Sum:", total)
    print("Average:", average)
    print("Largest number:", largest)
    print("Smallest number:", smallest)
    print("Even numbers:", even_count)
    print("Odd numbers:", odd_count)


def main():
    print("===== NUMBER ANALYZER =====")

    numbers = get_numbers()
    analyze_numbers(numbers)


if __name__ == "__main__":
    main()
