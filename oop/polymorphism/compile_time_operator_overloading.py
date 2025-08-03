# It refers overload the operator, for redefine user define data types

class Point:
    
    # Constructor
    def __init__(self, x: int, y: int) -> None:
        self.x: int = x
        self.y: int = y

    # Operator + Overload
    def __add__(self, other) -> 'Point':
        return Point(self.x + other.x, self.y + other.y)
    
    # for priniting the instanace for human readable
    def __str__(self) -> str:
        return f"x = {self.x}, y = {self.y}"


p1: Point = Point(3, 5)
print(p1)

p2: Point = Point(10, 15)
print(p2)

# operator overloading
p3: Point = p1 + p2
print(p3)

