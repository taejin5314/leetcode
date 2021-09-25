from typing import List

class Solution:
  def rotate(self, nums: List[int], k: int) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    n = len(nums)
    k = k % n
    nums[:] = nums[n-k:] + nums[:n-k]
    return nums

problem = Solution()
print(problem.rotate([1, 2, 3, 4, 5, 6, 7], 3))
print(problem.rotate([-1, -100, 3, 99], 2))
        