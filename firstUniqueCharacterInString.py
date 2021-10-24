class Solution:
  def firstUniqChar(self, s: str) -> int:
    map = {}

    for c in s:
      if c not in map:
        map[c] = 1
      else:
        map[c] += 1
    
    return map

problem = Solution()
print(problem.firstUniqChar('leetcode'))
print(problem.firstUniqChar('loveleetcode'))
print(problem.firstUniqChar('aabb'))