from typing import List

class Solution:
  def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
    rows = len(image)
    cols = len(image[0])
    originalColor = image[sr][sc]

    def dfs(r, c):
      if r < 0 or c < 0 or r > rows - 1 or c > cols - 1 or image[r][c] == newColor or image[r][c] != originalColor:
        return
      image[r][c] = newColor

      dfs(r + 1, c)
      dfs(r - 1, c)
      dfs(r, c + 1) 
      dfs(r, c - 1)
    dfs(sr, sc)

    return image

problem = Solution()
print(problem.floodFill([[1, 1, 1], [1, 1, 0], [1, 0, 1]], 1, 1, 2))
print(problem.floodFill([[0, 0, 0], [0, 0, 0]], 0, 0, 2))