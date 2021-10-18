from typing import List

class Solution:
  def singleNumber(self, nums: List[int]) -> int:
    hashSet = set()

    for num in nums:
      if num in hashSet:
        hashSet.remove(num)
      else:
        hashSet.add(num)

    return hashSet.pop()


problem = Solution()
print(problem.singleNumber([2, 2, 1]))
print(problem.singleNumber([4, 1, 2, 1, 2]))
print(problem.singleNumber([1]))