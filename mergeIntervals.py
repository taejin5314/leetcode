from typing import List

class Solution:
  def merge(self, intervals: List[List[int]]) -> List[List[int]]:
    intervals.sort(key=lambda item: item[0])
    res = []
    no_more_merge = False

    while not no_more_merge:
      res = []
      i = 0
      no_more_merge = True
      while i < len(intervals):
        if i != len(intervals) - 1 and intervals[i][1] >= intervals[i+1][0]:
          new = [intervals[i][0], max(intervals[i+1][1], intervals[i][1])]
          res.append(new)
          i += 2
          no_more_merge = False
        else:
          res.append(intervals[i])
          i += 1
      intervals = res
    return res

problem = Solution()
print(problem.merge([[1,3], [2,6], [8,10], [15,18]]))