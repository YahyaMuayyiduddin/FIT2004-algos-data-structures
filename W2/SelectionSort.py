
"""
Worst/Best case: O(n)
Space complexity: O(n)
Auxillary: O(1)

"""
def selection_sort(lst):
    for i in range(len(lst)):
        min = i
        for j in range(i, len(lst)):
            if lst[j] < lst[min]:
                min = j
        lst[i], lst[min] = lst[min], lst[i]

res = [3,2,5,1,6]
selection_sort(res)
print(res)