student1_subjects = {
    "Python",
    "AI",
    "Database",
    "Web Development"
}

student2_subjects = {
    "Python",
    "Machine Learning",
    "Database",
    "C++"
}

print("Student 1 subjects:", student1_subjects)
print("Student 2 subjects:", student2_subjects)

# Common subjects
common_subjects = student1_subjects.intersection(student2_subjects)
print("\nCommon subjects:", common_subjects)

# All subjects
all_subjects = student1_subjects.union(student2_subjects)
print("All subjects:", all_subjects)

# Subjects only in Student 1
only_student1 = student1_subjects.difference(student2_subjects)
print("Only Student 1:", only_student1)

# Subjects only in Student 2
only_student2 = student2_subjects.difference(student1_subjects)
print("Only Student 2:", only_student2)