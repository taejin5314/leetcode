# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        stack = [(original, cloned)]
        while stack: 
            x, y = stack.pop()
            if x == target: return y
            if x:
                stack.append((x.left, y.left))
                stack.append((x.right, y.right))