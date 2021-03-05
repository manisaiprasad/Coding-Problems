size = int(input())
findInt = int(input())
counter = 0
for i in range(1, size+1):
    for j in range(1, size+1):
        res = i*j
        if res == findInt:
            counter += 1
print(counter)
