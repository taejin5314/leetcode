from typing import List
import copy

class Solution:
  def exist(self, board: List[List[str]], word: str) -> bool:
    rows = len(board)
    cols = len(board[0])

    def dfs(board, i, j, target):
      if i < 0 or i >= rows or j < 0 or j >= cols or target[0] != board[i][j]:
        return False

      boardCopy = copy.deepcopy(board)

      if boardCopy[i][j] == target[0]:
        boardCopy[i][j] = "#"
        target = target[1:]
      else:
        return

      if len(target) == 0:
        return True
        
      return dfs(boardCopy, i+1, j, target) or dfs(boardCopy, i-1, j, target) or dfs(boardCopy, i, j+1, target) or dfs(boardCopy, i, j-1, target)

    for i in range(rows):
      for j in range(cols):
        if board[i][j] == word[0]:
          res = dfs(board, i, j, word)

          if res:
            return True
    
    return False

problem = Solution()
print(problem.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED"))
print(problem.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "SEE"))
print(problem.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCB"))