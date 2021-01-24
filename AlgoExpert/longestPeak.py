def longestPeak(array):
    # Write your code here.
	longestPeekLength = 0
    i = 1
	while i < len(array)-1:
		isPeak = array[i-1] < array[i] and array[i] > array[i+1]
		if not isPeak:
			i += 1
			continue
		leftIdx = i - 2 
		while leftIdx >= 0 and array[leftIdx] < array[leftIdx + 1]:
			leftIdx -= 1
			
		rightIdx = i + 2
		while rightIdx < len(array) and array[rightIdx] < array[rightIdx - 1]:
			rightIdx += 1
			
		currentPeakLenght = rightIdx - leftIdx -1
		longestPeekLength = max(longestPeekLength, currentPeakLenght)
		i = rightIdx
	return longestPeekLength
		
