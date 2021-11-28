from typing import List

class Solution:
  def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
    result = []
    temp = []

    def dfs(node):
      if node == len(graph) - 1:
        result.append(temp.copy())
        return

      for i in graph[node]:
        temp.append(i)
        dfs(i)
        temp.pop()
    
    temp.append(0)
    dfs(0)
    return result

problem = Solution()
print(problem.allPathsSourceTarget([[1,2], [3], [3], []]))
print(problem.allPathsSourceTarget([[4,3,1],[3,2,4],[3],[4],[]]))
print(problem.allPathsSourceTarget([[1],[]]))