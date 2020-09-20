

# Complete the compare_lists function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def compare_lists(llist1, llist2):
    if llist1 != None and llist2 != None:
        if llist1.data == llist2.data:
            return compare_lists(llist1.next, llist2.next)
    elif llist1 == None and llist2 == None:
        return 1
        
    return 0

