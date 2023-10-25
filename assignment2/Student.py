class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def display_info(self):
        info = f"Name: {self.name}\nAge: {self.age}\nGrade: {self.grade}"
        return info


student1 = Student("Rajat", 23, "A++")


print("Student Information:")
print(student1.display_info())
