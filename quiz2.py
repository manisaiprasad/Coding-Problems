
def euclidean_distance(X, Y):
    
    return (sum([(x - y)**2 for x, y in zip(X, Y)]))**(1/2)


euclidean_distance(X, Y)
