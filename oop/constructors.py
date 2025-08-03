
class Person:

    # Constructor with __int__
    # Constructor doesn't return
    def __init__(self, name: str = None) -> None:
        self.name: str = name

    # Method
    def introduce(self) -> None:
        print(f"person name is {self.name}")


object1: Person = Person()
object2: Person = Person('Alice')


object1.introduce()
object2.introduce()


Person('Bob').introduce()