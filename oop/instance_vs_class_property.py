
class Person:
    country: str = 'Bangladesh'

    # Constructor
    def __init__(self, name: str, age: int) -> None:
        self.name: str = name 
        self.age: int = age


persion1: Person = Person('Alice', 30)
persion2: Person = Person('Bob', 25)

print(f"persons1 : {persion1.name}, {persion1.country}, {persion1.age}")
print(f"persons2 : {persion2.name}, {persion2.country}, {persion2.age}")


# Change class property using class name for globally
Person.country = 'Pakistan'


# after changing class property
print("\nafter changing class property")
print(f"persons1 : {persion1.name}, {persion1.country}, {persion1.age}")
print(f"persons2 : {persion2.name}, {persion2.country}, {persion2.age}")


persion1.age = 40


# after changing instance property
print("\nafter changing instance property")
print(f"persons1 : {persion1.name}, {persion1.country}, {persion1.age}")
print(f"persons2 : {persion2.name}, {persion2.country}, {persion2.age}")
