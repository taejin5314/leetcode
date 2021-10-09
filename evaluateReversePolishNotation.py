from typing import List

class Solution:
  def evalRPN(self, tokens: List[str]) -> int:
    for elm in tokens:
      if elm == '+':
        print(elm)
      elif elm == '-':
        print(elm)
      elif elm == '*':
        print(elm)
      elif elm == '/':
        print(elm)
      else:
        print(int(elm))
    

problem = Solution()
print(problem.evalRPN(["2","1","+","3","*"]))
print(problem.evalRPN(["4","13","5","/","+"]))
print(problem.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))