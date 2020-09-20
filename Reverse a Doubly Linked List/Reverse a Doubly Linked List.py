

# Complete the reverse function below.

#
# For your reference:
#
# DoublyLinkedListNode:
#     int data
#     DoublyLinkedListNode next
#     DoublyLinkedListNode prev
#
#
def reverse(head):
    if head == None or head.next == None:
        return head

    curNode = head

    while curNode != None:
        n = curNode.next
        p = curNode.prev
        curNode.next = p
        curNode.prev = n
        curNode = n

    return p.prev

