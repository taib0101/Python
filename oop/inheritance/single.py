
# Base Class
class Animal:
    color: str = "white"

    # Constructor
    def __init__(self, name: str) -> None:
        self.name = name

    def animal_details(self) -> None:
        print(f"Animal name is {self.name}")


# Derived Class
class Dog(Animal):

    def __init__(self, name: str) -> None:
        # super().__init__("Spike") # you can manully assign like this 
        super().__init__(name)

    def dog_details(self) -> None:
        print(f"Dog name is {self.name}")


object1: Dog = Dog("Spike")
object1.animal_details()
object1.dog_details()
print("Animal color is : ", object1.color, "\n")

object2: Animal = Animal("Droopy")
object2.animal_details()
print("Animal color is : ", object2.color)


print("object1 is it instance of Animal ? ", isinstance(object1, Animal))