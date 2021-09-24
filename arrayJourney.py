def array_journal(path, max_steps):
    sum = 0
    for i in range(max_steps, len(path)+1):
        firstidx = i-max_steps
        max_Sums = []
        for j in range(max_steps):
            secondidx = firstidx + j
            max_Sums.append(path[secondidx])
        sum += max(max_Sums)
    sum += path[-1]
    return sum


if __name__ == "__main__":
    path = [10, 2, -10, 5, 10]
    max_steps = 2
    print(array_journal(path, max_steps))
