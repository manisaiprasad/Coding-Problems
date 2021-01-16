def longestPalindromicSubstring(string):
    # Write your code here.
    longest = ""
    if len(string) == 1:
        return string
    for i in range(len(string)):
        for j in range(1, len(string)):
            subString = string[i:j+1]
            if len(subString) > len(longest) and isPalindrome(subString):
                longest = subString
    return longest


def isPalindrome(string):
    # Write your code here.
    reverse_chars = []
    for i in reversed(range(len(string))):
        reverse_chars.append(string[i])
    return "".join(reverse_chars) == string
