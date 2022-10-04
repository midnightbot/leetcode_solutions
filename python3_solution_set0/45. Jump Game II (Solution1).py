class Solution:
    def jump(self, nums: List[int]) -> int:
        
        
        dp = [float('inf') for x in range(len(nums))]
        
        dp[len(nums)-1] = 0
        
        for x in range(len(nums)-2,-1,-1):
            mins =  float('inf')
            for y in range(x,min(x+nums[x]+1,len(nums))):
                if dp[y] < mins:
                    mins = 1 + dp[y]
                 
            dp[x] = mins
       
        return dp[0]
        
        
        
