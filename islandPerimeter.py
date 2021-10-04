from typing import List

class Solution:
  def islandPerimeter(self, grid: List[List[int]]) -> int:
    rows = len(grid)
    cols = len(grid[0])
    perimeter = 0

    def bfs(grid, i, j):
      nonlocal perimeter
      if i < 0 or i >= rows or j < 0 or j >= cols or grid[i][j] == 0:
        return

      grid[i][j] = 0

      perimeter += 3

      if i < rows - 1:
        if grid[i+1][j] == 1:
          perimeter -= 1
      if i > 0:
        if grid[i-1][j] == 1:
          perimeter -= 1

      if j < cols - 1:
        if grid[i][j+1] == 1:
          perimeter -= 1
      if j > 0:
        if grid[i][j-1] == 1:
          perimeter -= 1

      bfs(grid, i+1, j)
      bfs(grid, i-1, j)
      bfs(grid, i, j+1)
      bfs(grid, i, j-1)

    for i in range(rows):
      for j in range(cols):
        if grid[i][j] == 1:
          bfs(grid, i, j)
    
    return perimeter

problem = Solution()
print(problem.islandPerimeter([[1, 1], [1, 1]]))