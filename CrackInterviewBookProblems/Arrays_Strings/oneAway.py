def oneAway(string1, string2):
    counter = 0

    for letter in string1:

        if letter in string2:
            counter += 1

    if counter == len(string1)-1 or counter == len(string2)-1:
        return True

    return False


print(oneAway("pale", "ple"))  # true
print(oneAway("pale", "pales"))  # true
print(oneAway("pale", "bale"))  # true
print(oneAway("pale", "bake"))  # false
print(oneAway("", "a"))  # true
