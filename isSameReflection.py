def isSameReflection(word1, word2):
    start = word2[0]
    word1Idx = word1.find(start)
    newWord = word1[word1Idx:]
    rev = word1[:word1Idx][::-1]
    print(newWord+rev)
    if newWord == word2:
        return 1
    return -1


isSameReflection("manisai", "saimani")
