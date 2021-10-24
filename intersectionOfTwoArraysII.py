from typing import List

class Solution:
  def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
    map = {}
    res = []

    for num in nums1:
      map[num] = map.get(num, 0) + 1

    for num in nums2:
      if num in map and map[num] > 0:
        res.append(num)
        map[num] -= 1
    
    return res

problem = Solution()
print(problem.intersect([1,2,2,1], [2,2]))
print(problem.intersect([4,9,5], [9,4,9,8,4]))