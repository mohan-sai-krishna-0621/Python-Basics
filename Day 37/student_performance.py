
import json
import os

FILE_NAME = "students.json"
students = []


def load_students():
    global students

    if not os.path.exists(FILE_NAME):
        students = []
        return

    try:
        with open(FILE_NAME, "r") as file:
            data = json.load(file)

        if isinstance(data, list):
            students = data
        else:
            students = []
            print("Invalid data format. Starting with an empty list.")

    except (json.JSONDecodeError, OSError):
        students = []
        print("Could not load student records.")


def save_students():
    try:
        with open(FILE_NAME, "w") as file:
            json.dump(students, file, indent=4)
    except OSError:
        print("Error saving student records.")


def add_student():
    name = input("Enter student name: ").strip()

    if not name:
        print("Name cannot be empty.")
        return

    try:
        marks = float(input("Enter marks (0-100): "))

        if not 0 <= marks <= 100:
            print("Marks must be between 0 and 100.")
            return

    except ValueError:
        print("Please enter valid numeric marks.")
        return

    student = {
        "name": name,
        "marks": marks
    }

    students.append(student)
    save_students()

    print("Student added successfully!")


def view_students():
    if not students:
        print("No student records available.")
        return

    print("\n===== STUDENT RECORDS =====")

    for number, student in enumerate(students, start=1):
        result = "PASS" if student["marks"] >= 40 else "FAIL"

        print(
            f"{number}. {student['name']} | "
            f"Marks: {student['marks']:.2f} | "
            f"Result: {result}"
        )


def search_student():
    name = input("Enter student name to search: ").strip().lower()

    found = False

    for student in students:
        if student["name"].lower() == name:
            result = "PASS" if student["marks"] >= 40 else "FAIL"

            print(f"Name: {student['name']}")
            print(f"Marks: {student['marks']:.2f}")
            print(f"Result: {result}")

            found = True

    if not found:
        print("Student not found.")


def show_statistics():
    if not students:
        print("No records available for analysis.")
        return

    total_marks = sum(student["marks"] for student in students)
    average = total_marks / len(students)

    passed = sum(
        1 for student in students
        if student["marks"] >= 40
    )

    failed = len(students) - passed

    topper = max(students, key=lambda student: student["marks"])

    print("\n===== PERFORMANCE STATISTICS =====")
    print(f"Total students: {len(students)}")
    print(f"Average marks: {average:.2f}")
    print(f"Passed students: {passed}")
    print(f"Failed students: {failed}")
    print(
        f"Highest scorer: {topper['name']} "
        f"({topper['marks']:.2f})"
    )


def main():
    load_students()

    while True:
        print("\n===== STUDENT PERFORMANCE SYSTEM =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Show Statistics")
        print("5. Exit")

        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            show_statistics()
        elif choice == "5":
            print("Student Performance System closed.")
            break
        else:
            print("Invalid choice. Select 1-5.")


if __name__ == "__main__":
    main()
