from typing import List

# class TrieNode:
#   def __init__(self):
#     self.next = {}
#     self.end = False

#   def addWord(self, word):
#     curr = self

#     for elm in word:
#       if elm not in self.next:
#         curr.next[elm] = TrieNode()
#       curr = curr.next[elm]
#     curr.end = True

# class Solution:
#   def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
#     root = TrieNode()

#     for elm in words:
#       root.addWord(elm)

#     rows = len(board)
#     cols = len(board[0])
#     result = set()
#     visit = set()

#     def dfs(i, j, node, word):
#       if i < 0 or j < 0 or i == rows or j == cols or board[i][j] not in node.next or (i, j) in visit:
#         return
      
#       visit.add((i, j))
#       node = node.next[board[i][j]]
#       word += board[i][j]
#       if node.end:
#         result.add(word)

#       dfs(i+1, j, node, word)
#       dfs(i-1, j, node, word)
#       dfs(i, j+1, node, word)
#       dfs(i, j-1, node, word)
#       visit.remove((i, j))

#     for i in range(rows):
#       for j in range(cols):
#         dfs(i, j, root, "")
    
#     return list(result)
    
class Solution:
  def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
    return 0

problem = Solution()
print(problem.findWords([["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], ["oath","pea","eat","rain"]))
print(problem.findWords([["a","b"],["c","d"]], ["abcb"]))