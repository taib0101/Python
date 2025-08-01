# reference also called non-primitive or compound
# mutable means changeable
# immutable means non changeable

my_list: list = [1, 2, 3]                       # list (mutable and reference)
my_dict: dict = {"name": "taib", "age": 30}     # dict
my_set: set = {"banana", "apple"}               # set
my_tuple: tuple = (1, 2, 3)                     # tuple (immutable and reference)
my_byte: bytearray = bytearray(b"taib")         # mutable byte sequence


print("list : ", my_list)
print("dict : ", my_dict)
print("set : ", my_set)
print("tuple : ", my_tuple)
print("byte array : ", my_byte)