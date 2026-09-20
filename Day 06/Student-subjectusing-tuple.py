student_name = input("Enter student name: ")

subjects = (
    "Python",
    "Data Structures",
    "Database",
    "AI",
    "Web Development"
)

print("\nStudent Name:", student_name)
print("Subjects:")

for subject in subjects:
    print("-", subject)

print("\nTotal subjects:", len(subjects))

print("First subject:", subjects[0])
print("Last subject:", subjects[-1])