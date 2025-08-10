fruits: list = ['banana', 'apple', 'mango', 'pine-apple']

# list comprehension
array: list = [value for value in fruits]
print(f"array of fruits : {array}")

# list comprehension with conditions
mango: list = [value for value in fruits if value == 'mango']
print(f"mango : {mango}")