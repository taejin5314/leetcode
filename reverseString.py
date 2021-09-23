from typing import List

class Solution:
  def reverseString(self, s: List[str]) -> None:
    if len(s) < 2:
      return s
    s = self.reverseString(s[len(s)//2:]) + self.reverseString(s[:len(s)//2])
    return s

problem = Solution()
print(problem.reverseString(["h","e","l","l","o"]))