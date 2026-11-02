import math_utils
import text_utils


def main():
    while True:
        print("\n===== PYTHON UTILITY TOOLKIT =====")
        print("1. Add two numbers")
        print("2. Calculate factorial")
        print("3. Count words")
        print("4. Reverse text")
        print("5. Count vowels")
        print("6. Convert text to title case")
        print("7. Exit")

        choice = input("Choose an option (1-7): ").strip()

        try:
            if choice == "1":
                a = float(input("Enter first number: "))
                b = float(input("Enter second number: "))
                print("Result:", math_utils.add(a, b))

            elif choice == "2":
                number = int(input("Enter a non-negative integer: "))
                print("Factorial:", math_utils.factorial(number))

            elif choice == "3":
                text = input("Enter text: ")
                print("Word count:", text_utils.count_words(text))

            elif choice == "4":
                text = input("Enter text: ")
                print("Reversed text:", text_utils.reverse_text(text))

            elif choice == "5":
                text = input("Enter text: ")
                print("Vowel count:", text_utils.count_vowels(text))

            elif choice == "6":
                text = input("Enter text: ")
                print("Title case:", text_utils.make_title(text))

            elif choice == "7":
                print("Utility Toolkit closed.")
                break

            else:
                print("Invalid choice. Select 1-7.")

        except ValueError as error:
            print("Input error:", error)

        except OverflowError:
            print("The calculation result is too large.")

        except TypeError as error:
            print("Type error:", error)


if __name__ == "__main__":
    main()
