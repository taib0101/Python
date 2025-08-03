class MathOperation:
    
    @staticmethod
    def add(x: int, y: int) -> int:
        return x + y
    

# Call static method directly from class
print("Sum = ", MathOperation.add(10, 20))

# you can also create instance
object1: MathOperation = MathOperation()
print("Sum = ", object1.add(40, 20))