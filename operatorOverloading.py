# Operator Overloading built-in operator Re-Define kore User-Defined Data Types er jonno

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __str__(self):
        return str(self.x) + " " + str(self.y)

p1 = Point(10, 20)
p2 = Point(30, 40)

p3 = p1 + p2
print(p3)
print(p1)