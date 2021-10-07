from typing import List

class Solution:
  def exist(self, board: List[List[str]], word: str) -> bool:
    rows = len(board)
    cols = len(board[0])

    def dfs(board, i, j, target):
      target = target[1:]
      print(target)

    for i in range(rows):
      for j in range(cols):
        if board[i][j] == word[0]:
          dfs(board, i, j, word)

problem = Solution()
print(problem.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED"))
print(problem.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "SEE"))
print(problem.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCB"))