from typing import Optional

class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

class Solution:
  def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
    if not root:
      return None

    if root.val == key:
      if root.left:
        left_right_most = root.left
        while left_right_most.right:
          left_right_most = left_right_most.right
        
        left_right_most.right = root.right

        return root.left
      else:
        return root.right
    elif root.val > key:
      root.left = self.deleteNode(root.left, key)
    else:
      root.right = self.deleteNode(root.right, key)
      
    return root

problem = Solution()
print(problem.deleteNode([5,3,6,2,4,None,7], 3))