from typing import List

class Solution:
  def numIslands(self, grid: List[List[str]]) -> int:
    rows = len(grid)
    cols = len(grid[0])
    count = 0

    def bfs(grid, i ,j):
      if i < 0 or i >= rows or j < 0 or j >= cols or grid[i][j] == '0':
        return 

      grid[i][j] = '0'
      bfs(grid, i + 1, j)
      bfs(grid, i - 1, j)
      bfs(grid, i, j + 1)
      bfs(grid, i, j - 1)

    for i in range(rows):
      for j in range(cols):
        if grid[i][j] == '1':
          count += 1
          bfs(grid, i, j)

    return count

problem = Solution()
print(problem.numIslands([
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]))
print(problem.numIslands([
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]))