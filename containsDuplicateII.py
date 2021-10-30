from typing import List

class Solution:
  def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
    print(nums)
    return 0

problem = Solution()
print(problem.containsNearbyDuplicate([1, 2, 3, 1], 3))
print(problem.containsNearbyDuplicate([1, 0, 1, 1], 1))
print(problem.containsNearbyDuplicate([1, 2, 3, 1, 2, 3], 2))