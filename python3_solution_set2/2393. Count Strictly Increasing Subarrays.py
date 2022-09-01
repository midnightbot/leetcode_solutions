class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        ## simple dp
        n = len(nums)
        dp = [1 for x in range(n)]
        
        for x in range(1,n):
            if nums[x] > nums[x-1]:
                dp[x] = 1 + dp[x-1]
            else:
                dp[x] = 1
        return sum(dp)
                
        
