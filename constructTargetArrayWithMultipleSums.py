class Solution:
    def isPossible(self, T: List[int]) -> bool:
        if len(T)==1:
            if T[0]==1: return True
            else: return False
        def update():
            idx = T.index(max(T))
            remSum = sum(T) - T[idx]
            if remSum < T[idx]:
                T[idx]= T[idx] % remSum
                if T[idx]==0: T[idx]=remSum
                return True
            else:
                return False
        while any(T[i] > 1 for i in range(len(T))):
            if not update(): return False
        return True 