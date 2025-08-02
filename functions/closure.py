# Closure Fucntion
def outer() -> callable:
    print("this is from outer")

    def inner() -> None:
        print("this is from inner")

    return inner

variable = outer()

variable()