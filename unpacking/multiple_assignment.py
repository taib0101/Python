
# Assign multiple value in one line
x, y, z = 1, 2, 3
print(f"x = {x}, y = {y}, z = {z}")


# same value into multiple variables
a = b = c = 0
print(f"a = {a}, b = {b}, c = {c}") 


# swap the value
a, b = 10, 20
a, b = b, a
print(f"a = {a}, b = {b}")

# ignore the unused value with underscore(_)
left, _, right = ['Alice', 30, 'shit']
print(f"left = {left}, right = {right}")