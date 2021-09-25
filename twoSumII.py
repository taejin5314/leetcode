from typing import List

class Solution:
  def twoSum(self, numbers: List[int], target: int) -> List[int]:
    left, right = 0, len(numbers) - 1
    while left <= right:
      if numbers[left] + numbers[right] > target:
        right -= 1
      elif numbers[left] + numbers[right] < target:
        left += 1
      else:
        return [left + 1, right + 1]

problem = Solution()
print(problem.twoSum([2, 7, 11, 15], 9))
print(problem.twoSum([2, 3, 4], 6))
print(problem.twoSum([-1, 0], -1))