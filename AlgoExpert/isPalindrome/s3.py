def isPalindrome(string):
    # Write your code here.
    leftIndex = 0
    rightIndex = len(string)-1

    while(leftIndex < rightIndex):
        if string[leftIndex] == string[rightIndex]:
            leftIndex += 1
            rightIndex -= 1
        else:
            return False
    return True
