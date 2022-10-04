class Solution:
    def nthUglyNumber(self, n: int) -> int:
        
        ## 2,3,5 factors

        if n == 1:
            return 1
        dp = [0 for x in range(n)]
        d2 = 0
        d3 = 0
        d5 = 0
        
        dp[0] = 1
        
        for x in range(1,n):
            
            dp[x] = min(dp[d2]*2, dp[d3]*3,dp[d5]*5)
            
            if dp[x] == dp[d2]*2:
                d2+=1
                
            if dp[x] == dp[d3] * 3:
                d3+=1
                
            if dp[x] == dp[d5]*5:
                d5+=1
                
        return dp[-1]
            
        
        
        
        
