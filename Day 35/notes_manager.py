import json
import os

FILE_NAME = "notes.json"
notes = []


def load_notes():
    global notes

    if not os.path.exists(FILE_NAME):
        notes = []
        return

    try:
        with open(FILE_NAME, "r") as file:
            notes = json.load(file)

        if not isinstance(notes, list):
            notes = []
            print("Invalid notes format. Starting with an empty list.")

    except (json.JSONDecodeError, OSError):
        notes = []
        print("Could not load notes. Starting with an empty list.")


def save_notes():
    try:
        with open(FILE_NAME, "w") as file:
            json.dump(notes, file, indent=4)

        print("Notes saved successfully!")

    except OSError:
        print("Error: Could not save notes.")


def add_note():
    note = input("Enter your note: ").strip()

    if not note:
        print("Note cannot be empty!")
        return

    notes.append(note)
    save_notes()


def view_notes():
    if not notes:
        print("No notes available.")
        return

    print("\n===== YOUR NOTES =====")

    for number, note in enumerate(notes, start=1):
        print(f"{number}. {note}")


def delete_note():
    view_notes()

    if not notes:
        return

    try:
        number = int(input("Enter note number to delete: "))

        if 1 <= number <= len(notes):
            removed_note = notes.pop(number - 1)
            save_notes()
            print(f"Deleted note: {removed_note}")
        else:
            print("Invalid note number.")

    except ValueError:
        print("Please enter a valid number.")


def main():
    load_notes()

    while True:
        print("\n===== PERSONAL NOTES MANAGER =====")
        print("1. Add Note")
        print("2. View Notes")
        print("3. Delete Note")
        print("4. Exit")

        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            add_note()

        elif choice == "2":
            view_notes()

        elif choice == "3":
            delete_note()

        elif choice == "4":
            print("Notes Manager closed. Goodbye!")
            break

        else:
            print("Invalid choice. Please select 1-4.")


if __name__ == "__main__":
    main()