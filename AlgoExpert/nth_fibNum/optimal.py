def getNthFib(n):
    # Write your code here.
    first = 0
    last = 1
    counter = 2

    while counter < n:
        nextfib = first + last
        first = last
        last = nextfib
        counter += 1

    return last if n > 1 else first

# o(n)
