fruits: set = {'banana', 'apple', 'mango', 'lichi', 'mango'}

# set comprehensions
sett: set = {value for value in list(fruits)}
print(f"sett of fruits : {sett}")

# set comprehension
lichi: set = {value for value in list(sett) if value == 'lichi'}
print(f"sett of lichi : {lichi}")