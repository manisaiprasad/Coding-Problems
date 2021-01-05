def threeNumberSum(array, targetSum):
    # Write your code here.
	result = []
	array.sort()
    for i in range(len(array)):
		for j in range(i+1,len(array)):
			for k in range(j+1,len(array)):
				sum = array[i]+array[j]+array[k]
			    if sum == targetSum:
					temp_array = [array[i],array[j],array[k]]
					result.append(temp_array)
	return result
						

threeNumberSum([1, 2, 3, 4, 5, 6, 7, 8, 9, 15], 18)

