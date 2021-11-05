import math

class Solution:
  def arrangeCoins(self, n: int) -> int:
    return int((math.sqrt(8*n+1)-1)/2)

problem = Solution()
print(problem.arrangeCoins(5))
print(problem.arrangeCoins(8))