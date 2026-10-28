from collections import namedtuple

Student = namedtuple(“Student”, [“name”, “age”, “course”])

student = Student(“Vikram”, 19, “CSE AI-ML”)

student_dict = student._asdict()

print(“Student Record:”)
print(student_dict)
