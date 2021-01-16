def waysToDecodeMsg(str1):
    letterMap = {
        "1": "a",
        "2": "b",
        "3": "c",
        "4": "d",
        "5": "e",
        "6": "f",
        "7": "g",
        "8": "h",
        "9": "i",
        "10": "j",
        "11": "k",
        "12": "l",
        "13": "m"
    }
    counter = 0
    prev_value = None

    if len(str1) == 1:
        if letterMap.get(str1):
            return 1

    for letter in str1:

        if prev_value is None:
            prev_value = letter
            if letter == "0":
                return 0
            continue

        if letterMap.get(prev_value):
            if counter == 0:
                counter += 1

        if letterMap.get(prev_value+letter):
            counter += 1
        prev_value = letter

    return counter


print(waysToDecodeMsg("2312"))
print(waysToDecodeMsg("1312"))
print(waysToDecodeMsg("13112"))
print(waysToDecodeMsg("4"))
print(waysToDecodeMsg("012"))
print(waysToDecodeMsg("11111"))
