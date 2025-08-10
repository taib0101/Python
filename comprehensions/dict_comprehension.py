person: dict = {
    'name': 'Alice',
    'age': 30,
    'country': 'Mexico'
}

# dict comprehension
dictionary: dict = {key: value for key, value in person.items()}
print(f"dictionary of person : {dictionary}")

# dict comprehension with conditions
country: dict = {key: value for key, value in person.items() if key == 'country'}
print(f"dictionary of country : {country}")