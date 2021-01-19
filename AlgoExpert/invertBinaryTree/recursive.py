def invertBinaryTree(tree):
    # Write your code here.
    root = tree
    if root is None:
        return
    root.left, root.right = root.right, root.left
    invertBinaryTree(root.left)
    invertBinaryTree(root.right)

# This is the class of the input binary tree.


class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
# time O(n) space(d)
