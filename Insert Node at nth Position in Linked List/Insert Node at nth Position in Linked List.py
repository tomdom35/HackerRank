

# Complete the insertNodeAtPosition function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def insertNodeAtPosition(head, data, position):
    headNode = head
    newNode = SinglyLinkedListNode(data)

    if position == 0:
        headNode = newNode
        newNode.next = head
    else:
        curNode = head
    for i in range(position-1):
        curNode = curNode.next

    temp = curNode.next
    curNode.next = newNode
    newNode.next = temp

    return headNode


