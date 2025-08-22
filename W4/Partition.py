import random

def HoarePartition(array):
    pivotIndex = random.randint(0, len(array)-1)
    pivot = array[pivotIndex]
    array[0], array[pivotIndex] = array[pivotIndex], array[0]
    lo = 1
    hi = len(array) - 1
    while lo <= hi:
        while lo <= hi and array[lo] <= pivot: lo += 1
        while lo <= hi and array[hi] > pivot: hi -= 1
        if lo <= hi:
            array[hi], array[lo] = array[lo], array[hi]
    
    array[0], array[hi] = array[hi], array[0]
    return hi

def HoarePartition(array,low,high):
    pivotIndex = random.randint(low, high)
    pivot = array[pivotIndex]
    array[low], array[pivotIndex] = array[pivotIndex], array[low]
    lo = low + 1
    hi = high
    while lo <= hi:
        while lo <= hi and array[lo] <= pivot: lo += 1
        while lo <= hi and array[hi] > pivot: hi -= 1
        if lo <= hi:
            array[hi], array[lo] = array[lo], array[hi]
    
    array[low], array[hi] = array[hi], array[low]
    return hi

# array = [34, 7, 56, 23, 89, 12, 67, 45, 90, 3, 78, 51, 29, 61, 8, 44, 72, 18, 39, 95]
# print(HoarePartition(array))
# print(array)
    


