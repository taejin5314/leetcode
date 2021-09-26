from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next

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

head = ListNode([1, 2, 2, 1])
problem = Solution()
print(problem.isPalindrome(head))