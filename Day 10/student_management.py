class Student:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

    def display(self):
        print("Name:", self.name)
        print("Roll No:", self.roll_no)
        print("Marks:", self.marks)
        print("----------------")


students = []

student1 = Student("Rahul", 101, 85)
student2 = Student("Anil", 102, 90)
student3 = Student("Kiran", 103, 78)

students.append(student1)
students.append(student2)
students.append(student3)

for student in students:
    student.display()