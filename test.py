# arr = [3, 3, 4, 4, 5]
# n = 5
# l = 10
# newArr = []
# arr.sort()
# if (arr[0]*n) < l:
#     print("-1")
# elif (arr[0]*n) == l:
#     print(arr[0])
# else:
#     for i in range(n-1):
#         newArr.append(arr[i]*n)
#     dist = abs(newArr[0]-l)
#     idx = 0
#     for i in range(1, n-1):
#         cdist = abs(newArr[i]-l)
#         if cdist < dist:
#             idx = i
#             dist = cdist
#     print(arr[idx])

# pp = 6
# qq = 3
# rr = 5

# qq = 1+rr
# qq = 5+qq
# if 5 < rr or (pp+rr) > (rr-pp):
#     pp = (9 & 7)+pp
#     qq = 5+qq
# print(pp+qq+rr)

# p = 4
# q = 2
# r = 7
# if 4 < q:
#     q = 1+r
# print(p+q+r)
# a = 5
# b = 7
# c = 67
# for i in range(3, 6-1):
#     b = (11+10) ^ c
#     if(c+7) > (b-c):
#         continue
#     else:
#         break
#     a = (a+a)+c
# print(a+b)
p = 5
q = 4
r = 8
for r in range(2, 7):
    p = (10+7)+p
    if (9-7) > (r-9):
        q = (p+r)+p
        p = r+p
print(p+q)
