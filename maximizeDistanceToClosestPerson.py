from typing import List

class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        m, temp, first = 0, 0, None
        for s in seats:
            if s == 1:
                if first == None:
                    first = temp
                m, temp = max(m,temp), 0
            temp += 1
			
        return max(first, m//2, temp-1)

problem = Solution()
print(problem.maxDistToClosest([1,0,0,0,1,0,1]))