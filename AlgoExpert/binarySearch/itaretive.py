def binarySearch(array, target):
    # Write your code here.
    left = 0
    right = len(array)-1
    mid = 0
    while left <= right:
        mid = (left + right)//2
        match = array[mid]
        if match == target:
            return mid
        elif target < match:
            right = mid-1
        else:
            left = mid+1
    return -1
