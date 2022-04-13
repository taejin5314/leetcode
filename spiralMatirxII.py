class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        top, bottom, left, right, element = 0, n, 0, n, 1
        spiral = [[None for _ in range(n)] for _ in range(n)]
        while top < bottom and left < right:
            for i in range(left, right): 
                spiral[top][i] = element
                element += 1
            top += 1
            for i in range(top, bottom): 
                spiral[i][right-1] = element
                element += 1
            right -= 1
            if not (top < bottom and left < right): return spiral
            for i in range(right-1, left-1, -1): 
                spiral[bottom-1][i] = element
                element += 1
            bottom -= 1
            for i in range(bottom-1, top-1, -1): 
                spiral[i][left] = element
                element += 1
            left += 1
        return spiral