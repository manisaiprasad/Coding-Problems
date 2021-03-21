def sortedSquaredArray(array):
    # Write your code here.
	for idx in range(len(array)):
		num = array[idx]
		array[idx] = num*num

	array.sort()
    return array

print(sortedSquaredArray([1,2,3,4,5,6,7,8]))
