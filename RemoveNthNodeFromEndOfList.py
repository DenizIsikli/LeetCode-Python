class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast, slow = head, head
        for _ in range(n): fast = fast.next
        if not fast: return head.next
        while fast.next: fast, slow = fast.next, slow.next
        slow.next = slow.next.next
        return head

    # I create two pointers, fast and slow, and set them both to head.
    # I move fast n nodes ahead of slow.
    # If fast is None, I return head.next.
    # If fast is not None, I move fast and slow forward until fast is None.
    # Then I set slow.next to slow.next.next.
    # Finally, I return head.
