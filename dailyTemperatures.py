from typing import List

class Solution:
  def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
    ans = [0 for _ in range(len(temperatures))]
    stack = []

    for i, t in enumerate(temperatures):
      while stack and t > stack[-1][0]:
        stackT, stackInd = stack.pop()
        ans[stackInd] = (i - stackInd)

      stack.append([t, i])

    return ans

problem = Solution()
print(problem.dailyTemperatures([73,74,75,71,69,72,76,73]))
print(problem.dailyTemperatures([30,40,50,60]))
print(problem.dailyTemperatures([30,60,90]))