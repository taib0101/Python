# Convert integer to string
x = 120
print(str(x))

# Convert string to integer
y = "210"
print(int(y))

# Convert Array to string 
arr = [1, 2, 3]
print(" ".join(str(value) for value in arr if value == 2))

# Convert string to Array
str = "Mustain Murtaza Taib"
print(str.split(' '))

# Convert list to Array 
import numpy as np
listt = [1, 2, 3, 4, 5]
print(np.array(listt))
# print([x**2 for x in listt])

# Convert Array to list
arr = np.array([1, 2, 3, 4, 5])
print(arr.tolist())