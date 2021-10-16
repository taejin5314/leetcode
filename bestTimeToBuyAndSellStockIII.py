from typing import List

class Solution:
  def maxProfit(self, prices: List[int]) -> int:
    if not prices:
      return 0
    
    result = [0 for _ in range(len(prices))]

    for transaction in range(1, 3):
      price = -prices[0]
      profit = 0

      for i in range(1, len(prices)):
        price = max(price, result[i] - prices[i])
        profit = max(profit, price + prices[i])
        result[i] = profit
    
    return profit

problem = Solution()
print(problem.maxProfit([3,3,5,0,0,3,1,4]))
print(problem.maxProfit([1,2,3,4,5]))
print(problem.maxProfit([7,6,4,3,1]))
print(problem.maxProfit([1]))