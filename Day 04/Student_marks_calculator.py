
def calculate_total(maths, python, english):
    return maths + python + english


def calculate_percentage(total):
    return total / 3


def calculate_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    else:
        return "F"


# Get marks from the user
maths = float(input("Enter Maths marks: "))
python = float(input("Enter Python marks: "))
english = float(input("Enter English marks: "))

# Calculate results using functions
total = calculate_total(maths, python, english)
percentage = calculate_percentage(total)
grade = calculate_grade(percentage)

# Display result
print("\n--- Student Result ---")
print("Total      :", total)
print("Percentage :", percentage)
print("Grade      :", grade)

