class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return
        node = [root]
        while node:
            cur = node.pop()
            if cur.left and cur.right:
                cur.left.next = cur.right
                if cur.next:
                    cur.right.next = cur.next.left
                node.append(cur.right)
                node.append(cur.left)
        return root
        