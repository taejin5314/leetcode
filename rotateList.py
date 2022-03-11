class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None
        
        node = head
        length = 1
        while node.next:
            length += 1
            node = node.next
            
        k = k % length
        
        node.next = head
        newNode = head
        for _ in range(length - k - 1):
            newNode = newNode.next
        
        result = newNode.next
        newNode.next = None

        return result
        