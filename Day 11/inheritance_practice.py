
# inheritance_practice.py

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_person(self):
        print("Name:", self.name)
        print("Age:", self.age)


class Student(Person):
    def __init__(self, name, age, roll_no, course):
        super().__init__(name, age)
        self.roll_no = roll_no
        self.course = course

    def display_student(self):
        self.display_person()
        print("Roll Number:", self.roll_no)
        print("Course:", self.course)


# Create an object
s1 = Student("Mohan", 20, 101, "CSE AI/ML")

s1.display_student()