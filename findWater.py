def findWater(i, j, val):

    glass = [0]*int(i * (i + 1) / 2)
    index = 0
    glass[index] = val

    for row in range(1, i):
        for col in range(1, row+1):
            val = glass[index]
            glass[index] = 1.0 if (val >= 1.0) else val
            val = (val - 1) if (val >= 1.0) else 0.0
            glass[index + row] += (val / 2)
            glass[index + row + 1] += (val / 2)
            index += 1

    return glass[int(i * (i - 1) / 2 + j - 1)]


print(findWater(3, 3, 5))
