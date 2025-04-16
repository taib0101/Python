list1 = [1, 2, 3]
list2 = list1
list2.append(4)
print("without breaking reference: ", list1)
del list1[len(list1) - 1]

list2 = list1.copy() # it breaks reference
list2.append(4)
print("with breaking reference: ", list1)
