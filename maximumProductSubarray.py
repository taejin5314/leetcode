from typing import List

class Solution:
  def maxProduct(self, nums: List[int]) -> int:
    prev_max = nums[0]
    prev_min = nums[0]
    max_to_n = nums[0]
    min_to_n = nums[0]
    ans = nums[0]

    for i in nums[1:]:
      max_to_n = max(max(prev_max*i, prev_min*i), i)
      min_to_n = min(min(prev_max*i, prev_min*i), i)
      prev_max = max_to_n
      prev_min = min_to_n
      ans = max(ans, max_to_n)
    return ans

problem = Solution()
print(problem.maxProduct([2, 3, -2, 4]))
print(problem.maxProduct([-2, 0, -1]))