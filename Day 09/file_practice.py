# Day 09 - File Handling Practice

# Write data to a file
with open("notes.txt", "w") as file:
    file.write("Hello, Python!\n")
    file.write("Today I am learning file handling.\n")
    file.write("Python is easy to learn.\n")

print("Data written successfully.")

# Read data from the file
with open("notes.txt", "r") as file:
    data = file.read()

print("\nFile contents:")
print(data)

# Append new data
with open("notes.txt", "a") as file:
    file.write("This is a new line added to the file.\n")

print("New data added successfully.")