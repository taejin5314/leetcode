class Solution:
  def isHappy(self, n: int) -> bool:
    def dfs(map, n):
      if n == 1:
        return True
      if n in map:
        return False

      res = 0
      map.append(n)

      for num in str(n):
        res += int(num) ** 2
    
      return dfs(map, res)
    
    return dfs([], n)

problem = Solution()
print(problem.isHappy(19))
print(problem.isHappy(2))