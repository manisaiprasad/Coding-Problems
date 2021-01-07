def moveElementToEnd(array, toMove):
    # Write your code here.
	arrayValues = []
	counter = 0
    for i in range(len(array)):
        if array[i] == toMove:
        	counter += 1
    	else:
    		arrayValues.append(array[i])
	
	for i in range(counter):
		arrayValues.append(toMove)
	
	return arrayValues

# time complexity O(n)
# space complexity O(n)
