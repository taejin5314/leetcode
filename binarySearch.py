from typing import List

class Solution:
  def search(self, nums: List[int], target: int) -> int:
    left, right = 0, len(nums) - 1
    while left <= right:
      mid = (left + right) // 2
      if nums[mid] == target:
        return mid
      elif nums[mid] < target:
        left = mid + 1
      elif nums[mid] > target:
        right = mid -1
    return -1

problem = Solution()
print(problem.search([-1,0,3,5,9,12], 9))
print(problem.search([-1,0,3,5,9,12], 2))