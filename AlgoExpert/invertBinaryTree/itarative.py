def invertBinaryTree(tree):
    # Write your code here.
    queue = [tree]
    while len(queue):
        current = queue.pop(0)
        if current is None:
            continue

        current.left, current.right = current.right, current.left

        queue.append(current.left)
        queue.append(current.right)


# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
