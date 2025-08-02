# set automatically removes duplicates
fruits: set = {"apple", "mango", "grape", "banana", "pine-apple", "apple"}
print("distinct values : ", fruits)


# Adding single value
fruits.add("jack-fruit")
print("after adding fruits : ", fruits)


# Adding more data
fruits.update(["dragon", "olive"])
print("after adding more data fruits : ", fruits)


# remove data from fruits
fruits.remove("apple") # it might raise key-error if 'apple' doesn't exist
print("after remove apple from fruits : ", fruits)


# remove data from fruits
fruits.discard("apple") # it doesn't raise key-error if 'apple' doesn't exist
print("after remove apple from fruits : ", fruits)


# check membership
print("is mang exists : ", "banana" in fruits)


# length of fruits
print("length of fruits : ", len(fruits))


print({1, 2} is {1, 2})
print({1, 2} == {1, 2})