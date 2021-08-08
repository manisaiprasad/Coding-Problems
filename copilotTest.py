
def countCoins(radius, height, coinRadius):
    '''
    Count coins in a cylinder
    '''
    coins = 0
    for i in range(radius):
        for j in range(height):
            if ((i - coinRadius)**2 + (j - coinRadius)**2)**0.5 <= coinRadius:
                coins += 1
    return coins


print(countCoins(6, 12, 2))
