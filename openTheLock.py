from collections import defaultdict
import collections
from typing import DefaultDict, List

class Solution:
  def openLock(self, deadends: List[str], target: str) -> int:
    nums = []
    deadends = set(deadends)

    for i in range(10000):
      cand = '0000' + str(i)
      nums.append(cand[-4:])

    adjList = defaultdict(list)
    
    for cand in nums:
      for i in range(4):
        for digit in [((int(cand[i]) + 1) % 10), ((int(cand[i]) - 1) % 10)]:
          nx = cand[:i] + str(digit) + cand[i+1:]
          if nx not in deadends:
            adjList[cand].append(nx)

    if "0000" in deadends:
      return -1

    q = collections.deque([("0000", 0)])
    visited = set()
    while q:
      cand, steps = q.popleft()

      if cand == target:
        return steps
      for nx in adjList[cand]:
        if nx not in visited:
          visited.add(nx)
          q.append((nx, steps+1))
    return -1

problem = Solution()
print(problem.openLock(["0201","0101","0102","1212","2002"], "0202"))
print(problem.openLock(["8888"], "0009"))
print(problem.openLock(["8887","8889","8878","8898","8788","8988","7888","9888"], "8888"))
print(problem.openLock(["0000"], "8888"))
