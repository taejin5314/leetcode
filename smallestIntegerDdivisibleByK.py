class Solution:
  def smallestRepunitDivByK(self, k: int) -> int:
    if not k % 2 or not k % 5:
      return -1
    n = length = 1
    while True:
      if not n % k:
        return length
      length += 1
      n = 10 * n + 1

problem = Solution()
print(problem.smallestRepunitDivByK(1))
print(problem.smallestRepunitDivByK(2))
print(problem.smallestRepunitDivByK(3))