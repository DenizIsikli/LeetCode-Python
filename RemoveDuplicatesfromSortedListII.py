# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        dummy = ListNode(0, head)
        prev = dummy
        curr = head

        while curr:
            if curr.next and curr.val == curr.next.val:
                while curr.next and curr.val == curr.next.val:
                    curr = curr.next
                prev.next = curr.next
            else:
                prev = prev.next
            curr = curr.next

        return dummy.next

    # I first check if the list is empty, if it is, I return the list
    # I create a dummy node to store the head of the list
    # I create a prev pointer to keep track of the previous node
    # I create a curr pointer to keep track of the current node
    # I iterate through the list
    # If the current node has a next node and the value of the current node is equal to the value of the next node
    # I iterate with a while loop to find the last occurrence of the value of the current node
    # I then set the next node of the previous node to the next node of the current node
    # Otherwise, I set the next node of the previous node to the next node of the current node
    # I set the current node to the next node of the current node
    # I return the next node of the dummy node
