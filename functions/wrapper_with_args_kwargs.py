
def decorator(base_function: callable):
    def wrapper(*args, **kwargs):
        print("Wrape before calling base function")

        a, b = args
        print(f"args holds as like tuple. Example: a = {a}, b = {b}")

        base_function(*args, **kwargs)

        c = kwargs.get("c")
        d = kwargs.get("d")
        print(f"kwargs holds as like dictionary. Example: c = {c}, d = {d}")

        print("Wrape after calling base function")

    return wrapper


def main_base_function(a, b, c, d):
    print("Base function called")
    print(f"Bro are here a = {a}, b = {b}, c = {c}, d = {d}")


main_base_function = decorator(base_function=main_base_function)

main_base_function(1, 2, c=3, d=4)