from Partition import HoarePartition

def QuickSelect(array, low, high, k):
    target = len(array) - k
    pivotIndex = HoarePartition(array, low, high)
    if pivotIndex == target:
        return pivotIndex
    if pivotIndex < target:
        return QuickSelect(array, pivotIndex+1, high,k)
    elif pivotIndex > target:
        return QuickSelect(array, low, pivotIndex-1,k)

if __name__ == "__main__":
    array = [34, 7, 56, 23, 89, 12, 67, 45, 90, 3, 78, 51, 29, 61, 8, 44, 72, 18, 39, 95]
    print(array[QuickSelect(array, 0, len(array)-1, 2)])

