
x: int = 10 # global variable

def global_variables() -> None:
    global x # global variable
    for i in range(3):
        x += 1

global_variables()
print(f"x : {x}")


def local_variables() -> None:
    y = 10 # local variable
    print(f"local variable is : {locals()}")

local_variables()

# you can not print local variable to global