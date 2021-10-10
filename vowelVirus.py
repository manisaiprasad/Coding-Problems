def slove(L, M):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = ''
    for char in M:
        if char in vowels:
            result += 'x'*(ord(char)-96)
            continue
        result += char
    return result
