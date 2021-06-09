# p = 3
# q = 10
# r = 12
# p = (p+4)+q
# q = q+r
# p = (11 ^ 2) ^ p
# p = (9 ^ 12)+q
# print(p+q+r)


# def funn(a, b, c):

#     for c in range(5, 7):
#         a = (b+c)+b
#         if (5+8) > (a+5):
#             continue
#         else:
#             break
#         a = (c ^ 10)+b
#     return a+b


# print(funn(9, 3, 6))

# a = 5
# b = 4
# c = 6
# for c in range(5, 8):
#     if (a+c) > (b-a):
#         b = b+a
#     a = (b+5)+c
# print(a+b)

def numofballs(arr):
    count = 0
    for i in range(len(arr)):

        print((i+1)**2)
        diff = ((i+1)**2)-arr[i]
        count += diff

    if count == 0:
        return None
    return count


print(numofballs([1, 2, 7, 13]))
