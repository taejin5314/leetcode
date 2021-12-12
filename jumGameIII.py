from typing import List

class Solution:
  def canReach(self, arr: List[int], start: int) -> bool:
    queue = [start]
    visited = [False] * len(arr)

    while queue:
      curr = queue[0]
      queue.pop(0)

      if arr[curr] == 0:
        return True

      visited[curr] = True
      right = curr + arr[curr]
      left = curr - arr[curr]

      if right < len(arr) and not visited[right]:
        queue.append(right)


      if left >= 0 and not visited[left]:
        queue.append(left)
    return False

problem = Solution()
print(problem.canReach([4, 2, 3, 0, 3, 1, 2], 5))
print(problem.canReach([4, 2, 3, 0, 3, 1, 2], 0))
print(problem.canReach([3, 0, 2, 1, 2], 2))