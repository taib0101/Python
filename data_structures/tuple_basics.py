# tuple is immutable, means non-changeable, that means you can't insert, remove, modify like list
# Creating a tuple
colors: tuple = ("red", "green", "blue", "dark", "yellow")


# Creating single unit tuple
single: tuple = ("only",)


# find the the value within range
print("colours with ranage : ", colors[1:3])


# first two values
print("first two values : ", colors[:2])


# reversed values
print("reversed values : ", colors[::-1])

# index of blue
print("index of blue : ", colors.index("blue"))


# membership of yellow
print("is yellow exists ? ", "yellow" in colors)


# sort
numbers: tuple = (2, 4, 1, 0, 5)
print("sort : ", sorted(numbers))


# length of tuple
print("length : ", len(colors))


print((100,) is (100,))
print((100,) == (100,))
