class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def print_avg(self):
        sum = 0
        for num in self.marks:
            sum += num
        print(sum / 3)

s1 = Student('Ali', [10, 12, 11])
s1.print_avg()