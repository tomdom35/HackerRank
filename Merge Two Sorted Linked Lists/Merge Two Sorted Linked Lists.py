

# Complete the mergeLists function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
sys.setrecursionlimit(3000)

def mergeLists(head1, head2):
    if head1.data <= head2.data:
        return mergeListsHelper(head1, head1, head2)
    else:
        return mergeListsHelper(head2, head1, head2)

def mergeListsHelper(head, node1, node2):
    if node1 != None and node2 != None:
        if node1.data <= node2.data:
            if node1.next != None:
                if node1.next.data >= node2.data:
                    temp1 = node1.next
                    node1.next = node2
                    temp2 = node2.next
                    node2.next = temp1
                    return mergeListsHelper(head, node2, temp2)
                else:
                    return mergeListsHelper(head, node1.next, node2)
            else:
                node1.next = node2
                return head
        else:
            temp2 = node2.next
            node2.next = node1
            return mergeListsHelper(head, node2, temp2)
    else:
        return head
            




