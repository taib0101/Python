# primitive
x: int = 10 # immutable or nonchageable
print("address of x : ", id(x))

x += 1
print("address of x : ", id(x))

# reference
my_list: list = [1, 2, 3] # mutable or changeable
print("address of my_list : ", id(my_list))

my_list.append(4)
print("address of my_list : ", id(my_list))