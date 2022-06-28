class Solution:
    def minDeletions(self, s: str) -> int:
        freq = sorted(Counter(s).values(), reverse=True)
        seen = {freq[0]}
        deletions = 0
        for f in freq[1:]:
            while f > 0 and f in seen:
                f -= 1
                deletions += 1
            if f > 0:
                seen.add(f)
        return deletions