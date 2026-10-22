
def parameter_decorator(parameter):
    print("parameter = ", parameter)

    def decorator(base_function: callable):
        
        def wrapper(*args, **kwargs):
            args = ("Bro 1", "Bro 2")
            kwargs['c'] = "Bro 3"
            kwargs['d'] = "Bro 4"
            print("Wrape before calling base function")
            base_function(*args, **kwargs)
            print("Wrape after calling base function")

        return wrapper

    return decorator

@parameter_decorator("bro")
def main_base_function(a, b, c, d):
    print("Base function called")
    print(f"Bro are here a = {a}, b = {b}, c = {c}, d = {d}")

main_base_function(1, 2, c=3, d=4)