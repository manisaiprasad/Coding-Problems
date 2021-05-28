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

# def countSetBits(n):
#     count = 0
#     while n:
#         count += 1
#         n &= (n-1)
#     return count

# Function that return count of
# flipped number


# def FlippedCount(a, b):

#     # Return count of set bits in
#     # a XOR b
#     return countSetBits(a ^ b)


# # Driver code
# a = 7
# b = 182
# c = 256
# print(FlippedCount(a, c))


# def fun1(p, q):
#     if q == 0:
#         return 0
#     if q % 2 == 0:
#         return fun1(p+p, q/2)
#     return fun1(p+p, q/2)+p

# def fun1(n):
#     if n > 100:
#         return n-10


# print(fun1(3, 4))

# a = 7
# b = 89

# for i in range(2, 6-1):
#     for j in range(i):
#         a = a+i+j
#         j += 2
#     i += 2
# print(a)

# a = 3
# b = 3
# n = 3
# for i in range(1, 3):
#     a = 1
#     b = 3
#     print(b)
#     for j in range(i-1):
#         c = b-a
#         print(c)
#         a = a+1
#     print("\n")

# def fun(x=3):
#     if x > 0:
#         fun(x-1)
#         print(x)
#         fun(x-1)


# fun()

# p=6
# q=10
# d=5
# for i in range(1,4):
#     r =

# ch1 = input()
# ch2 = input()
# diff = ord(ch2) - ord(ch1)
# value = diff + ord(ch2)
# print(chr(value))


# def nextGreaterInLeft(a):
#     left_index = [0] * len(a)
#     s = []
#     for i in range(len(a)):
#         while len(s) != 0 and a[i] >= a[s[-1]]:
#             s.pop()
#         if len(s) != 0:
#             left_index[i] = s[-1]
#         else:
#             left_index[i] = 0
#         s.append(i)
#     return left_index


# def nextGreaterInRight(a):
#     right_index = [0] * len(a)
#     s = []
#     for i in range(len(a) - 1, -1, -1):
#         while len(s) != 0 and a[i] >= a[s[-1]]:
#             s.pop()
#         if len(s) != 0:
#             right_index[i] = s[-1]
#         else:
#             right_index[i] = 0
#         s.append(i)
#     return right_index

# def LRProduct(arr):

#     left = nextGreaterInLeft(arr)
#     right = nextGreaterInRight(arr)
#     ans = -1
#     for i in range(1, len(left) - 1):

#         if left[i] == 0 or right[i] == 0:
#             ans = max(ans, 0)
#         else:
#             temp = (left[i] + 1) * (right[i] + 1)
#             ans = max(ans, temp)
#     return ans

# arr = [ 5, 4, 3, 4, 5 ]

# print(LRProduct(arr))

