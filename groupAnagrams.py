from typing import  List
from collections import defaultdict

class Solution:
  def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    map = defaultdict(list)

    for str in strs:
      sortedStr = ''.join(sorted(str))
      map[sortedStr].append(str)

    return map.values()

problem = Solution()
print(problem.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
print(problem.groupAnagrams([""]))
print(problem.groupAnagrams(["a"]))