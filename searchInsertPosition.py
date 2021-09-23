from typing import List

class Solution:
  def searchInsert(self, nums: List[int], target: int) -> int:
    left, right = 0, len(nums) - 1
    while left <= right:
      mid = (left + right) // 2
      if nums[mid] > target:
        if (mid > 0 and nums[mid - 1] < target) or mid == 0:
          return mid
        right = mid - 1
      elif nums[mid] < target:
        if (mid < len(nums) - 1 and nums[mid + 1] > target) or mid == len(nums) - 1:
          return mid + 1
        left = mid + 1 
      else:
        return mid

problem = Solution()
print(problem.searchInsert([1, 3, 5, 6], 5))
print(problem.searchInsert([1, 3, 5, 6], 2))
print(problem.searchInsert([1, 3, 5, 6], 7))
print(problem.searchInsert([1, 3, 5, 6], 0))
print(problem.searchInsert([1], 0))