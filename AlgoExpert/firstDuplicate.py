def firstDuplicateValue(array):
    # Write your code here.
    seen = set()
    for i in array:
        if i in seen:
            return i
        else:
            seen.add(i)

    return -1
