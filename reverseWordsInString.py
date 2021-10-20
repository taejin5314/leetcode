from typing import List

class Solution:
  def reverseWords(self, s: str) -> str:
    arr = []
    for word in s.split():
      arr.insert(0, word)

    return ' '.join(arr)

problem = Solution()
print(problem.reverseWords("the sky is blue"))
print(problem.reverseWords("  hello world  "))
print(problem.reverseWords("a good     example"))
print(problem.reverseWords("  Bob     Loves  Alice   "))
print(problem.reverseWords("Alice does not even like bob"))