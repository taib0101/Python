# Convert int to float
a: int = 10
b: float = float(a)

print(f"b = {b: .2f}")


# Convert int to string
a: int = 123
number: str = str(a)
print(f"number = {number}")


# Convert string to int
# when convert string to int must be contains digit or single '.', if character contains, it raise error
number = "123"
print("converted string to int : ", int(number))