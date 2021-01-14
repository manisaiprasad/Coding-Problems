def findClosestValueInBst(tree, target):
    # Write your code here.
    return findClosestValueInBstHelper(tree, target, tree.value)


def findClosestValueInBstHelper(currentNode, target, closest):
    if currentNode is None:
        return closest
    if abs(target - closest) > abs(target - currentNode.value):
        closest = currentNode.value
    if target < currentNode.value:
        return findClosestValueInBstHelper(currentNode.left, target, closest)
    elif target > currentNode.value:
        return findClosestValueInBstHelper(currentNode.right, target, closest)
    else:
        return closest

# This is the class of the input tree. Do not edit.


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
