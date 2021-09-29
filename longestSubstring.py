class Solution:
  def lengthOfLongestSubstring(self, s: str) -> int:
    return len(set(list(s)))

problem = Solution()
print(problem.lengthOfLongestSubstring("abcabcbb"))
print(problem.lengthOfLongestSubstring("bbbbb"))
print(problem.lengthOfLongestSubstring("pwwkew"))
print(problem.lengthOfLongestSubstring(""))