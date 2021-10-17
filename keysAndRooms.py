from typing import List
from collections import defaultdict

class Solution:
  def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
    visited = defaultdict(int, {0 : 1})
    stack = [0]
    count = 1

    while stack:
      keys = rooms[stack.pop()]
      for k in keys:
        if not visited[k]:
          stack.append(k)
          visited[k] = 1
          count += 1
    
    return count == len(rooms)

problem = Solution()
print(problem.canVisitAllRooms([[1],[2],[3],[]]))
print(problem.canVisitAllRooms([[1,3],[3,0,1],[2],[0]]))