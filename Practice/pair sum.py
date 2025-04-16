listt = input("Take a list: ").split(', ')
target = int(input("Take a target: "))

listt = [int(value) for value in listt]
listt = sorted(listt)

l = 0
h = len(listt) - 1

def pairSum():
    print(listt)
    
    global l, h
    while l != h:
        # print("sum: ", listt[l] + listt[h], l, h)
        if listt[l] + listt[h] == target:
            return True
        elif listt[l] + listt[h] > target:
            h -= 1
        else:
            l += 1
    return False
print("Found" if pairSum() == True else "Not Found")