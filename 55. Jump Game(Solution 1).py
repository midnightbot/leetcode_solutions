class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        dp = [0 for x in range(len(nums))]
        
        dp[len(dp)-1] = True
        
        if nums[0] >=len(nums):
            return True
        
        
        for x in range(len(nums)-2,-1,-1):
            for y in range((nums[x]+1)):
                if (y+x)<len(nums) and dp[x+y] == True:
                    dp[x] = True
                    break
                    
        if dp[0] == True:
            return True
        else:
            return False
        
        
        
##Dynamic Programming (Approach 1)
## explanation : ()
