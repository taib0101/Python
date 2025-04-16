class Constructor:
    def __init__(self):
        self.public_var = "I am Public"
        self._protected_var = "I am Protected"
        self.__private_var = "I am Private"
    
    def display(self):
        print(self._protected_var)
        print(self.__private_var)
    
obj = Constructor()
print(obj.public_var)
obj.display()
