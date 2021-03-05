# n_arr = int(input())
# arr = list(map(int, input().split(" ")))

# n_brr = int(input())
# brr = list(map(int, input().split(" ")))

# result = []
# for i in list(set(arr).difference(brr)):
#     result.append(i)

# for i in list(set(brr).difference(arr)):
#     result.append(i)

# set_difference = set(arr).intersection(brr)

# dict_arr = {i: arr.count(i) for i in arr}
# dict_brr = {i: brr.count(i) for i in brr}

# for i in set_difference:
#     if i in dict_arr and i in dict_brr:
#         if dict_arr[i] != dict_brr[i]:
#             result.append(i)


# print(result)

def countSetBits(n):
    count = 0
    while n:
        count += 1
        n &= (n-1)
    return count

# Function that return count of
# flipped number


def FlippedCount(a, b):

    # Return count of set bits in
    # a XOR b
    return countSetBits(a ^ b)


# Driver code
a = 7
b = 182
c = 256
print(FlippedCount(a, c))
