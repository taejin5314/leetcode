from typing import List

class Solution:
  def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
    for i in range(len(words)):
      for elm in words[i]:
        print(elm)
    

problem = Solution()
print(problem.findWords([["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], ["oath","pea","eat","rain"]))
print(problem.findWords([["a","b"],["c","d"]], ["abcb"]))