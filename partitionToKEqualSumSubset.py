from typing import List

class Solution:
  def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
    if sum(nums) % k == 0:
      targetSum = sum(nums) // k
    else:
      return False

    used = [False for _ in range(len(nums))]
    
    def divideInSubset(t, k, index):
      if k == 0:
        return True
      if t == 0:
        return divideInSubset(targetSum, k - 1, 0)
      else:
        for i in range(index, len(nums)):
          if not used[i] and t - nums[i] >= 0:
            used[i] = True

            if divideInSubset(t - nums[i], k, i + 1):
              return True
            
            used[i] = False


    return True if divideInSubset(targetSum, k, 0) else False


problem = Solution()
print(problem.canPartitionKSubsets([4,3,2,3,5,2,1], 4))
print(problem.canPartitionKSubsets([1,2,3,4], 3))
print(problem.canPartitionKSubsets([2,2,2,2,3,4,5], 4))