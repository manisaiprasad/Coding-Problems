def getNthFib(n, memo={2: 1, 1: 0}):
    # Write your code here.
    if n in memo:
        return memo[n]
    else:
        memo[n] = getNthFib(n-1)+getNthFib(n-2)

    return memo[n]


print(getNthFib(23))
