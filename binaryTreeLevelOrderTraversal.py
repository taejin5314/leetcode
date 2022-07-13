class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root:
            queue, result = deque([root]), []
            
            while len(queue):
                n = len(queue)
                level = []
                for i in range(n):
                    cur = queue.popleft()
                    if cur.left:
                        queue.append(cur.left)
                    if cur.right:
                        queue.append(cur.right)
                    level.append(cur.val)
                result.append(level)
            
            return result
        else:
            return []