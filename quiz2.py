
def euclidean_distance(X, Y):
    
    return (sum([(x - y)**2 for x, y in zip(X, Y)]))**(1/2)


euclidean_distance(X, Y)

def fizzBuzz(n):
    for i in range(1, n+1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)
