from typing import List

class Solution:
  def largestRectangleArea(self, heights: List[int]) -> int:
    st, res = [], 0
    for bar in heights + [-1]:
      step = 0
      while st and st[-1][1] >= bar:
        w, h = st.pop()
        step += w
        res = max(res, step * h)

      st.append((step + 1, bar))

    return res

problem = Solution()
print(problem.largestRectangleArea([2,1,5,6,2,3]))