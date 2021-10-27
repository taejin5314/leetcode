from typing import List

class Solution:
  def sortColors(self, nums: List[int]) -> None:
    left, right = 0, len(nums) - 1
    i = 0

    while i <= right:
      if nums[i] == 0:
        nums[left], nums[i] = nums[i], nums[left]
        left += 1
      elif nums[i] == 2:
        nums[right], nums[i] = nums[i], nums[right]
        i -= 1
        right -= 1
      
      i += 1

    return nums

problem = Solution()
print(problem.sortColors([2, 0, 2, 1, 1, 0]))
print(problem.sortColors([2, 0, 1]))
print(problem.sortColors([0]))
print(problem.sortColors([1]))