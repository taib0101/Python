listt = [1, 2, 20, 4, 101, 50, 41]
print(sorted(listt))
print(listt[::-1]) # reverse
print("Filter with list comprehension: ", [value for value in listt if value % 2 == 0])


listt1 = [
    {
        'name': 'Taib',
        'age': 40
    },
    {
        'name': 'Anik',
        'age': 10
    }
]

print(list(map(lambda x: x['age'], listt1)))

listt2 = [1, 2, 3, 4]
listt2.append(10)

del listt2[0] # delete specific index of list
print(listt2)

print(listt2.index(10)) # index of list's value