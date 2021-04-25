def firstNonRepeatingCharacter(string):
    # Write your code here.
	count = {}
	for char in string:
		count[char] = count.get(char, 0)+1
	for i in range(len(string)):
		char = string[i]
		if count[char] == 1:
			return i
    return -1
