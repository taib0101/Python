
class Person:

    # constructor
    def __init__(self, name: str) -> None:
        self.name = name
        print(f"Object person {self.name} created")

    # destructor
    def __del__(self) -> None:
        print(f"Object person {self.name} deleted")


object1 = Person('Alice')
del object1