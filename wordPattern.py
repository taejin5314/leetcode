class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        str = str.split(' ')
        return len(set(pattern)) == len(set(str)) == len(set(zip(pattern, str))) and len(pattern) == len(str)