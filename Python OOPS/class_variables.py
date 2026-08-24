class Person:
    # Class variable: stored on the class object (Person).
    # All instances can read it unless they have their own 'speices'.
    speices = 'Human'

    def __init__(self, name, age):
        # Instance variables: stored separately inside each Person object.
        self.name = name
        self.age = age


# Accessing the class variable directly through the class object.
print(Person.speices)  # Human


p1 = Person('A', 10)

# p1 doesn't have its own 'speices', so Python looks in the class (Person).
print(p1.speices)  # Human


# Assignment through the instance creates an instance variable on p1.
# It does NOT change Person.speices.
p1.speices = 'Homo sepians'

print(p1.speices)     # Homo sepians: found in p1
print(Person.speices) # Human: still unchanged


# A new Person object is created here.
# This new object doesn't have its own 'speices',
# so Python looks in Person and finds the class variable.
print(Person('A', 10).speices)  # Human