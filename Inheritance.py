# Base Class
class Animal:
    def __init__(self, animal):
        self.className = animal
    
# Derived Class
class Name(Animal):
    def __init__(self, animal, name):
        super().__init__(animal)
        self.name = name

obj = Name("Animal", "Dog")
print(obj.name)
print(obj.className)
