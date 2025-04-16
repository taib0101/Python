obj = {
    'name': 'Taib',
    'age': 30,
    'gender': 'Male'
}

for key in obj:
    print(key, ": ", obj[key])

for key in obj.keys():
    print(key)

for value in obj.values():
    print(value)

for key, value in obj.items():
    print(f"{key}: {value}")