class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        cnt = {}
        for x in sorted(arr): 
            cnt[x] = 1 + sum(cnt[xx]*cnt[x//xx] for xx in cnt if not x%xx and x//xx in cnt)
        return sum(cnt.values()) % 1_000_000_007