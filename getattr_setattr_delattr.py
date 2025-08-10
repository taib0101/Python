
class Person:
    name: str = 'Alice'
    age: int = 30
    country: str = 'Mexico'

person: Person = Person()

# getattr is only work for class object not for dict
print("attribute of person dictionary : ", getattr(person, 'name'))