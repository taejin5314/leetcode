from typing import List

class Solution:
  def containsDuplicate(self, nums: List[int]) -> bool:
    map = {}

    for num in nums:
      if num not in map:
        map[num] = 1
      else:
        return True
    
    return False
    
problem = Solution()
print(problem.containsDuplicate([1, 2, 3, 1]))
print(problem.containsDuplicate([1, 2, 3, 4]))
print(problem.containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))