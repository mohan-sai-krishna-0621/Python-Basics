# Student Management Program

print("===== STUDENT MANAGEMENT SYSTEM =====")

name = input("Enter student name: ")
roll_no = input("Enter roll number: ")

maths = float(input("Enter Maths marks: "))
python = float(input("Enter Python marks: "))
english = float(input("Enter English marks: "))

total = maths + python + english
percentage = total / 3

print("\n===== STUDENT DETAILS =====")
print("Name:", name)
print("Roll Number:", roll_no)
print("Maths:", maths)
print("Python:", python)
print("English:", english)
print("Total Marks:", total)
print("Percentage:", percentage)

if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 50:
    grade = "D"
else:
    grade = "Fail"

print("Grade:", grade)      