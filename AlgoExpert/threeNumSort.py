def threeNumberSort(array, order):
    # Write your code here.
    counter = [0, 0, 0]
    for value in array:
        if value == order[0]:
            counter[0] += 1
        elif value == order[1]:
            counter[1] += 1
        elif value == order[2]:
            counter[2] += 1

    currentIdx = 0
    for i in range(3):

        for n in range(counter[i]):
            array[currentIdx] = order[i]
            currentIdx += 1

    return array
