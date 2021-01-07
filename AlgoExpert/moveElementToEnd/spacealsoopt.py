def moveElementToEnd(array, toMove):
    # Write your code here.
	left = 0
	right = len(array)-1
	while left < right:
		while left < right and array[right] == toMove:
			right -= 1
		if array[left] == toMove:
			array[left], array[right] = array[right], array[left]

		left += 1
    return array
# time O(n)
# space O(n)
