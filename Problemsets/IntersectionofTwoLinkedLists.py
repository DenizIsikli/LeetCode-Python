class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if not headA or not headB:
            return None

        p,q = headA , headB
        while p and q and p != q :
            p = p.next
            q = q.next
            if p == q :
                return q
            if not p :
                p = headB
            if not q :
                q = headA
        return p

    # While "p" and "q" exists, and don't match, they go to the next element in their own list. If "p" and "q" match
    # I return q (headB).

    # Lastly I check if "p" is out of elements and I thereby intersect it with headB, and likewise with "q" if
    # the list is out of elements and I thereby intersect it with headA
