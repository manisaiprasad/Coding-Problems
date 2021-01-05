def balancedBrackets(string):
    # Write your code here.
    stack = []
    opening_brackets = "([{"
    closing_brackets = "}])"
    matching_brackets = {
        ")": "(",
        "}": "{",
        "]": "["
    }
    for char in string:
        peek = len(stack)-1
        if char in opening_brackets:
            stack.append(char)

        if char in closing_brackets:
            if stack == []:
                return False
            if matching_brackets[char] == stack[peek]:
                stack.pop()
            else:
                return False

    return stack == []
