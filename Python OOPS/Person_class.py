class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person('Ahmad', 19)
p2 = Person('Ali', 20)
print(p1.name, p1.age, p2.name, p2.age)