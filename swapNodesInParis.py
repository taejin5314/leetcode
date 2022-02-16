class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head:
            h = head.next
            if h:
                h.next, head.next = head, h.next
                h.next.next = self.swapPairs(h.next.next)
                return h
        return head