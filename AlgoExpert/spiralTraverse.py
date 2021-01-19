def spiralTraverse(array):
    # Write your code here.
    startRow, endRow = 0, len(array)-1
    startCol, endCol = 0, len(array[0])-1
    new_array = []
    while startRow <= endRow and startCol <= endCol:
        for col in range(startRow, endCol + 1):
            new_array.append(array[startRow][col])

        for row in range(startRow+1, endRow+1):
            new_array.append(array[row][endCol])

        for col in reversed(range(startCol, endCol)):
            if startRow == endRow:
                break
            new_array.append(array[endRow][col])

        for row in reversed(range(startRow + 1, endRow)):
            if startCol == endCol:
                break
            new_array.append(array[row][startCol])

        startRow += 1
        endRow -= 1
        startCol += 1
        endCol -= 1

    return new_array
