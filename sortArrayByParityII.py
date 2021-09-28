from typing import List

class Solution:
  def sortArrayByParityII(self, nums: List[int]) -> List[int]:
    result = [None for _ in range(len(nums))]
    even, odd = 0, 1

    for i in range(len(nums)):
      if (nums[i] % 2 == 0):
        result[even] = nums[i]
        even += 2
      if (nums[i] % 2 == 1):
        result[odd] = nums[i]
        odd += 2
    return result

problem = Solution()
print(problem.sortArrayByParityII([4, 2, 5, 7]))