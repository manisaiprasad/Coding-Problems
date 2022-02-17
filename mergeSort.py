def merge(left, right):
    print(left, right)
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    print("result")
    print(result)
    return result


def mergeSort(L):
    if len(L) < 2:
        return L[:]
    else:
        middle = len(L)//2
        left = mergeSort(L[:middle])
        right = mergeSort(L[middle:])
        print("left")
        print(left)
        print("right")
        print(right)
        return merge(left, right)


L = [3, 2, 1, 6, 7, 4, 5, 8]
print(mergeSort(L))
