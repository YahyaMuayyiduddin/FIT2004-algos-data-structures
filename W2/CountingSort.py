

def counting_sort(lst,max):
    count = [0] * (max+1)
    for i in range(len(lst)):
        count[lst[i]] += 1
    res = [None] * len(lst)
    positions = [0] * (max+1)
    for i in range(1, len(positions)):
        positions[i] = positions[i-1] + count[i-1]

    for i in range(len(lst)):
        res[positions[lst[i]]] = lst[i]
        positions[lst[i]] += 1
    return res


lst = [3,2,1,4,6,5,4]

res = counting_sort(lst, 6)
print(res)