class Solution:
  def fib(self, n: int) -> int:
    arr = [1 for i in range(n + 1)]
    arr[0] = 0
        
    for i in range(2, n + 1):
      arr[i] = arr[i - 2] + arr[i - 1]
        
    return arr[n]

problem = Solution()
print(problem.fib(0))
print(problem.fib(1))
print(problem.fib(2))
print(problem.fib(3))
print(problem.fib(4))
print(problem.fib(5))
print(problem.fib(6))
print(problem.fib(7))