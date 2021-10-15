from typing import List

class Solution:
  def maxProfit(self, prices: List[int]) -> int:
    result = {}
  
    def dfs(index, buying):
      if index >= len(prices):
        return 0
      if (index, buying) in result:
        return result[(index, buying)]
      
      cooldown = dfs(index + 1, buying)
      if buying:
        buy = dfs(index + 1, not buying) - prices[index]
        result[(index, buying)] = max(buy, cooldown)
      else:
        sell = dfs(index + 2, not buying) + prices[index]
        result[(index, buying)] = max(sell, cooldown)
      return result[(index, buying)]
  
    return dfs(0, True)


problem = Solution()
print(problem.maxProfit([1, 2, 3, 0, 2]))
print(problem.maxProfit([1]))