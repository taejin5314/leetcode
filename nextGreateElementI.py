from typing import List

class Solution:
  def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
    hashMap = dict()
    stack = []
    result = []

    for num in nums2:
      while stack and stack[-1] < num:
        hashMap[stack[-1]] = num
        stack.pop()
      stack.append(num)

    for num in stack:
      hashMap[num] = -1

    for num in nums1:
      result.append(hashMap[num])

    return result

problem = Solution()
print(problem.nextGreaterElement([4,1,2], [1,3,4,2]))
print(problem.nextGreaterElement([2,4], [1,2,3,4]))
print(problem.nextGreaterElement([1, 3, 5, 2, 4], [6, 5, 4, 3, 2, 1, 7]))