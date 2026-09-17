name = input("Enter student name: ")
age = int(input("Enter age: "))
marks = float(input("Enter marks: "))

if age >= 18 and marks >= 60:
    print("\n", name, "is eligible.")
else:
    print("\n", name, "is not eligible.")