from typing import List
from collections import deque

class Solution:
  def shortestPath(self, grid: List[List[int]], k: int) -> int:
    rows, cols = len(grid) - 1, len(grid[0]) - 1
    queue = deque([[0, 0, 0]]) # row, col, k
    path = {(0, 0): 0}
    steps = 0

    while queue:
      for _ in range(len(queue)):
        [i, j, obs] = queue.popleft()
        if obs > k:
          continue
        if i == rows and j == cols:
          return steps
        for [i2, j2] in [[i+1, j], [i-1, j], [i, j+1], [i, j - 1]]:
          if 0 <= i2 <= rows and 0 <= j2 <= cols:
            next_obs = obs + 1 if grid[i2][j2] == 1 else obs
            if next_obs < path.get((i2, j2), float('inf')):
              path[(i2, j2)] = next_obs
              queue.append([i2, j2, next_obs])
      steps += 1
    return -1

problem = Solution()
print(problem.shortestPath([[0,0,0],
 [1,1,0],
 [0,0,0],
 [0,1,1],
 [0,0,0]], 1))
print(problem.shortestPath([[0,1,1],
 [1,1,1],
 [1,0,0]], 1))