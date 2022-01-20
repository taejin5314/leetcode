class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        str = s.split(' ')
        return len(set(pattern)) == len(set(str)) == len(set(zip(pattern, str))) and len(pattern) == len(str)