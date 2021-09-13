
def FindMeOut(input1):
    multiples = []
    for i in range(2, 20):
        multiples.append(input1 * i)
    for multiple in multiples:
        s = sum(int(digit) for digit in str(multiple))
        if(input1 == s):
            return multiple
    return -1

    
    # i = 1
    # while (1):
    #     # Checking if number has
    #     # sum of digits = N
    #     if (getSum(i) == input1):
    #         return(i)
    #         break

    #     i += 1

# def FindMeOut(s, base=10):

#     best = dict()
#     best[(0, 0)] = 0
#     new_candidates = dict()
#     new_candidates[(0, 0)] = 0

#     target_key = (s, 0)
#     dc = 0
#     while (True):
#         dc += 1
#         candidates = new_candidates
#         new_candidates = dict()
#         for ((ds, r), v) in candidates.items():
#             vhi = v * base
#             rhi = r * base
#             for d in range(0, base):
#                 nv = vhi + d
#                 nds = ds + d
#                 nr = (rhi + d) % s
#                 nkey = (nds, nr)
#                 if nkey not in best or nv < best[nkey]:
#                     best[nkey] = nv
#                     new_candidates[nkey] = nv
#         if target_key in best:
#             if len(str(best[target_key])) == 1:
#                 return best[target_key]*2
#             return best[target_key]


print(FindMeOut(9))
print(FindMeOut(10))
