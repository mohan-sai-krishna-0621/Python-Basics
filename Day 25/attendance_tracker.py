
import os

FILE_NAME = "attendance.txt"
students = {}


def load_attendance():
    if not os.path.exists(FILE_NAME):
        return

    try:
        with open(FILE_NAME, "r") as file:
            for line in file:
                line = line.strip()

                if not line:
                    continue

                try:
                    roll_no, name, present, total = line.split(",", 3)

                    students[roll_no] = {
                        "name": name,
                        "present": int(present),
                        "total": int(total)
                    }
                except ValueError:
                    print("Skipping invalid record:", line)

        print("Attendance records loaded successfully!")

    except OSError:
        print("Error reading attendance file.")


def save_attendance():
    try:
        with open(FILE_NAME, "w") as file:
            for roll_no, details in students.items():
                file.write(
                    f"{roll_no},{details['name']},"
                    f"{details['present']},{details['total']}\n"
                )

        print("Attendance saved successfully!")

    except OSError:
        print("Error saving attendance file.")


def add_student():
    roll_no = input("Enter roll number: ").strip()

    if not roll_no:
        print("Roll number cannot be empty!")
        return

    if roll_no in students:
        print("Student already exists!")
        return

    name = input("Enter student name: ").strip()

    if not name:
        print("Student name cannot be empty!")
        return

    if "," in name or "," in roll_no:
        print("Names and roll numbers cannot contain commas!")
        return

    students[roll_no] = {
        "name": name,
        "present": 0,
        "total": 0
    }

    save_attendance()
    print("Student added successfully!")


def mark_attendance():
    roll_no = input("Enter roll number: ").strip()

    if roll_no not in students:
        print("Student not found!")
        return

    status = input("Present or Absent (P/A): ").strip().upper()

    if status not in ("P", "A"):
        print("Invalid choice! Enter P or A.")
        return

    students[roll_no]["total"] += 1

    if status == "P":
        students[roll_no]["present"] += 1
        print("Marked Present!")
    else:
        print("Marked Absent!")

    save_attendance()


def view_attendance():
    if not students:
        print("No student records available.")
        return

    print("\n========== ATTENDANCE RECORDS ==========")

    for roll_no, details in students.items():
        total = details["total"]
        present = details["present"]

        if total > 0:
            percentage = (present / total) * 100
        else:
            percentage = 0

        print("\nRoll Number:", roll_no)
        print("Name:", details["name"])
        print("Classes Present:", present)
        print("Total Classes:", total)
        print(f"Attendance Percentage: {percentage:.2f}%")
        print("-" * 35)


def search_student():
    roll_no = input("Enter roll number to search: ").strip()

    if roll_no not in students:
        print("Student not found!")
        return

    details = students[roll_no]
    total = details["total"]
    present = details["present"]

    percentage = (present / total * 100) if total > 0 else 0

    print("\nStudent Details")
    print("Roll Number:", roll_no)
    print("Name:", details["name"])
    print("Classes Present:", present)
    print("Total Classes:", total)
    print(f"Attendance Percentage: {percentage:.2f}%")


def main():
    load_attendance()

    while True:
        print("\n===== ATTENDANCE TRACKER =====")
        print("1. Add Student")
        print("2. Mark Attendance")
        print("3. View All Attendance")
        print("4. Search Student")
        print("5. Save Attendance")
        print("6. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_student()

        elif choice == "2":
            mark_attendance()

        elif choice == "3":
            view_attendance()

        elif choice == "4":
            search_student()

        elif choice == "5":
            save_attendance()

        elif choice == "6":
            save_attendance()
            print("Thank you for using Attendance Tracker!")
            break

        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()
