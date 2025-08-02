# lambda function
square: callable = lambda x: x * 2
print(f"square = {square(2)}")


# lambda with map
numbers: list = [1, 2, 3, 4, 5]
print("squared numbers : ", list(map(lambda x: x * 2, numbers)))


# lambda with sorting
info: list = [
    {
        "name": "Alice",
        "age": 20
    },
    {
        "name": "Bob",
        "age": 10
    },
    {
        "name": "Dan",
        "age": 30
    }
]
print("dict sort : ", sorted(info, key=lambda person: person["age"]))
print("dict sort : ", info)
print("\n")


# callback function
def callback(a: int, b: int):
    print("sum = ", a + b)


def functions(callback: callable) -> None:
    print("calling callback function here")
    callback(20, 30)

functions(callback)