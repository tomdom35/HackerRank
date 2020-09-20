

# Complete the findMergeNode function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def findMergeNode(head1, head2):
    nodes1 = []
    while head1 != None:
        nodes1.append(head1)
        head1 = head1.next
    while head2 not in nodes1:
        head2 = head2.next
    return head2.data

