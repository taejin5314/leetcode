# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def countNodes(self, root: Optional[TreeNode]) -> int:
    if not root:
      return 0
        
    left = self.getDepth(root.left)
    right = self.getDepth(root.right)
        
    if left == right:
      return pow(2, left) + self.countNodes(root.right)
    else:
      return pow(2, right) + self.countNodes(root.left)        
        
  def getDepth(self, root):
    if not root:
      return 0
      
    return 1 + self.getDepth(root.left)

problem = Solution()
print(problem.countNodes([1, 2, 3, 4, 5, 6]))