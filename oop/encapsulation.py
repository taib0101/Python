
class Person:

    # This is the main concept of Encapsulation
    # where access modifier like private and protected are limited to instance 

    name: str # Public property or attribute
    __bank_account: str # Private property or attribute
    _age: int # Protected property or attribute

    # Constructor
    def __init__(self, name: str, bank_account: str, age: int) -> None:
        self.name = name
        self.__bank_account = bank_account
        self._age = age


    # Method
    def introduce(self) -> str:
        return f"Person name is {self.name}, bank account is {self.__bank_account}, age is {self._age}"
    

object1 = Person('Alice', '123sdfq324', 30)
print(object1.introduce())

print(Person('Bob', '43564dfg3', 40).introduce())