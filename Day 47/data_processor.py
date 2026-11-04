
students = []


def get_marks():
    while True:
        try:
            marks = float(input("Enter marks (0-100): "))

            if 0 <= marks <= 100:
                return marks

            print("Marks must be between 0 and 100.")

        except ValueError:
            print("Invalid input! Enter a number.")


def add_student():
    print("\n===== ADD STUDENT =====")

    name = input("Enter student name: ").strip()

    if not name:
        print("Name cannot be empty!")
        return

    if any(s["name"].lower() == name.lower() for s in students):
        print("Student already exists!")
        return

    marks = get_marks()

    students.append({
        "name": name,
        "marks": marks
    })

    print("Student added successfully!")


def display_students():
    if not students:
        print("\nNo student records found.")
        return

    print("\n===== STUDENT RECORDS =====")

    for student in students:
        print(
            f"Name: {student['name']} | "
            f"Marks: {student['marks']:g}"
        )


def calculate_average():
    if not students:
        print("\nNo data available.")
        return

    total = sum(student["marks"] for student in students)
    average = total / len(students)

    print(f"\nClass Average: {average:.2f}")


def show_topper():
    if not students:
        print("\nNo data available.")
        return

    topper = max(students, key=lambda s: s["marks"])

    print("\n===== TOPPER =====")
    print(f"Name: {topper['name']}")
    print(f"Marks: {topper['marks']:g}")


def sort_students():
    if not students:
        print("\nNo data available.")
        return

    sorted_students = sorted(
        students,
        key=lambda s: s["marks"],
        reverse=True
    )

    print("\n===== RANKING =====")

    for rank, student in enumerate(sorted_students, start=1):
        print(
            f"{rank}. {student['name']} - "
            f"{student['marks']:g} marks"
        )


def show_passed_students():
    passed = [
        student for student in students
        if student["marks"] >= 40
    ]

    print("\n===== PASSED STUDENTS =====")

    if not passed:
        print("No students passed.")
        return

    for student in passed:
        print(f"{student['name']} - {student['marks']:g}")


def show_failed_students():
    failed = [
        student for student in students
        if student["marks"] < 40
    ]

    print("\n===== FAILED STUDENTS =====")

    if not failed:
        print("No students failed.")
        return

    for student in failed:
        print(f"{student['name']} - {student['marks']:g}")


def main():
    while True:
        print("\n===== DATA PROCESSING TOOL =====")
        print("1. Add Student")
        print("2. Display Students")
        print("3. Calculate Class Average")
        print("4. Show Topper")
        print("5. Sort Students by Marks")
        print("6. Show Passed Students")
        print("7. Show Failed Students")
        print("8. Exit")

        choice = input("Choose an option (1-8): ").strip()

        if choice == "1":
            add_student()

        elif choice == "2":
            display_students()

        elif choice == "3":
            calculate_average()

        elif choice == "4":
            show_topper()

        elif choice == "5":
            sort_students()

        elif choice == "6":
            show_passed_students()

        elif choice == "7":
            show_failed_students()

        elif choice == "8":
            print("Thank you for using Data Processing Tool!")
            break

        else:
            print("Invalid choice! Select from 1 to 8.")


if __name__ == "__main__":
    main()
