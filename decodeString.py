class Solution:
  def decodeString(self, s: str) -> str:
    for elm in s:
      print(elm)

problem = Solution()
print(problem.decodeString("3[a]2[bc]"))
print(problem.decodeString("3[a2[c]]"))
print(problem.decodeString("2[abc]3[cd]ef"))
print(problem.decodeString("abc3[cd]xyz"))