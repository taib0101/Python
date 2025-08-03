# In Tradition programmig language, there have multiple function with same name for function over loading
# But In Python, there have no function overloading , there have default arguments as play role of overloading

class Person:

    # constructor
    def __init__(self, name: str = None) -> None:
        self.name: str = name

    def introduce(self) -> None:
        print(f"Person name is {self.name}")


object1: Person = Person()
object1.introduce()

object2: Person = Person('Alice')
object2.introduce()