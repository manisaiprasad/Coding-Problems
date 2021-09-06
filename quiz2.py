X = set(1, 2, 35, 4, 5, 6, 7, 8, 9, 10)
Y = set(1, 2, 13, 4, 5, 34, 7, 11, 9, 10)


def euclidean_distance(X, Y):
    return (sum([(x - y)**2 for x, y in zip(X, Y)]))**(1/2)


euclidean_distance(X, Y)
