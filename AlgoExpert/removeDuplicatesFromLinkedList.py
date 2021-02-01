# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeDuplicatesFromLinkedList(linkedList):
    # Write your code here.
	currNode = linkedList
	while currNode is not None:
		nextNode = currNode.next
		while nextNode is not None and currNode.value == nextNode.value:
			nextNode = nextNode.next

		currNode.next = nextNode
		currNode = nextNode
    return linkedList
