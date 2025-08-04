from abc import ABC, abstractmethod

# abstraction hides implementation details
# you can't create instance directly from abstraction
class Animal(ABC):

    # you can use constructor as abstract method
    @abstractmethod
    def __init__(self, name: str) -> None:
        self.name = name

    # hide implemention details
    @abstractmethod
    def make_sound(self) -> None:
        print(f"{self.name} make sound")

# Inheritance
class Dog(Animal):

    def __init__(self, name: str) -> None:
        # super().__init__("Droopy")
        super().__init__(name)
        

    # This is function override, part of polymorphison
    def make_sound(self) -> None:
        super().make_sound() # called parent class's method by super()
        print("Dog here")


object1: Dog = Dog('Spike')
object1.make_sound()

print("object1 is it instance of Animal ? ", isinstance(object1, Animal))
