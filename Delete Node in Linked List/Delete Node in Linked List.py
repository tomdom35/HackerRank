

# Complete the deleteNode function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def deleteNode(head, position):
    headNode = head
    curNode = head

    if position == 0:
        headNode = head.next
    else:

        for i in range(position-1):
            curNode = curNode.next

        temp = curNode.next.next
        curNode.next = temp

    return headNode

