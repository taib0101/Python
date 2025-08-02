
# *args collects all positional arguments
def sum_all(*args) -> int:
    sum = 0
    for value in args:
        sum += value

    return sum

print(f"sum = {sum_all(1, 2, 3, 4, 5)}")


# **kwargs collect all keyword arguments
def display_info(**kwargs) -> None:
    print("Display info is : ", kwargs)

display_info(name="Alice", age=30, country="Shit")


# combining all positional and keyword arguments
def combined_all1(*args, **kwargs) -> None:
    print(f"args = {args}, kwargs = {kwargs}")

combined_all1(1, 2, 3, name="Alice", age=30)


def combined_all2(a, b, c, **kwargs) -> None:
    print(f"a = {a}, b = {b}, kwargs = {kwargs}")

combined_all2(1, 2, 3, name="Alice", age=30)
