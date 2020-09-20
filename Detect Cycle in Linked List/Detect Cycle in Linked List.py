

# Complete the has_cycle function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def has_cycle(head):
    if head == None:
        return False
    
    pnt1 = head
    pnt2 = head.next
    count = 0

    while(pnt2 != None):
        if pnt1 == pnt2:
            return True

        pnt2 = pnt2.next
        
        if count % 2 == 0:
            pnt1 = pnt1.next
        count += 1

    return False


