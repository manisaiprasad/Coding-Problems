# This is an input class. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def validateBst(tree):
    # Write your code here.
    return validBstHelper(tree, float('-inf'), float('inf'))


def validBstHelper(tree, minValue, maxValue):
    if tree is None:
        return True

    if tree.value < minValue or tree.value >= maxValue:
        return False

    leftIsValid = validBstHelper(tree.left, minValue, tree.value)
    return leftIsValid and validBstHelper(tree.right, tree.value, maxValue)
