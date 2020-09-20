

# Complete the removeDuplicates function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def removeDuplicates(head):
    head = getNextNode(head)
    curNode = head
    
    while curNode.next != None:
        curNode.next = getNextNode(curNode.next)
        curNode = curNode.next

    return head

def getNextNode(node):
    while(node.next != None and node.next.data == node.data):
        node = node.next
    return node  


