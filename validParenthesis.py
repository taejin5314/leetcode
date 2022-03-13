class Solution:
    def isValid(self, s: str) -> bool:
        dict = { "{" : "}", "[" : "]", "(" : ")"}
        stack = []
        
        for elm in s:
            if elm in dict.keys():
                stack.append(elm)
            else:
                if not stack:
                    return False
                c = stack.pop()
                if dict[c] != elm:
                    return False
            
        if stack:
            return False
        return True