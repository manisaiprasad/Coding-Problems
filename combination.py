from itertools import permutations
N = int(input())
comb = permutations(['A', 'B'], N)
# Print the obtained combinations
for i in list(comb):
    print(i)
