import os

FILE_NAME = "passwords.txt"


def load_passwords():
    passwords = {}

    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            for line in file:
                line = line.strip()

                if line:
                    website, username, password = line.split("|")

                    passwords[website] = {
                        "username": username,
                        "password": password
                    }

    return passwords


def save_passwords(passwords):
    with open(FILE_NAME, "w") as file:
        for website, details in passwords.items():
            file.write(
                f"{website}|{details['username']}|{details['password']}\n"
            )

    print("Passwords saved successfully!")


def add_password(passwords):
    website = input("Enter website: ")
    username = input("Enter username: ")
    password = input("Enter password: ")

    passwords[website] = {
        "username": username,
        "password": password
    }

    save_passwords(passwords)
    print("Password added successfully!")


def view_passwords(passwords):
    if not passwords:
        print("No passwords saved.")
        return

    for website, details in passwords.items():
        print("\nWebsite:", website)
        print("Username:", details["username"])
        print("Password:", details["password"])


def delete_password(passwords):
    website = input("Enter website to delete: ")

    if website in passwords:
        del passwords[website]
        save_passwords(passwords)
        print("Password deleted successfully!")
    else:
        print("Website not found.")


def main():
    passwords = load_passwords()

    while True:
        print("\n===== PASSWORD MANAGER =====")
        print("1. Add Password")
        print("2. View Passwords")
        print("3. Delete Password")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_password(passwords)

        elif choice == "2":
            view_passwords(passwords)

        elif choice == "3":
            delete_password(passwords)

        elif choice == "4":
            print("Exiting Password Manager...")
            break

        else:
            print("Invalid choice. Try again.")


main()