class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return nums[0]
        
        dp = [0 for x in range(len(nums))]
        
        
        dp[0] = nums[0]   
        dp[1] = max(nums[0],nums[1])
        
        for x in range(2,len(dp)):
            dp[x] = max(dp[x-1],nums[x]+dp[x-2])
            
        return dp[len(dp)-1]
