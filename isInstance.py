def detect_type(x):
    if isinstance(x, int):
        print("Integer")
    elif isinstance(x, float):
        print("Float")
    elif isinstance(x, str):
        print("String")
    elif callable(x):
        print("Function")
    elif isinstance(x, list):
        print("List")
    elif isinstance(x, dict):
        print("Dictionary (object-like)")
    else:
        print("Other type:", type(x))

# Try it
detect_type(42)
detect_type(lambda x: x)
detect_type({"a": 1})