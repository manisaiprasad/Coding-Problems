def minNumofHops(array):
    if len(array) == 1:
        return 0
    hops = 0
    maxReach = array[0]
    steps = array[0]
    for i in range(1, len(array)-1):
        maxReach = max(maxReach, i+array[i])
        steps -= 1
        if steps == 0:
            hops += 1
            steps = maxReach-i

    return hops + 1


array = []
for i in range(11):
    val = int(input())
    array.append(val)

print(minNumofHops(array))
