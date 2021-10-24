from typing import List

class Solution:
  def findMin(self, nums: List[int]) -> int:
    lo, hi = 0, len(nums) - 1

    while lo < hi:
      mid = (lo + hi) // 2

      if nums[mid] > nums[hi]:
        lo = mid + 1
      else:
        hi = mid if nums[hi] != nums[mid] else hi - 1

    return nums[lo]

problem = Solution()
print(problem.findMin([1, 3, 5]))
print(problem.findMin([2, 2, 2, 0, 1]))
        