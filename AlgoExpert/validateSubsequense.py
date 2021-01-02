def isValidSubsequence(array, sequence):
    # Write your code here.
    seqIndex = 0
    for i in array:
        if seqIndex == len(sequence):
            break
        if i == sequence[seqIndex]:
            seqIndex += 1
    return seqIndex == len(sequence)
