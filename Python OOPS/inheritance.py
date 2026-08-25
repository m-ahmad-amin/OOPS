class Person:
    species = 'Human'

    def greet(self):
        print('Hello from Person')

class Student(Person):
    university = 'Standford'

s1 = Student()

print(s1.university)
print(s1.species)
s1.greet()