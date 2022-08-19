class Solution: 
    def isPossible(self, nums: List[int]) -> bool:
        if len(nums) < 3: return False

        freqs = Counter(nums)
        tails = Counter()

        for num in nums:

            # if the number already has a place in a sequence
            if freqs[num] == 0:
                continue

            # if the number may be placed as a continuation of another sequence
            elif tails[num] > 0:
                tails[num] -= 1
                tails[num + 1] += 1

            # the number is not consecutive to a previous sequence
            # a new sequence must be created
            elif freqs[num + 1] > 0 and freqs[num + 2] > 0:
                freqs[num + 1] -= 1
                freqs[num + 2] -= 1
                tails[num + 3] += 1

            # if the number cannot continue a new sequence
            # and cannot begin a new sequence then the list
            # cannot be split
            else:
                return False
            freqs[num] -= 1

        return True