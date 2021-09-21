from typing import List

class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        for i in nums:
            if i % 2 == 0:
                nums.remove(i)
                nums.insert(0, i)
        return nums

problem = Solution()
print(problem.sortArrayByParity([3, 2, 4, 1]))