class Solution:
  def tribonacci(self, n: int) -> int:
    if n == 0:
      return 0
    elif n == 1:
      return 1
    elif n == 2:
      return 1
    else:
      prevPrevPrev, prevPrev, prev = 0, 1, 1
      for i in range(3, n+1):
        cur = prev + prevPrev + prevPrevPrev
        prevPrevPrev = prevPrev
        prevPrev = prev
        prev = cur
      return cur

problem = Solution()
print(problem.tribonacci(4))
print(problem.tribonacci(25))