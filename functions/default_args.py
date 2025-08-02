# Basic Functions
def add(a: int, b: int) -> int:
    return a + b

print(f"sum = {add(20, 30)}")


# Default arguments
def power(base: int, exponent: int = 1) -> int:
    return base ** exponent

print("power : ", power(3))
print("power : ", power(3, 2))
