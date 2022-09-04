class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        
        ## 10**9 ~ const * 2**30
        ## therefore max size of nice subarray is 30
        
        result = 1
        low = -1
        curr = 0
        
        for it, x in enumerate(nums):
            while (curr & x):
                low+=1
                curr ^= nums[low]
            curr |= x
            result = max(result, it - low )
        return result
        
