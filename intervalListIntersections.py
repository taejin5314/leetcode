from typing import List

class Solution:
  def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
    combined = sorted(firstList + secondList, key=itemgetter(0))
    intersection = []
    currentEnd = -1

    for start, end in combined:
      if start <= currentEnd:
        intersection.append([start, min(currentEnd, end)])
      currentEnd = max(currentEnd, end)        

    return intersection
problem = Solution()
print(problem.intervalIntersection([[0,2],[5,10],[13,23],[24,25]], [[1,5],[8,12],[15,24],[25,26]]))