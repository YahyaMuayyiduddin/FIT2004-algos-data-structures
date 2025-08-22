# def merge_k(lists):
#     idx = [1] * len(lists)
#     res = []


def remove_duplicates(l):
    lst = sorted(l)

    for i in range(1, len(lst)):
        if lst[i] == lst[i-1]:
            lst[i-1] = None
    
    return lst



print(remove_duplicates([3,4,3,2,5,2,1,5,6,2,6]))