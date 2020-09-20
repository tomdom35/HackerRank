

# Complete the reverse function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def reverse(head):
    curNode = head
    tempList = []

    while(curNode.next != None):
        tempList.append(curNode)
        curNode = curNode.next

    curNode = head
    temp = curNode.next
    curNode.next = None
    curNode = temp
    
    for i in tempList:
        temp = curNode.next
        curNode.next = i
        if temp != None:
            curNode = temp

    return curNode
    




