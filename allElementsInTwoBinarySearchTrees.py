class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        res = []
        
        def rec(node):
            if node:
                res.append(node.val)
                
                rec(node.left)
                rec(node.right)
        
		# traverse first tree, append nodes
        rec(root1)
		
		# traverse second tree, append nodes
        rec(root2)
        
		# return sorted array
        return sorted(res)