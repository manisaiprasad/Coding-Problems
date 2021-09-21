def valid_parentheses(string):
    # your code here
    stack = []
    for char in string:
        if char == '(':
            stack.append(char)
        if char == ')':
            if len(stack) >= 1:
                stack.pop()
            else:
                return False
    return True if len(stack) == 0 else False
