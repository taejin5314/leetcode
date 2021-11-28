from typing import List

class Solution:
  def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
    return graph

problem = Solution()
print(problem.allPathsSourceTarget([[1,2], [3], [3], []]))
print(problem.allPathsSourceTarget([[4,3,1],[3,2,4],[3],[4],[]]))
print(problem.allPathsSourceTarget([1], []))