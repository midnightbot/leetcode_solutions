##ss
##simple dp
class Solution:
    def maxSumAfterOperation(self, nums: List[int]) -> int:
        
        ## nums[i] -> nums[i] ** 2 at only one pos
        ## max subarray sum
        
        
        ##subarray is continuous
        
        
        ##dp[x][y] max-subarray including elem at pos 'x'  y =0 not squared y =1 squared
        
        dp = [[-float('inf') for x in range(2)]for y in range(len(nums))]
        
        dp[0][0] = nums[0]
        dp[0][1] = nums[0] ** 2
        ans = max(dp[0][0],dp[0][1])
        
        for x in range(1,len(nums)):
            dp[x][0] = max(nums[x], dp[x-1][0] + nums[x])
            dp[x][1] = max(nums[x]**2, dp[x-1][0] + nums[x]**2, dp[x-1][1] + nums[x])
            ans = max(dp[x][0],dp[x][1],ans)
            
        #print(dp)
        return ans
