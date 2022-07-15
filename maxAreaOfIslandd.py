class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        max_count = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    self.cur_count = 0
                    self.dfs(grid, i, j)

                    max_count = max(max_count, self.cur_count)
    
        return max_count

    def dfs(self, grid, row, col):
        self.cur_count += 1
        grid[row][col] = '#'

        if col > 0 and grid[row][col - 1] == 1:
            self.dfs(grid, row, col - 1)
    
        if col + 1 < len(grid[0]) and grid[row][col+1] == 1:
            self.dfs(grid, row, col + 1)

        if row > 0 and grid[row - 1][col] == 1:
            self.dfs(grid, row - 1, col)

        if row + 1 < len(grid) and grid[row + 1][col] == 1:
            self.dfs(grid, row + 1, col)