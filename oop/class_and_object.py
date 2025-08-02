
# Create Class with Pascal Case
class Person:

    # Property or Attribute
    name: str = None

    # Method
    def introduce(self) -> None:
        print(f"person name is {self.name}")


# Create instance
object1: Person = Person()
object2: Person = Person()


# Set manually Attribute
object2.name = "Alice"


object1.introduce()
object2.introduce()
