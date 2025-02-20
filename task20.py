# Read marks of three subjects and determine if the student has passed or failed using classes and objects

class Student:
    def __init__(self, marks1, marks2, marks3):
        self.marks1 = marks1
        self.marks2 = marks2
        self.marks3 = marks3

    def is_passed(self):
        if self.marks1 >= 40 and self.marks2 >= 40 and self.marks3 >= 40:
            return True
        else:
            return False

# Read marks of three subjects from the user
marks1 = int(input("Enter marks for subject 1: "))
marks2 = int(input("Enter marks for subject 2: "))
marks3 = int(input("Enter marks for subject 3: "))

# Create an object of the Student class
student = Student(marks1, marks2, marks3)

# Determine if the student has passed or failed
if student.is_passed():
    print("The student has passed.")
else:
    print("The student has failed.")
