# Convert list to dict
# Method 01
keys: list = ['name', 'age']
values: list = ['Alice', 30]
print("converted list to dict by keys and values : ", dict(zip(keys, values)))


# Method 02
pairs: list = [('name', 'Alice'), ('age', 30)]
print("converted list to dict by pair of tuple : ", dict(pairs))


# Convert dict to list
person: dict = {
    'name': 'Alice',
    'age': 30
}
print("convert dict to list : ", list(person.items()))