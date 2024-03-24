# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        current = dummy

        while current.next:
            if current.next.val == val:
                current.next = current.next.next
            else:
                current = current.next

        return dummy.next

    # I create a dummy node and set its next to the head of the linked list.
    # I then iterate through the linked list.
    # If the value of the current node is equal to the target value, I skip that node.
    # Otherwise, I move the current pointer to the next node, removing the current node from the list.
    # Finally, I return the next node of the dummy node, which is the new head of the linked list.
