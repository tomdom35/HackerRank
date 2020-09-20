

# Complete the sortedInsert function below.

#
# For your reference:
#
# DoublyLinkedListNode:
#     int data
#     DoublyLinkedListNode next
#     DoublyLinkedListNode prev
#
#
def sortedInsert(head, data):
    new = DoublyLinkedListNode(data)
    if head.data >= data:
        new.next = head
        head.prev = new
        return new

    curNode = head
    
    while(curNode.next != None):
        curNode = curNode.next
        if curNode.data >= data:
            new.next = curNode
            curNode.prev.next = new
            new.prev = curNode.prev
            curNode.prev = new
            return head

    curNode.next = new
    return head
    

