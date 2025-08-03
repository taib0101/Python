
class Keyboard:

    # Private Property or attribute
    _keyboard_name: str

    # Constructor
    def __init__(self, keyboard_name: str) -> None:
        self._keyboard_name = keyboard_name

    def keyboard_details(self) -> None:
        print(f"Keyboard name is {self._keyboard_name}")



class Mouse:

    # Constructor
    def __init__(self, mouse_name: str) -> None:
        self.mouse_name = mouse_name

    def mouse_details(self) -> None:
        print(f"Mouse name is {self.mouse_name}")


# In Java, derived class can't inherit from multiple base class. that's way java use interface
# In Java, derived class can't inherit private property 
class Computer(Keyboard, Mouse):

    # Constructor
    def __init__(self, keyboard_name: str, mouse_name: str):
        Keyboard.__init__(self, keyboard_name)
        Mouse.__init__(self, mouse_name)

    def computer_details(self) -> None:
        print("\nComputer details")
        self.keyboard_details() # super().keyboard_details() this is use better for use function override as polymorphism
        super().mouse_details() # self.mouse_details()


object1: Computer = Computer('Dell', 'Hp')
object1.keyboard_details()
object1.mouse_details()
object1.computer_details()


print("object1 is it instance of Keyboard ? ", isinstance(object1, Keyboard))
print("object1 is it instance of Mouse ? ", isinstance(object1, Mouse))
print("object1 is it instance of Computer ? ", isinstance(object1, Computer))
