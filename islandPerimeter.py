from typing import List

class Solution:
  def islandPerimeter(self, grid: List[List[int]]) -> int:
    rows = len(grid)
    cols = len(grid[0])
    perimeter = 0

    for i in range(rows):
      for j in range(cols):
        if grid[i][j] == 1:
          perimeter += 4

          if i and grid[i-1][j]:
            perimeter -= 2
          if j and grid[i][j-1]:
            perimeter -= 2
    
    return perimeter

problem = Solution()
print(problem.islandPerimeter([[1, 1], [1, 1]]))