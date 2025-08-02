
person: dict = {"name": "Alice", "age": 30}

key1, key2 = person
print(f"key1 = {key1}, key2 = {key2}")


value1, value2 = person.values()
print(f"value1 = {value1}, value2 = {value2}")


# dict unpack thorugh functions
def display_info(name: str, age: int) -> None:
    print(f"name = {name}, age = {age}")

# **person means dict makes it keyword arguments
display_info(**person)