class Solution:
  def isPowerOfTwo(self, n: int) -> bool:
    return n > 0 and n & n - 1 == 0

problem = Solution()
print(problem.isPowerOfTwo(1))
print(problem.isPowerOfTwo(16))
print(problem.isPowerOfTwo(3))