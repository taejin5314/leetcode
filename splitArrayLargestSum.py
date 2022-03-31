class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        prefixSum = []
        curSum = 0 
        for num in nums: 
            curSum += num
            prefixSum.append(curSum)
        self.prefixSum = prefixSum   
        memo = dict()
        minMax = self.helper(0, m-1, memo)
        return minMax
        
    def getSum(self, start: int, end: int) -> int: 
        res = self.prefixSum[end]
        res -= self.prefixSum[start-1] if start-1 >= 0 else 0 
        return res
    
    def helper(self, index: int, splits: int, memo: dict) -> int: 
        if splits == 0: 
            subarray = self.getSum(index, len(self.prefixSum)-1)
            return subarray
        
        key = (index, splits) 
        if key in memo: 
            return memo[key]
        
        minMax = float('inf')
        maxIndex = len(self.prefixSum)-splits
        for i in range (index, maxIndex): 
            subarray = self.getSum(index, i)
            maxLeftover = self.helper(i+1, splits-1, memo)
            maximum = max(subarray, maxLeftover) 
            minMax = min(minMax, maximum)
        memo[key] = minMax
        return minMax  