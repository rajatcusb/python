class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def greet(self):
        return f"Hello, I'm {self.name}."

    def introduce(self):
        return f"My name is {self.name}. I am {self.age} years old, and I am {self.gender}."

class Student(Person):
    def __init__(self, name, age, gender, course):
        super().__init__(name, age, gender)
        self.course = course

    def introduce(self):
        return super().introduce() + f" I am a student studying {self.course}."

class Teacher(Person):
    def __init__(self, name, age, gender, subject):
        super().__init__(name, age, gender)
        self.subject = subject

    def introduce(self):
        return super().introduce() + f" I am a teacher, and I teach {self.subject}."

# Create a Person, Student, and Teacher objects
person = Person("Asmita", 30, "female")
student = Student("Ram", 20, "male", "Computer Science")
teacher = Teacher("Rahul", 40, "male", "Math")

# Greet and introduce each person
print(person.greet())
print(person.introduce())

print("\n" + student.greet())
print(student.introduce())

print("\n" + teacher.greet())
print(teacher.introduce())
