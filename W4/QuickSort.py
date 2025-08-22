from W4.Partition import HoarePartition

def QuickSort(array,lo,hi):
    if lo < hi:
        pivotIndex = HoarePartition(array, lo, hi)
        QuickSort(array, lo, pivotIndex-1)
        QuickSort(array, pivotIndex + 1, hi)



if __name__ == "__main__":
    array = [34, 7, 56, 23, 89, 12, 67, 45, 90, 3, 78, 51, 29, 61, 8, 44, 72, 18, 39, 95]
    QuickSort(array, 0 , len(array) - 1)
    print(array)
