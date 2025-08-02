
person: dict = {
    "name": "Alice",
    "age": 30
}


# Accessing value by key
print("name : ", person["name"])
print("name : ", person.get("name"))


# Adding a key-value pair
person["email"] = "cut_the@bullshit.com"
print("after adding value : ", person["email"])


# remove attribute or key-value
person.pop("email")
# or you can delete by that 'del person["email"]'
print("after removing key-value : ", person)


# updating specific value
person["age"] = 31
print("after updating specific value : ", person["age"])


# key, value, items
print("keys : ", person.keys())
print("values : ", person.values())
print("items : ", person.items())


print(
    {
        "name": "Alice",
        "age": 30
    } is {
        "name": "Alice",
        "age": 30
    }
)
print(
    {
        "name": "Alice",
        "age": 30
    } == {
        "name": "Alice",
        "age": 30
    }
)