class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        
        superset_b = reduce(lambda x, y: x | y, map(Counter, words2))
        return [a for a in words1 if superset_b & Counter(a) == superset_b]