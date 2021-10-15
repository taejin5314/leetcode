from typing import List

class Solution:
  def maxProfit(self, prices: List[int]) -> int:
    obj = {}

    def dfs(index, buying):
      if index >= len(prices):
        return 0
      if (index, buying) in obj:
        return obj[(index, buying)]

      cooldown = dfs(index + 1, buying)
      if buying:
        buy = dfs(index + 1, not buying) - prices[index]
        obj[(index, buying)] = max(buy, cooldown)
      else:
        sell = dfs(index + 2, not buying) + prices[index]
        obj[(index, buying)] = max(sell, cooldown)
      
      return obj[(index, buying)]
    
    return dfs(0, True)


problem = Solution()
print(problem.maxProfit([1, 2, 3, 0, 2]))
print(problem.maxProfit([1]))