def isPalindrome(string):
    # Write your code here.
    reverse_chars = []
    for i in reversed(range(len(string))):
        reverse_chars.append(string[i])
    return "".join(reverse_chars) == string
