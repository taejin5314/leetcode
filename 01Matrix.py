from typing import List

class Solution:
  def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
    print(mat)

problem = Solution()
print(problem.updateMatrix([[0,0,0],[0,1,0],[0,0,0]]))
print(problem.updateMatrix([[0,0,0],[0,1,0],[1,1,1]]))