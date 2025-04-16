# Allows ReUse, Enables Polymorphism, contain essential details
# Abstract contain constructor, property, method and details
# Instance can't make of Abstract class directly

from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def __init__(self, name):
        # super().__init__()
        self.name = name

    @abstractmethod
    def details(self):
        pass 

class Type(Animal):
    def __init__(self, name):
        super().__init__(name)
    
    def details(self):
        print("this is abstraction")

obj = Type("Dog")
    
