class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        k = 4 
        
        s = sum(matchsticks)
        if s % k != 0:
            return False
        
        target = s // k 
        n = len(matchsticks)
        
        def dfs(m):
            
            stack = [(m, 0, {m}, matchsticks[m])]
            while stack:
                #print(stack)
                node, cnt, path, sums = stack.pop()
                
                
                if sums == target:
                    if cnt == k-1:
                        return True
                    for i in range(0, n):
                        if i not in path:
                            stack.append((i, cnt+1, path | {i}, matchsticks[i]))

                elif sums < target:
                    for i in range(node+1, n):
                        if i not in path:
                            stack.append((i, cnt, path | {i}, sums + matchsticks[i]))
                else: # sums > target
                    pass
            return False
        return dfs(0)