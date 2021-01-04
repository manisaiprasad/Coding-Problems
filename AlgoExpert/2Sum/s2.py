def twoNumberSum(array, targetSum):
    # Write your code here.
	nums = {}
	for num in array:
		complement = targetSum-num
		if complement in nums:
			return [complement, num]
		else:
            nums[num] = True
    return []
# time complexity O(n)
