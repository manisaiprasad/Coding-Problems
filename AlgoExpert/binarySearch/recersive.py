def binarySearch(array, target):
    # Write your code here.
    return binarySearchHelper(array, target, 0, len(array)-1)


def binarySearchHelper(array, target, low, high):

    if low > high:
        return -1
    mid = (low+high)//2
    match = array[mid]
    if match == target:
        return mid
    elif target < match:
        return binarySearchHelper(array, target, low, mid-1)
    elif target > match:
        return binarySearchHelper(array, target, mid+1, high)
