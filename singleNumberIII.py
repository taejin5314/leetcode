from typing import List
from collections import defaultdict

class Solution:
  def singleNumber(self, nums: List[int]) -> List[int]:
    map = defaultdict(int)

    for num in nums:
      if map[num] == 1:
        del map[num]
      else:
        map[num] += 1
    return map.keys()

problem = Solution()
print(problem.singleNumber([1, 2, 1, 3, 2, 5]))
print(problem.singleNumber([-1, 0]))
print(problem.singleNumber([0, 1]))