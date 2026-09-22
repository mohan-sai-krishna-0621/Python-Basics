# Student Information Program

student = {}

# Get student details
student["name"] = input("Enter student name: ")
student["roll_no"] = input("Enter roll number: ")
student["course"] = input("Enter course: ")
student["college"] = input("Enter college name: ")

# Get marks
student["python_marks"] = int(input("Enter Python marks: "))
student["maths_marks"] = int(input("Enter Maths marks: "))
student["c_marks"] = int(input("Enter C marks: "))

# Calculate total and average
total = (
    student["python_marks"]
    + student["maths_marks"]
    + student["c_marks"]
)

average = total / 3

# Display information
print("\n----- STUDENT INFORMATION -----")
print("Name:", student["name"])
print("Roll No:", student["roll_no"])
print("Course:", student["course"])
print("College:", student["college"])

print("\n----- MARKS -----")
print("Python:", student["python_marks"])
print("Maths:", student["maths_marks"])
print("C:", student["c_marks"])

print("\nTotal Marks:", total)
print("Average Marks:", average)

# Result
if average >= 40:
    print("Result: PASS")
else:
    print("Result: FAIL")