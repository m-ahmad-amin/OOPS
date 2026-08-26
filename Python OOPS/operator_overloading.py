class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def cooridnate(self):
        return (self.x, self.y)

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

p1 = Point(1, 2)
print(p1.cooridnate())
p2 = Point(3, 7)
print(p2.cooridnate())
print((p1 + p2).cooridnate())
print((p1 - p2).cooridnate())