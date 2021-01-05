def stringCompresstion(string):
    counter = 0
    compressedString = ""
    prevLetter = None

    for letter in string:
        if prevLetter is None:
            prevLetter = letter
            compressedString += prevLetter
            counter = 1
            continue

        if prevLetter == letter and counter != 0:
            counter += 1

        else:
            compressedString += str(counter)
            prevLetter = letter
            compressedString += prevLetter
            counter = 1

    return compressedString+str(counter)


print(stringCompresstion("aabccaaa"))
