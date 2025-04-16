# Input Array
# arr1 = input().split()
# print(f"Array is : {arr1}")
# print(f"Last value of Array : {arr1[2]}")

# Declaring Array with specific size
import numpy as np
arr2 = np.full(5, 7, dtype=int) # for 1D Array
print(arr2)

arr3 = np.full((3, 2), 'Upamaa', dtype='U6') # for 2d Array 
print(arr3)

"""
    dtype: int, float, double, str, 'U6'
"""

# push as append pop as delete in numpy
arr4 = np.array([1, 2, 3])
arr4 = np.append(arr4, 10)
arr4 = np.append(arr4, 20)
arr4 = np.delete(arr4, 0) # any kind of index can delete
print(arr4)

# length
arr5 = np.array([1, 2, 3, 4])
print("Size = ", arr5.size)
print("Shape = ", arr5.shape) # for 2d array
print("Length = ", len(arr5))

# Map lambda function
arr6 = np.array([
    {
        'name': 'Anik',
        'age': 30
    },
    {
        'name': 'Taib',
        'age': 26
    }
])

# def mapFunction(x):
#     return x['name']
# names = np.vectorize(mapFunction)(arr6)

names = np.vectorize(lambda x: x['name'])(arr6)

print(names)

# sort
arr7 = np.array([1, 10, 5, 20, 30])
# np.sort(arr7)
print("sort asc: ", np.array(sorted(arr7))) # ascending
print("sort desc: ", np.array(sorted(arr7))[::-1]) # descending

arr8 = np.array([
    {
        'name': 'Anik',
        'age': 30
    },
    {
        'name': 'Taib',
        'age': 26
    }
])

print(np.array(sorted(arr8, key=lambda x: x['age'])))

# index
arr11 = np.array([1, 2, 3, 4, 5])
print(np.where(arr11 == 2)[0][0])

# filter
arr9 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(arr9[(arr9 > 2) & (arr9 < 8)])

# reverse array
arr10 = np.array([1, 2, 3, 4, 5])
print(arr10[::-1])

# slice 
arr12 = np.array([1, 20, 30, 4, 5])
print(arr12[1:3])

# includes
arr13 = [1, 2, 3, 4]
print(1 in arr13)