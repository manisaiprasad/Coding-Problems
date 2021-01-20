def globMatching(fileName, pattern):
    # Write your code here.
    astrixFound = False
    fileIdx = 0
    patternIdx = 0
    patterMatched = False
    while fileIdx < len(fileName) and patternIdx < len(pattern):

        if pattern[patternIdx] == "*" and len(pattern) == 1:
            return True

        if pattern[patternIdx] == "*":
            astrixFound = True
            patternIdx += 1

        if pattern[patternIdx] == "?":
            patternIdx += 1
            fileIdx += 1
            patterMatched = True
            astrixFound = False
            continue

        if fileName[fileIdx] == pattern[patternIdx]:
            patternIdx += 1
            fileIdx += 1
            patterMatched = True
            astrixFound = False
            continue

        if fileName[fileIdx] != pattern[patternIdx] and astrixFound:
            fileIdx += 1
            continue
    return patterMatched


print(globMatching("abcdefgh", "a*e?g"))
print(globMatching("abcdefgh", "*"))
