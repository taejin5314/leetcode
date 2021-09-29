from typing import List

class Solution:
  def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
    
    image[sr][sc] = newColor
    return 0

problem = Solution()
print(problem.floodFill([[1, 1, 1], [1, 1, 0], [1, 0, 1]], 1, 1, 2))
print(problem.floodFill([[0, 0, 0], [0, 0, 0]], 0, 0, 2))