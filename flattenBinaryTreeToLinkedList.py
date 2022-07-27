class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return

        nodes = []
        stack = [root]
        while stack:
            node = stack.pop()
            if not node:
                continue
            nodes.append(node)
            stack.append(node.right)
            stack.append(node.left)

        root = nodes.pop(0)
        for node in nodes:
            root.right = node
            root.left = None
            root = node