class Solution:
  def numSquares(self, n: int) -> int:
    i, k, squares = 1, 1, []

    while k <= n:
      squares.append(k)
      i += 1
      k = i ** 2

    dp = [n for _ in range(n+1)]

    for square in squares:
      for i in range(1, n+1):
        if square <= i:
          if i % square == 0:
            candidate = i // square
            dp[i] = min(candidate, dp[i])
          else:
            dp[i] = min(dp[i], 1 + dp[i - square])

    return dp[n]

problem = Solution()
print(problem.numSquares(12))
print(problem.numSquares(13))