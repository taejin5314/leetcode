class Solution:
  def fib(self, n: int) -> int:
    arr = [1 for i in range(n)]
        
    for i in range(2, n):
      arr[i] = arr[i - 2] + arr[i - 1]
        
    return arr[n-1]

problem = Solution()
print(problem.fib(3))