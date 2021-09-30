from typing import List

class Solution:
  def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
    if sum(nums) % k == 0:
      targetSum = sum(nums) // k
    else:
      return False
    
    def divideInSubset(nums, n, targetSum):
      if targetSum == 0:
        return True
      if n == 0 and targetSum != 0:
        return False

      if nums[n-1] > targetSum:
        return divideInSubset(nums, n-1, targetSum)

      return divideInSubset(nums, n-1, targetSum) or divideInSubset(nums, n-1, targetSum - nums[n-1])

    return divideInSubset(nums, len(nums), targetSum)


problem = Solution()
print(problem.canPartitionKSubsets([4,3,2,3,5,2,1], 4))
print(problem.canPartitionKSubsets([1,2,3,4], 3))
print(problem.canPartitionKSubsets([2,2,2,2,3,4,5], 4))