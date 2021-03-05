def generateDocument(characters, document):
    # Write your code here.
    charCounter = {}

    for char in characters:
        if char in charCounter:
            charCounter[char] = charCounter[char]+1
        else:
            charCounter[char] = 1

    for char in document:
        if char not in charCounter or charCounter[char] == 0:
            return False
        charCounter[char] = charCounter[char]-1
    return True
