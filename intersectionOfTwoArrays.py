from typing import List

class Solution:
  def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
    result = []

    hashSet = set(nums1)

    for num in set(nums2):
      if num in hashSet:
        result.append(num)
    
    return result

problem = Solution()
print(problem.intersection([1, 2, 2, 1], [2, 2]))
print(problem.intersection([4, 9 ,5], [9, 4, 9, 8, 4]))