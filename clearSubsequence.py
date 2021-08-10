def clearSubSequence(n, array):
    if n == 0:
        return 0
    prefix_sum = 0
    length = 0
    for i in range(n):
        prefix_sum += array[i]
        if prefix_sum > 0:
            print(i)
            length += 1
            print(length)
            continue

    return i


n = int(input())
array = []
for i in range(n):
    array.append(int(input()))
print(clearSubSequence(n, array))
