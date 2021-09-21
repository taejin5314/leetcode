from typing import List

class Solution:
  def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
    count, maximum = 1, 0
    for i in range(1, len(nums)):
      if nums[i] != nums[i-1]:
        count = 1
      else:
        count += 1
      maximum = max(maximum, count)
    return maximum

problem = Solution()
print(problem.findMaxConsecutiveOnes([1, 1, 0, 1, 1, 1]))