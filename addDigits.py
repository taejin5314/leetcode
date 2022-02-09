class Solution:
    def addDigits(self, num: int) -> int:
        i = sum([int(x) for x in str(num)])
        while i > 9:
            i = sum([int(x) for x in str(i)])
            
        return i