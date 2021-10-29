from typing import List
from collections import deque

class Solution:
  def orangesRotting(self, grid: List[List[int]]) -> int:
    rows = len(grid)
    cols = len(grid[0])
    res = 0
        
    queue = deque([])
        
    for i in range(rows):
      for j in range(cols):
        if grid[i][j] == 2:
          queue.append([i, j, res])
          grid[i][j] = 0
                    
    while queue:
      x, y, res = queue.popleft()
            
      for i, j in [x-1, y], [x+1, y], [x, y-1], [x, y+1]:
        if 0 <= i < rows and 0 <= j < cols and grid[i][j] == 1:
          queue.append([i, j, res + 1])
          grid[i][j] = 0
                    
    if any(1 in row for row in grid):
      return -1
    else:
      return res

problem = Solution()
print(problem.orangesRotting([[2,1,1],[1,1,0],[0,1,1]]))
print(problem.orangesRotting([[2,1,1],[0,1,1],[1,0,1]]))
print(problem.orangesRotting([[0,2]]))
