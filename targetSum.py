from typing import DefaultDict, List

class Solution:
  def findTargetSumWays(self, nums: List[int], target: int) -> int:
    dic = {}

    def dfs(index, total):
      key = (index, total)

      if key not in dic:
        if index == len(nums):
          return total == target
        else:
          dic[key] = dfs(index+1, total + nums[index]) + dfs(index+1, total - nums[index])

      return dic[key]

    return dfs(0, 0)

problem = Solution()
print(problem.findTargetSumWays([1,1,1,1,1], 3))
print(problem.findTargetSumWays([1], 1))
print(problem.findTargetSumWays([11,19,14,50,47,35,18,32,8,2,31,45,6,25,49,23,25,33,24,33], 44))