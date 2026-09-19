

# Get 5 subject marks
for i in range(5):
    mark = int(input(f"Enter marks for subject {i + 1}: "))
    marks.append(mark)

# Display marks
print("All Marks:", marks)

# Calculate total
total = sum(marks)
print("Total:", total)

# Calculate average
average = total / len(marks)
print("Average:", average)

# Highest mark
print("Highest:", max(marks))

# Lowest mark
print("Lowest:", min(marks))