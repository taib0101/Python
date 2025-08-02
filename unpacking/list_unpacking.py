
listt: list = [1, 2, 3, 4, 5]


# unpack into single unit
a, b, c, d, e = listt
print(f"a = {a}, b = {b}, c = {c}, d = {d}, e = {e}")


# unpack into only three unit
*left,   middle, right = listt
print(f"left = {left}, middle = {middle}, right = {right}")


# same as shit 
left, *middle, right = listt
print(f"left = {left}, middle = {middle}, right = {right}")


# same as shit
left, middle, *right = listt
print(f"left = {left}, middle = {middle}, right = {right}")