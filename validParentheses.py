class Solution:
  def isValid(self, s: str) -> bool:
    return 0

problem = Solution()
print(problem.isValid("()"))
print(problem.isValid("()[]{}"))
print(problem.isValid("(]"))
print(problem.isValid("([)]"))
print(problem.isValid("{[]}"))