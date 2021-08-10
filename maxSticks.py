def maxSticks(n, k, sticks):
    sticks.sort()
    maxSum = 0
    newArray = []
    while n <= k:
        if n == k:
            for i in range(n):
                maxSum += (sticks[i] * sticks[i])
            return maxSum
        else:
            maxValue = sticks.pop()
            print(sticks)
            if maxValue % 2 != 0:
                sticks.append(int(maxValue/2)+maxValue % 2)
            else:
                sticks.append(int(maxValue/2))

            sticks.append(int(maxValue/2))
            sticks.sort()
            print(sticks)
            n = len(sticks)


n = int(input())
k = int(input())
sticks = []
for i in range(n):
    sticks.append(int(input()))
print(maxSticks(n, k, sticks))
