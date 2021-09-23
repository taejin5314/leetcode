from typing import List

class Solution:
  def sortedSquares(self, nums: List[int]) -> List[int]:
    return sorted([num*num for num in nums])

problem = Solution()
print(problem.sortedSquares([-4,-1,0,3,10]))
print(problem.sortedSquares([-7,-3,2,3,11]))