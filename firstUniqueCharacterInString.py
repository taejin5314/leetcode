class Solution:
  def firstUniqChar(self, s: str) -> int:
    map = {}

    for i, c in enumerate(s):
      if c not in map:
        map[c] = [1, i]
      else:
        map[c][0] += 1
    
    for c in map:
      if map[c][0] == 1:
        return map[c][1]

    return -1

problem = Solution()
print(problem.firstUniqChar('leetcode'))
print(problem.firstUniqChar('loveleetcode'))
print(problem.firstUniqChar('aabb'))