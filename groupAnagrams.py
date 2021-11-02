from typing import List

class Solution:
  def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    return strs

problem = Solution()
print(problem.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
print(problem.groupAnagrams([""]))
print(problem.groupAnagrams(["a"]))