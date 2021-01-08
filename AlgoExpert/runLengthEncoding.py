def runLengthEncoding(string):
    # Write your code here.
    counter = 0
    compressed_string = []
    prevLetter = None

    for letter in range(len(string)):

        if prevLetter == None:
            prevLetter = string[letter]
            counter = 1
            continue

        if prevLetter == string[letter] and counter < 9:
            counter += 1
        else:
            compressed_string.append(str(counter))
            compressed_string.append(prevLetter)
            prevLetter = string[letter]
            counter = 1
        print(compressed_string)
    # lastrun
    compressed_string.append(str(counter))
    compressed_string.append(prevLetter)

    return "".join(compressed_string)
