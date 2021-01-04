def isPalindrome(string):
    # Write your code here.

    reverse_string = ""
    for i in reversed(range(len(string))):
        reverse_string += string[i]

    return reverse_string == string
