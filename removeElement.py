from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
      arrCopy = nums.copy()
      for i in arrCopy:
        if i == val:
          nums.remove(i)
      return nums

problem = Solution()
print(problem.removeElement([3,2,2,3], 2))