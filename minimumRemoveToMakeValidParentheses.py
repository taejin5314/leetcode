class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        open = 0
        s = list(s)
        
        for i, c in enumerate(s):
            if c == '(': open += 1
            elif c == ')':
                if not open: s[i] = ""
                else: open -= 1
        
        for i in range(len(s)-1, -1, -1):
            if not open: break
            if s[i] == '(': s[i] = ""; open -= 1
        
        return "".join(s)