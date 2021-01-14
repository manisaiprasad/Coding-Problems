def iterativeInOrderTraversal(tree, callback):
    # Write your code here.

    prevNode = None
    currentNode = tree
    while currentNode is not None:
        if currentNode is None or prevNode == currentNode.parent:
            if currentNode.left is not None:
                nextNode = currentNode.left
            else:
                callback(currentNode)
                nextNode = currentNode.right if currentNode.right is not None else currentNode.parent
        elif prevNode == currentNode.left:
            callback(currentNode)
            nextNode = currentNode.right if currentNode.right is not None else currentNode.parent
        else:
            nextNode = currentNode.parent
        prevNode = currentNode
        currentNode = nextNode
