def kadanesAlgorithm(array):
    # Write your code here.
    maxEndingCurrent = array[0]
    maxSoFar = array[0]
    for num in array[1:]:
        maxEndingCurrent = max(num, maxEndingCurrent + num)
        maxSoFar = max(maxSoFar, maxEndingCurrent)
    return maxSoFar
