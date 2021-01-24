def longestSubstringWithoutDuplication(string):
    # Write your code here.
	seen = {}
	longest = [0, 1]
	startIdx = 0

    for i,char in enumerate(string):
		if char in seen:
			startIdx = max(startIdx, seen[char]+1)
		if longest[1] - longest[0] < i+1 -startIdx:
			longest = [startIdx, i+1]
		seen[char] = i
    return string[longest[0] : longest[1]]
		
