# Recursion

# class Solution:
#   def longestCommonSubsequence(self, text1: str, text2: str) -> int:
#     if len(text1) == 0 or len(text2) == 0:
#       return 0
#     elif text1[len(text1) - 1] == text2[len(text2) - 1]:
#       return 1 + self.longestCommonSubsequence(text1[0:-1], text2[0:-1])
#     else:
#       return max(self.longestCommonSubsequence(text1, text2[0:-1]), self.longestCommonSubsequence(text1[0:-1], text2))

# Memoization

class Solution:
  def longestCommonSubsequence(self, text1: str, text2: str) -> int:
    t1Length = len(text1)
    t2Length = len(text2)

    table = [[None] * (t2Length + 1) for _ in range(t1Length + 1)]

    for i in range(t1Length + 1):
      for j in range(t2Length + 1):
        if i == 0 or j == 0:
          table[i][j] = 0
        elif text1[i - 1] == text2[j - 1]:
          table[i][j] = table[i-1][j-1] + 1
        else:
          table[i][j] = max(table[i-1][j], table[i][j-1])
    
    return table[t1Length][t2Length]


problem = Solution()
print(problem.longestCommonSubsequence('abcde', 'ace'))
print(problem.longestCommonSubsequence('abc', 'abc'))
print(problem.longestCommonSubsequence('abc', 'def'))