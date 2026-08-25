class Person:
    species = 'Human'

    def greet(self):
        print('Hello from Person')
        print(self.name)

class Student(Person):
    university = 'Standford'
    def __init__(self, name):
        self.name = name
        super().greet()

s1 = Student('Ali')

# print(s1.university)
# print(s1.species)
s1.greet()