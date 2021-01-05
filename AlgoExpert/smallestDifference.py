def smallestDifference(arrayOne, arrayTwo):
    # Write your code here.
    arrayOne.sort()
    arrayTwo.sort()
    smallestPair = []
    indexone = 0
    indextwo = 0
    smallestValue = float('inf')
    currentValue = float('inf')
    while indexone < len(arrayOne) and indextwo < len(arrayTwo):
        num1 = arrayOne[indexone]
        num2 = arrayTwo[indextwo]

        if num1 < num2:
            currentValue = num2 - num1
            indexone += 1
        elif num2 < num1:
            currentValue = num1 - num2
            indextwo += 1
        else:
            return [num1, num2]

        if currentValue < smallestValue:
            smallestValue = currentValue
            smallestPair = [num1, num2]
    return smallestPair
