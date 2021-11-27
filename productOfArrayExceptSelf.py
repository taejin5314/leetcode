from typing import List

class Solution:
  def productExceptSelf(self, nums: List[int]) -> List[int]:
    answer = 1
    n = len(nums)
    res = []

    for i in range(n):
      res.append(answer)
      answer *= nums[i]
    answer = 1
    for i in range(n-1, -1, -1):
      res[i] = res[i] * answer
      answer *= nums[i]
    return res

problem = Solution()
print(problem.productExceptSelf([1,2,3,4]))
print(problem.productExceptSelf([-1,-1,0,-3,-3]))