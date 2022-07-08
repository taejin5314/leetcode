class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        for i in range(m):
            if houses[i] != 0:
                cost[i] = [float('inf')]*n
                cost[i][houses[i]-1] = 0
        
        memo = {}
        
        def dfs(i, k, j):
            if i < 0: return 0
            if k == 0 or k > i+1: return float('inf')
            if i == 0: return cost[0][j]
            if (i, k, j) in memo: return memo[i, k, j]
                  
            res = min(dfs(i-1, k-1, c) + cost[i][j] for c in range(n) if c != j)
            res = min(res, dfs(i-1, k, j) + cost[i][j])
            memo[i, k, j] = res
            return res
        
        res = min(dfs(m-1, target, j) for j in range(n))
        return res if res != float('inf') else -1