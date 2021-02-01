def reverseWordsInString(string):
    # Write your code here.
	tokens = string.split(" ")
	reversedWords = []
	for item in reversed(tokens):
		reversedWords.append(item)
    return " ".join(reversedWords)
