def threeNumberSum(array, targetSum):
    # Write your code here.
    array.sort()
    triplets = []
    for i in range(len(array)-2):
        left = i+1
        right = len(array)-1

        while left < right:
            tempSum = array[i] + array[left] + array[right]
            if tempSum == targetSum:
                triplets.append([array[i], array[left], array[right]])
                left += 1
                right -= 1
            elif tempSum < targetSum:
                left += 1
            elif tempSum > targetSum:
                right -= 1
    return triplets
