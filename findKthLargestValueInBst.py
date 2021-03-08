# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def findKthLargestValueInBst(tree, k):
    # Write your code here.
	sortedValues = []
	inOrderTraverse(tree, sortedValues)
    return sortedValues[len(sortedValues) - k]

def inOrderTraverse(tree, sortedValues):
	if tree is None:
		return
	inOrderTraverse(tree.left,sortedValues)
	sortedValues.append(tree.value)
	inOrderTraverse(tree.right,sortedValues)

# time O(n)
