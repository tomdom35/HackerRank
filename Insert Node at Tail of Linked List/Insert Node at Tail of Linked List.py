

# Complete the insertNodeAtTail function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def insertNodeAtTail(head, data):
    if head != None:
        curNode = head
        while(curNode.next != None):
            curNode = curNode.next
        curNode.next = SinglyLinkedListNode(data)
    else:
        return SinglyLinkedListNode(data)
    return head

