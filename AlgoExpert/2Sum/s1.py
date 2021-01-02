def twoNumberSum(array, targetSum):
    # Write your code here.
	for num in range(len(array)):
		for num2 in range(len(array)):
			if array[num]+array[num2]==targetSum:
				if num == num2:
					continue
				return [array[num],array[num2]]
	return []
