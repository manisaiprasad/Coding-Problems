def staircase(n, memo={1: 1, 2: 2, 3: 4}):
    if n in memo:
        return memo[n]
    return staircase(n-1)+staircase(n-2)+staircase(n-3)
