
import json
import os

FILE_NAME = "students.json"


# Load student records from file
def load_students():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []


# Save student records to file
def save_students(students):
    with open(FILE_NAME, "w") as file:
        json.dump(students, file, indent=4)


# Add a student
def add_student(students):
    name = input("Enter student name: ")
    roll_no = input("Enter roll number: ")

    # Check for duplicate roll number
    for student in students:
        if student["roll_no"] == roll_no:
            print("Roll number already exists!")
            return

    marks = float(input("Enter marks: "))

    student = {
        "name": name,
        "roll_no": roll_no,
        "marks": marks
    }

    students.append(student)
    save_students(students)

    print("Student added successfully!")


# Display all students
def display_students(students):
    if not students:
        print("No student records found.")
        return

    print("\n--- Student Records ---")

    for student in students:
        print("Name:", student["name"])
        print("Roll Number:", student["roll_no"])
        print("Marks:", student["marks"])
        print("--------------------")


# Search for a student
def search_student(students):
    roll_no = input("Enter roll number to search: ")

    for student in students:
        if student["roll_no"] == roll_no:
            print("\nStudent Found!")
            print("Name:", student["name"])
            print("Roll Number:", student["roll_no"])
            print("Marks:", student["marks"])
            return

    print("Student not found.")


# Main program
students = load_students()

while True:
    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Search Student")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student(students)

    elif choice == "2":
        display_students(students)

    elif choice == "3":
        search_student(students)

    elif choice == "4":
        print("Thank you!")
        break

    else:
        print("Invalid choice. Try again.")