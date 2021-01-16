def gridTraverler(m, n, memo={(1, 1): 1}):
    key = (m, n)
    if m == 0 or n == 0:
        return 0

    if key in memo:
        return memo[(m, n)]
    else:
        memo[key] = gridTraverler(m-1, n) + gridTraverler(m, n-1)
    return memo[key]


print(gridTraverler(5, 6))
print(gridTraverler(8, 2))
