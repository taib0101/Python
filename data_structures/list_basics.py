# list is mutable, means changeable, and reference type 
fruits: list = ["apple", "banana", "cherry", "mango", "grape"]

# find ranged value
print("find the rande value : ", fruits[0:3])


# reverse the list
print("reversed value : ", fruits[::-1])


# first two value
print("first two value : ", fruits[:2])


# search specific values index
print("index of banana : ", fruits.index("banana"))


# insert value at the last of fruits
fruits.append("dragon")
print("after append the fruits : ", fruits)


# insert value to a specific index
fruits.insert(3, "bro")
print("after insert to a specific index : ", fruits)


# removing last value from fruits
fruits.pop()
print("after removing last value : ", fruits)


# remove specific value
fruits.remove("bro")
print("after removing specififc value : ", fruits)


# checking membership of fruits
print("is banana exists ? ", "banana" in fruits)


# length of fruits
print("length of fruits list : ", len(fruits))


# modify the specific index
fruits[0] = "jack-fruit"
print("after modifying speific fruits : ", fruits)


# sort of a list
array: list = [7, 4, 5, 1, 8, 0]
print("sort : ", sorted(array))


# sort of dictionary list
array: list = [
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
print("sort list of dictionary : ", sorted(array, key=lambda person: person['age'])) # to see more description goto functions/lambda_callback_functions


# copy a fruit list wihtout reference
fruits1 = fruits.copy()


print([100] is [100])
print([100] == [100])