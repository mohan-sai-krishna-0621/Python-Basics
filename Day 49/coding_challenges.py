
# DAY 49 - PYTHON CODING CHALLENGES


# 1. Find the largest number
def largest_number(numbers):
    return max(numbers)


# 2. Count even and odd numbers
def count_even_odd(numbers):
    even = 0
    odd = 0

    for number in numbers:
        if number % 2 == 0:
            even += 1
        else:
            odd += 1

    return even, odd


# 3. Reverse a string
def reverse_string(text):
    return text[::-1]


# 4. Check palindrome
def is_palindrome(text):
    text = text.lower().replace(" ", "")
    return text == text[::-1]


# 5. Count word frequency
def word_frequency(sentence):
    words = sentence.lower().split()
    frequency = {}

    for word in words:
        frequency[word] = frequency.get(word, 0) + 1

    return frequency


# 6. Remove duplicates
def remove_duplicates(numbers):
    return list(dict.fromkeys(numbers))


# 7. Find second-largest distinct number
def second_largest(numbers):
    unique_numbers = sorted(set(numbers), reverse=True)

    if len(unique_numbers) < 2:
        return None

    return unique_numbers[1]


# 8. Calculate factorial
def factorial(number):
    if number < 0:
        return None

    result = 1

    for i in range(1, number + 1):
        result *= i

    return result


# 9. Sort students by marks
def sort_students(students):
    return sorted(
        students,
        key=lambda student: student["marks"],
        reverse=True
    )


# 10. Find common elements
def common_elements(list1, list2):
    return list(set(list1) & set(list2))


# MAIN PROGRAM
def main():
    numbers = [10, 20, 5, 30, 15, 20]

    print("===== DAY 49 CODING CHALLENGES =====")

    print("\n1. Largest number:", largest_number(numbers))

    even, odd = count_even_odd(numbers)
    print("2. Even numbers:", even)
    print("   Odd numbers:", odd)

    print("3. Reverse string:", reverse_string("Python"))

    print("4. Is palindrome:", is_palindrome("madam"))

    print(
        "5. Word frequency:",
        word_frequency("python is easy python is powerful")
    )

    print("6. Remove duplicates:", remove_duplicates(numbers))

    print("7. Second largest:", second_largest(numbers))

    print("8. Factorial of 5:", factorial(5))

    students = [
        {"name": "Rahul", "marks": 85},
        {"name": "Priya", "marks": 92},
        {"name": "Amit", "marks": 75}
    ]

    print("9. Student ranking:", sort_students(students))

    print(
        "10. Common elements:",
        common_elements([1, 2, 3, 4], [3, 4, 5, 6])
    )


if __name__ == "__main__":
    main()
