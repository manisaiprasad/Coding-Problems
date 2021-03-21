price, change = input().split(",")
n = int(price) - int(change)
denoms = [0.01, 0.05, 0.10, 0.25, 0.50, 1, 2, 5, 10, 20, 50, 100]

if int(price) == int(change):
    print("ZERO")
elif int(price) > int(change):
    print("ERROR")
elif int(price) < int(change):
    numOfCoins = [float("inf") for amount in range(n+1)]
    numOfCoins[0] = 0
    for denom in denoms:
        for amount in (range(len(numOfCoins))):
            if denom <= amount:
                numOfCoins[amount] = min(
                    numOfCoins[amount], 1 + numOfCoins[amount-denom])
    print(numOfCoins[n] if numOfCoins[n] != float("inf") else -1)
