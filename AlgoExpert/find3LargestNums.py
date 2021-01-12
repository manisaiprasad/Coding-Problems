def findThreeLargestNumbers(array):
    # Write your code here.
    three_largest = [None, None, None]

    for num in array:
        updateThreeLargest(num, three_largest)
    return three_largest


def updateThreeLargest(num, three_largest):
    if three_largest[2] == None or num > three_largest[2]:
        shiftValue(three_largest, num, 2)
    elif three_largest[1] == None or num > three_largest[1]:
        shiftValue(three_largest, num, 1)
    elif three_largest[0] == None or num > three_largest[0]:
        shiftValue(three_largest, num, 0)


def shiftValue(array, num, idx):
    for i in range(idx + 1):
        if i == idx:
            array[i] = num
        else:
            array[i] = array[i+1]
