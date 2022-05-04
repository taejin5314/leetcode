class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        n_dict = defaultdict(int)
        count = 0
        for n in nums:
            if n == k-n and n in n_dict and n_dict[n] > 0:
                v = n_dict[n] + 1
                count += v//2
                n_dict[n] = 0 if v%2 == 0 else 1
            elif k-n in n_dict and n_dict[k-n] > 0:
                count += 1
                n_dict[k-n] -= 1
            else:
                n_dict[n] += 1    

        return count