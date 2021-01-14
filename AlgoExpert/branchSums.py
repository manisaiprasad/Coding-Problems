# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def branchSums(root):
    # Write your code here.
	sums = []
    findbranchSums(root, 0, sums)
    return sums

def findbranchSums(node, currentSum, sums):
    if node is None:
    	return
	
	newCurrentNode = currentSum + node.value
	if node.left is None and node.right is None:
		sums.append(newCurrentNode)
		return
	findbranchSums(node.left, newCurrentNode, sums)
	findbranchSums(node.right, newCurrentNode, sums)
