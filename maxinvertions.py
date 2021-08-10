
def getMaxInversions(arr, k):
    n = len(arr)
    if n == 1:
        return 0
    for i in range(k):
        arr.pop()

    n = len(arr)
    inv_count = 0
    for i in range(n):
        for j in range(i + 1, n):
            if (arr[i] > arr[j]):
                inv_count += 1

    return inv_count


n = int(input())
k = int(input())
array = []
for i in range(n):
    array.append(int(input()))
print(getMaxInversions(array, k))
