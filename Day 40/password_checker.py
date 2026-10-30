import string


def check_password(password):
    feedback = []
    score = 0

    # Check length
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Use at least 8 characters.")

    # Check uppercase letters
    if any(char.isupper() for char in password):
        score += 1
    else:
        feedback.append("Add an uppercase letter.")

    # Check lowercase letters
    if any(char.islower() for char in password):
        score += 1
    else:
        feedback.append("Add a lowercase letter.")

    # Check digits
    if any(char.isdigit() for char in password):
        score += 1
    else:
        feedback.append("Add a number.")

    # Check special characters
    if any(char in string.punctuation for char in password):
        score += 1
    else:
        feedback.append("Add a special character.")

    # Determine rating
    if score <= 2:
        strength = "Weak"
    elif score <= 4:
        strength = "Moderate"
    else:
        strength = "Strong"

    return strength, feedback


def main():
    print("===== PASSWORD STRENGTH CHECKER =====")
    print("Your password is checked locally and is not saved.")

    password = input("Enter a test password: ")

    if not password:
        print("Password cannot be empty.")
        return

    strength, feedback = check_password(password)

    print("\n===== RESULTS =====")
    print("Strength rating:", strength)

    if feedback:
        print("\nSuggestions:")
        for suggestion in feedback:
            print("-", suggestion)
    else:
        print("All five basic requirements are satisfied!")


if __name__ == "__main__":
    main()
