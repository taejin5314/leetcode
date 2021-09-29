class Solution:
  def lengthOfLongestSubstring(self, s: str) -> int:
    if len(s) < 1:
      return 0
    map = {}
    left, right = 0, 0
    longest = 1

    while right < len(s):
      if s[right] in map:
        left = max(left, map[s[right]] + 1)
      longest = max(longest, right - left + 1)
      map[s[right]] = right
      right += 1
    return longest

problem = Solution()
print(problem.lengthOfLongestSubstring("abcabcbb"))
print(problem.lengthOfLongestSubstring("bbbbb"))
print(problem.lengthOfLongestSubstring("pwwkew"))
print(problem.lengthOfLongestSubstring(""))
print(problem.lengthOfLongestSubstring("abba"))