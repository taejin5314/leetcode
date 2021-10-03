from typing import List

class Solution:
  def canJump(self, nums: List[int]) -> bool:
    lastGoodIndex = len(nums) - 1

    for i in range(len(nums) - 1, -1, -1):
      if nums[i] + lastGoodIndex >= lastGoodIndex:
        lastGoodIndex = i

    return lastGoodIndex == 0

problem = Solution()
print(problem.canJump([2, 3, 1, 1, 4]))
print(problem.canJump([3, 2, 1, 0, 4]))