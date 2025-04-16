
class Animal:
    def function(self):
        print("This is Animal")

class Dog(Animal):
    def function(self):
        print("This is Dog")

obj1 = Animal()
obj2 = Dog()

obj1.function()
obj2.function()