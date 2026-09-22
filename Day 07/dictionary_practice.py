# Dictionary Practice

# Create a dictionary
student = {
    "name": "Rahul",
    "age": 20,
    "course": "CSE",
    "year": 3
}

# Display dictionary
print("Student Details:")
print(student)

# Access values
print("\nName:", student["name"])
print("Age:", student["age"])
print("Course:", student["course"])

# Add a new item
student["college"] = "ABC Engineering College"

print("\nAfter adding college:")
print(student)

# Update a value
student["age"] = 21

print("\nAfter updating age:")
print(student)

# Delete an item
del student["year"]

print("\nAfter deleting year:")
print(student)

# Display keys
print("\nKeys:")
print(student.keys())

# Display values
print("\nValues:")
print(student.values())

# Display items
print("\nItems:")
print(student.items())