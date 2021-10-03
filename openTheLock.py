from typing import List

class Solution:
  def openLock(self, deadends: List[str], target: str) -> int:
    return 0

problem = Solution()
print(problem.openLock(["0201","0101","0102","1212","2002"], "0202"))
print(problem.openLock(["8888"], "0009"))
print(problem.openLock(["8887","8889","8878","8898","8788","8988","7888","9888"], "8888"))
print(problem.openLock(["0000"], "8888"))
