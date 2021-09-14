
# # def productOfDigits(n):
# #     return n if n < 10 else productOfDigits(n//10) * n % 10


# # print(productOfDigits(int(input())))

# def commonInBothStrings(str1,str2):

#     for char in str1:
#         for char2 in str2:
#             if char == char2:
#                 print(char)
#                 break


# print(commonInBothStrings(input(),input()))


# MAX_CHAR=26

# def printCommon( s1, s2):

#     a1 = [0 for i in range(MAX_CHAR)]
#     a2 = [0 for i in range(MAX_CHAR)]

#     length1 = len(s1)
#     length2 = len(s2)

#     for i in range(0,length1):
#         a1[ord(s1[i]) - ord('a')] += 1

#     for i in range(0,length2):
#         a2[ord(s2[i]) - ord('a')] += 1

#     for i in range(0,MAX_CHAR):
#         if (a1[i] != 0 and a2[i] != 0):

#             for j in range(0,min(a1[i],a2[i])):
#                 ch = chr(ord('a')+i)
#                 print (ch, end='')


# s1 = input()
# s2 = input()
# printCommon(s1, s2)


N = int(input())
arr = []
for i in range(N):
    arr.append(int(input()))

splited = [arr[x:x+3] for x in range(0, len(arr), 3)]

K = int(input())


def value(splited):
    for line in splited:
        if K not in line:
            return 0
    return 1
