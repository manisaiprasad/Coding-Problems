# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def findLoop(head):
    # Write your code here.
    slow = head.next
    fast = head.next.next
    while fast != slow:
        slow = slow.next
        fast = fast.next.next
    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next
    return slow

    # while fast and fast.next:
    # 	slow = slow.next
    # 	fast = fast.next.next
    # 	if slow == fast:
    # 		return slow.next
