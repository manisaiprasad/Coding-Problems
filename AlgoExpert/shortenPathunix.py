def shortenPath(path):
    # Write your code here.
    stack = []
    tokens = path.split("/")
    startsWithSlash = path[0] == "/"
    short_path = []
    if startsWithSlash:
        short_path.append("")

    for token in tokens:
        # filter
        if token == "." or token == "":
            continue

        if token == "..":
            if len(stack) > 0 and stack[-1] != "..":
                stack.pop()
                continue
            elif not startsWithSlash:
                stack.append(token)
                continue
            else:
                continue

        stack.append(token)

    for item in range(len(stack)):
        short_path.append(stack[item])

    if len(stack) == 0 and startsWithSlash:
        return "/"

    return "/".join(short_path)
