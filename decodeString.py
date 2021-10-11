class Solution:
  def decodeString(self, s: str) -> str:
    stack = []
    for i, elm in enumerate(s):
      if elm != ']':
        stack.append(elm)
      else:
        substring = ""
        while stack[-1] != "[":
          substring = stack.pop() + substring
        stack.pop()

        repeat = ""
        while stack and stack[-1].isdigit():
          repeat = stack.pop() + repeat
        stack.append(int(repeat) * substring)

    return "".join(stack)

problem = Solution()
print(problem.decodeString("3[a]2[bc]"))
print(problem.decodeString("3[a2[c]]"))
print(problem.decodeString("2[abc]3[cd]ef"))
print(problem.decodeString("abc3[cd]xyz"))