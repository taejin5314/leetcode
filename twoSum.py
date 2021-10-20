from typing import List

class Solution:
  def twoSum(self, nums: List[int], target: int) -> List[int]:
    hashMap = {}

    for i, num in enumerate(nums):
      if target - num in hashMap:
        return [hashMap[target - num][0], i]
      if num not in hashMap:
        hashMap[num] = [i]

problem = Solution()
print(problem.twoSum([2, 7, 11, 15], 9))
print(problem.twoSum([3, 2, 4], 6))
print(problem.twoSum([3, 3], 6))