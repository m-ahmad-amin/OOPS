class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print('Name:', self.name)
        print('Age:', self.age)

class Student(Person):
    def __init__(self, name, age, university):
            self.name = name
            self.age = age
            # super().__init__(name, age) # can be used instead of upper two lines (even better)
            self.university = university

    def introduce(self):
        super().introduce()
        print('University:', self.university)

class Teacher(Person):
    def __init__(self, name, age, subject):
        self.name = name
        self.age = age
        # super().__init__(name, age) # can be used instead of upper two lines (even better)
        self.subject = subject

    def introduce(self):
        super().introduce()
        print('Subject:', self.subject)

student = Student("Ahmad", 19, "GIKI")
teacher = Teacher("Ali", 35, "Computer Science")

student.introduce()
teacher.introduce()