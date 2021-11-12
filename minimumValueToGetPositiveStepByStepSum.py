from typing import List

class Solution:
  def minStartValue(self, nums: List[int]) -> int:
    sum, temp = nums[0], nums[0]
    for i in nums[1:]:
      temp += i
      sum = min(sum, temp)
    
    return max(1-sum, 1)
problem = Solution()
print(problem.minStartValue([-3, 2, -3, 4, 2]))
print(problem.minStartValue([1, 2]))
print(problem.minStartValue([1, -2, -3]))