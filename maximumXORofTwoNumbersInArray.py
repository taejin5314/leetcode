class Solution:
  def findMaximumXOR(self, nums: List[int]) -> int:
    max_bin_len = len(bin(max(nums))) - 2  
    max_xor = 0
    for prefix_len in range(1, max_bin_len + 1):
      max_xor <<= 1
      cur_xor = max_xor | 1
      shift = max_bin_len - prefix_len
      prefixes = {n >> shift for n in nums}
      found_match = any(cur_xor ^ prefix in prefixes for prefix in prefixes)
      max_xor |= found_match
    return max_xor