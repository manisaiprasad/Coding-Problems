def sumofTwo(array1, array2, target):
    for i in array1:
        complement = target - i
        if complement in array2:
            return True


print(sumofTwo([2, 4, -3, 5], [6, 8, 4, 5], 1))
