
import json

# Student information using a dictionary
student = {
    "name": "Mohan",
    "roll_no": 101,
    "marks": 85.5,
    "course": "CSE AI/ML"
}

# Convert dictionary into JSON string
json_data = json.dumps(student, indent=4)

print("JSON Data:")
print(json_data)

# Save JSON data into a file
with open("student.json", "w") as file:
    json.dump(student, file, indent=4)

print("Data saved successfully!")

# Read JSON data from the file
with open("student.json", "r") as file:
    data = json.load(file)

print("\nStudent Details:")
print("Name:", data["name"])
print("Roll Number:", data["roll_no"])
print("Marks:", data["marks"])
print("Course:", data["course"])