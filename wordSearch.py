from typing import List
import copy

class Solution:
  def exist(self, board: List[List[str]], word: str) -> bool:
    rows = len(board)
    cols = len(board[0])

    for i in range(rows):
      for j in range(cols):
        if board[i][j] == word[0]:
          if self.dfs(board, i, j, word):
            return True
    
    return False
  
  def dfs(self, board, i, j, word):
    if len(word) == 0:
      return True
    if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or word[0] != board[i][j]:
      return False

    tmp = board[i][j]
    board[i][j] = '#'
      
    res = self.dfs(board, i+1, j, word[1:]) or self.dfs(board, i-1, j, word[1:]) or self.dfs(board, i, j+1, word[1:]) or self.dfs(board, i, j-1, word[1:])
    board[i][j] = tmp

    return res

problem = Solution()
print(problem.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED"))
print(problem.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "SEE"))
print(problem.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCB"))

print(problem.exist([["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"]], "AAAAAAAAAAAAAAB"))