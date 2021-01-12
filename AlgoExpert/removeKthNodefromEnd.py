# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeKthNodeFromEnd(head, k):
    # Write your code here.
    len_node = head
    node = head
    counter = 0
    listlen = 0

    while len_node.next is not None:
        len_node = len_node.next
        listlen += 1

    while counter != listlen-k and node.next is not None:
        node = node.next
        counter += 1

    if node.next is not None:
        node.next = node.next.next

    if listlen-k == -1:
        head.value = head.next.value
        head.next = head.next.next
