# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        listLength = 0
        pos = head
        result = []
        
        while pos:
            pos = pos.next
            listLength += 1
        
        division, extra = divmod(listLength, k)
        
        pos2 = head
        cur = ListNode()
        cur.next = head
        for i in range(k):
            ans = cur
            for _ in range(division + int(i < extra)):
                cur = cur.next

            result.append(ans.next)
            ans.next = None
        return result