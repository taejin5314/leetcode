from typing import List

class Solution:
    def heightChecker(self, heights: List[int]) -> int:
      heightsCopy = heights.copy();
      heights.sort()
      count = 0

      for i in range(len(heights)):
        if heightsCopy[i] != heights[i]:
          count += 1
      return count

problem = Solution()
print(problem.heightChecker([1, 1, 4, 2, 1, 3]))
print(problem.heightChecker([5, 1, 2, 3, 4]))
print(problem.heightChecker([1, 2, 3, 4, 5]))