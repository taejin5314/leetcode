from typing import List

class Solution:
  def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
    hashMap = dict()
    stack = []
    result = []

    for num in nums2:
      if stack and stack[-1] < num:
        hashMap[stack.pop()] = num
      stack.append(num)

    for num in nums1:
      if num in hashMap:
        result.append(hashMap[num])
      else:
        result.append(-1)

    return result

problem = Solution()
print(problem.nextGreaterElement([4,1,2], [1,3,4,2]))
print(problem.nextGreaterElement([2,4], [1,2,3,4]))