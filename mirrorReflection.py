class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        while (not((p%2)or(q%2))):
            (p,q) = (p//2,q//2)
        return(1+(q%2)-(p%2))