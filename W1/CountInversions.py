
def merge_and_count(arr1, arr2):
    """
    Merge and counter function
    Time complexity: O(n) go through both lists
    Space complexity: O(n) create a new list
    
    
    """
    count = 0
    c1 = 0
    c2 = 0
    final = []
    while c1 < len(arr1) and c2 < len(arr2):
        if arr1[c1] <=  arr2[c2]:
            final.append(arr1[c1])
            c1 += 1
        else:
            final.append(arr2[c2])
            c2 += 1
            count += len(arr1) - c1
    while c1 < len(arr1):
        final.append(arr1[c1])
        c1 += 1
    while c2 < len(arr2):
        final.append(arr2[c2])
        c2 += 1
    return (final, count)


def countInversions(arr):
    """
    Count inversions
    Recurrence Relation for I(n): 
    2 * T(n/2) + cn for n > 1
    1               for n = 1 or n = 0


    """


    if len(arr) == 0:
        return (arr, 0)
    if len(arr) == 1:
        return (arr, 0)
    else:
        mid = (len(arr))//2
        left = countInversions(arr[0:mid])
        right = countInversions(arr[mid:len(arr)])
        merged = merge_and_count(left[0], right[0])
        arr = merged[0]
        cont = merged[1] + left[1] + right[1]
        return (arr, cont)

