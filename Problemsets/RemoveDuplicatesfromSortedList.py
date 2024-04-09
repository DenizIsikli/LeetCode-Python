# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        while current and current.next:
            if current.val == current.next.val:
                current.next = current.next.next
            else:
                current = current.next
        return head

    # I initialize a pointer current to the head of the linked list.
    # While current and the next node exist, meaning the current node is not the last node,
    # I check if the value of the current node is the same as the value of the next node.
    # If they are the same, I change the pointer of the current node to the node after the next node,
    # meaning I skip the next node to the next next node.
    # If they are not the same, I move the pointer current to the next node.
    # I return the head of the linked list after skipping all the duplicates.
