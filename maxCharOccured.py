def maxElement(input1):
    all_freq = {}
    for i in input1:
        if i in all_freq:
            all_freq[i] += 1
        else:
            all_freq[i] = 1
    res = max(all_freq, key=all_freq.get)
    return str(res)


print(maxElement("abcdd"))
