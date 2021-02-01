def powerset(array):
    # Write your code here.
    subsets = [[]]
    for item in array:
        for i in range(len(subsets)):
            currentSubset = subsets[i]
            subsets.append(currentSubset + [item])
    return subsets
