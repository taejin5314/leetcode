from typing import List

class Solution:
  def maxProfit(self, prices: List[int]) -> int:
    res = 0

    for i in range(1, len(prices)):
      if prices[i] > prices[i-1]:
        res += (prices[i] - prices[i-1])
    return res

problem = Solution()
print(problem.maxProfit([7, 1, 5, 3, 6, 4]))
print(problem.maxProfit([1, 2, 3, 4, 5]))
print(problem.maxProfit([7, 6, 4, 3, 1]))