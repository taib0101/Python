
# nested list comprehesion
coordinate: list = [(x, y) for x in range(3) for y in range(4)]
print(f"list of coordiante : {coordinate}")


# nested dict comprehension
table: dict = {key: {value for value in range(2)} for key in range(3)}
print(f"table : {table}")