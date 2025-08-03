# Function Overriding means , function was created on Base class and re-assign that function on Derived class

class Animal:

    def __init__(self, name: str) -> None:
        self.name: str = name

    def details(self) -> None:
        print("This is from Animal")


class Dog(Animal):

    def __init__(self, name: str) -> None:
        # super().__init__('Droopy')
        super().__init__(name)

    # Function overrided here
    def details(self) -> None:
        super().details() # this is optional
        print("This is from Dog")


object1 = Dog('Spike')
object1.details()