from typing import List

class Solution:
  def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
    sums = collections.Counter(c+d for c in nums3 for d in nums4)
    return sum(sums.get(-(a+b), 0) for a in nums1 for b in nums2)