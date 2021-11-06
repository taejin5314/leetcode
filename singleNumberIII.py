from typing import List

class Solution:
  def singleNumber(self, nums: List[int]) -> List[int]:
    print(nums)

problem = Solution()
print(problem.singleNumber([1, 2, 1, 3, 2, 5]))
print(problem.singleNumber([-1, 0]))
print(problem.singleNumber([0, 1]))