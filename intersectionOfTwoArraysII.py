from typing import List

class Solution:
  def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
    print(nums1, nums2)

problem = Solution()
print(problem.intersect([1,2,2,1], [2,2]))
print(problem.intersect([4,9,5], [9,4,9,8,4]))