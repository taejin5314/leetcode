from typing import List

class Solution:
  def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
    count, maximum = 0, 0
    for i in range(len(nums)):
      if nums[i] != 1:
        count = 0
      else:
        count += 1
      maximum = max(maximum, count)
    return maximum

problem = Solution()
print(problem.findMaxConsecutiveOnes([1, 0, 1, 1, 0, 1]))