from typing import List

class Solution:
  def thirdMax(self, nums: List[int]) -> int:
    arr = []
    for i,c in enumerate(nums):
      if len(arr) < 3 and c not in arr:
        arr.append(c)
      else:
        if c not in arr and min(arr) < c:
          arr[arr.index(min(arr))] = c

    return min(arr) if len(arr) >= 3 else max(arr)

problem = Solution()
print(problem.thirdMax([2, 2, 3, 1]))