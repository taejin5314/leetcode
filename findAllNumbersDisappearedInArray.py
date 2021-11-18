from typing import List

class Solution:
  def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
    res = []
    for i in range(1, len(nums)+1):
      if i not in nums:
        res.append(i)
    return res

problem = Solution()
print(problem.findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1]))
print(problem.findDisappearedNumbers([1, 1]))