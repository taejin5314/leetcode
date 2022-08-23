class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        right = None
        while slow:
            nxt = slow.next
            slow.next = right
            right = slow
            slow = nxt
        
        while right:
            if right.val != head.val:
                return False
            right = right.next
            head = head.next
        return True
    