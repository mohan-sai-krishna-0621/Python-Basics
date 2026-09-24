# Day 09 - Student Records

students = []

while True:
    print("\n--- Student Record System ---")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Search Student")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter student name: ")
        roll_no = input("Enter roll number: ")
        marks = float(input("Enter marks: "))

        student = {
            "name": name,
            "roll_no": roll_no,
            "marks": marks
        }

        students.append(student)

        print("Student added successfully.")

    elif choice == "2":
        if len(students) == 0:
            print("No student records found.")
        else:
            print("\nStudent Records:")

            for student in students:
                print("--------------------")
                print("Name:", student["name"])
                print("Roll No:", student["roll_no"])
                print("Marks:", student["marks"])

    elif choice == "3":
        roll_no = input("Enter roll number to search: ")

        found = False

        for student in students:
            if student["roll_no"] == roll_no:
                print("\nStudent Found!")
                print("Name:", student["name"])
                print("Roll No:", student["roll_no"])
                print("Marks:", student["marks"])

                found = True
                break

        if not found:
            print("Student not found.")

    elif choice == "4":
        print("Exiting program...")
        break

    else:
        print("Invalid choice. Please try again.")