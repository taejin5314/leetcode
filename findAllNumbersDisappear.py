from typing import List

class Solution:
  def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
    map = {}
    for i, c in enumerate(nums):
      map[c] = 1
      if i+1 not in map.keys():
        map[i+1] = 0
    return [arr for arr in map.keys() if map[arr] == 0]

problem = Solution()
print(problem.findDisappearedNumbers([4,3,2,7,8,2,3,1]))
print(problem.findDisappearedNumbers([1,1]))