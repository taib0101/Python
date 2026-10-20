
def decorator(base_function: callable):
    def wrapper():
        print("Wrape before calling base function")

        base_function()

        print("Wrape after calling base function")

    return wrapper

# main_base_function = decorator(base_function=main_base_function)
@decorator
def main_base_function():
    print("Base function called")


main_base_function()