from typing import List

class Solution:
  def rob(self, nums: List[int]) -> int:
    max_3_before, max_2_before, adjacent = 0, 0, 0
    for cur in nums:
      max_3_before, max_2_before, adjacent = max_2_before, adjacent, max(max_3_before + cur, max_2_before + cur)
    return max(max_2_before, adjacent)

problem = Solution()
print(problem.rob([1,2,3,1]))
print(problem.rob([2,7,9,3,1]))