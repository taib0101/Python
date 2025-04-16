import numpy as np

listt = input("Take list input: ").split(',')
listt = [int(value) for value in listt]

def merge_sort(l, r):
    if l == r:
        return None
    mid = int((l + r) / 2)
    merge_sort(l, mid)
    merge_sort(mid + 1, r)

    temp = np.full(r+1, 0, dtype=int)
    temp = temp.tolist()

    i = l
    j = mid+1
    k = l

    # print(l, r, mid)
    for kk in range(k, r+1):
        if i == mid+1:
            temp[kk] = listt[j]
            j += 1
        elif j == r+1:
            temp[kk] = listt[i]
            i += 1
        elif listt[i] >= listt[j]:
            temp[kk] = listt[j]
            j += 1
        else:
            temp[kk] = listt[i]
            i += 1
    
    for kk in range(k, r+1):
        listt[kk] = temp[kk]

    del temp
    return None

merge_sort(0, len(listt) - 1)

print(listt)