

# Complete the getNode function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def getNode(head, positionFromTail):
    return getNodeHelper(head, positionFromTail, [False])

def getNodeHelper(head, positionFromTail, found):
    if head.next == None:
        num = 0
    else:
        num = getNodeHelper(head.next, positionFromTail, found)
        if found[0]:
            return num
        else:
            num += 1
    if num == positionFromTail:
        found[0] = True
        return head.data
    else:
        return num



