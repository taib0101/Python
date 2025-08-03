
class Person:

    def __init__(self, name: str) -> None:
        self.name = name

    def __str__(self) -> str:
        return f"Person name is {self.name}"
    
    def __repr__(self) -> str:
        return f"Person is error"
    

print("Representation of with __str__ as string : ", Person('Alice'))
print("Representation of with __repr__ as string : ", repr(Person('Alice')))
