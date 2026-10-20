
students = {}

def add_student():
    name = input("Enter student name: ").strip()

    if not name:
        print("Name cannot be empty!")
        return

    try:
        marks = float(input("Enter marks (0-100): "))

        if marks < 0 or marks > 100:
            print("Marks must be between 0 and 100!")
            return

        students[name] = marks
        print("Student added successfully!")

    except ValueError:
        print("Please enter valid numeric marks.")


def get_grade(marks):
    if marks >= 90:
        return "A+"
    elif marks >= 80:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 50:
        return "D"
    else:
        return "Fail"


def view_students():
    if not students:
        print("No student records available.")
        return

    print("\n--- STUDENT RESULTS ---")

    for name, marks in students.items():
        print(f"Name: {name}")
        print(f"Marks: {marks:.2f}")
        print(f"Grade: {get_grade(marks)}")
        print("-" * 25)


def show_summary():
    if not students:
        print("Add students first!")
        return

    marks_list = list(students.values())

    print("\n--- CLASS SUMMARY ---")
    print(f"Number of students: {len(students)}")
    print(f"Average marks: {sum(marks_list) / len(marks_list):.2f}")
    print(f"Highest marks: {max(marks_list):.2f}")
    print(f"Lowest marks: {min(marks_list):.2f}")


while True:
    print("\n===== STUDENT MARKS ANALYZER =====")
    print("1. Add student")
    print("2. View student results")
    print("3. Show class summary")
    print("4. Exit")

    choice = input("Enter your choice: ").strip()

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        show_summary()
    elif choice == "4":
        print("Program closed.")
        break
    else:
        print("Invalid choice. Choose 1-4.")
