from typing import List

class Solution:
  def shortestPath(self, grid: List[List[int]], k: int) -> int:
    for i in range(len(grid)):
      for j in range(len(grid[i])):
        print(grid[i][j])

problem = Solution()
print(problem.shortestPath([[0,0,0],
 [1,1,0],
 [0,0,0],
 [0,1,1],
 [0,0,0]], 1))
print(problem.shortestPath([[0,1,1],
 [1,1,1],
 [1,0,0]], 1))