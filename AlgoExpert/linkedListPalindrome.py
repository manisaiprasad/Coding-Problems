# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

# Time O(n) Space O(1)


def linkedListPalindrome(head):
    # Write your code here.
    slow = head
    fast = head
    while fast is not None and fast.next is not None:
        fast = fast.next.next
        slow = slow.next

    reversedListNode = reverseList(slow)
    firstHalfNode = head

    while reversedListNode is not None:
        if reversedListNode.value != firstHalfNode.value:
            return False
        reversedListNode = reversedListNode.next
        firstHalfNode = firstHalfNode.next

    return True


def reverseList(head):
    prevNode, currentNode = None, head
    while currentNode is not None:
        nextNode = currentNode.next
        currentNode.next = prevNode
        prevNode = currentNode
        currentNode = nextNode
    return prevNode
