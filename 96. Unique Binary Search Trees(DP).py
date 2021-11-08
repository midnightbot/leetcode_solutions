class Solution:
    def numTrees(self, n: int) -> int:
        
        if n==1:
            return 1
        elif n==2:
            return 2
        elif n==3:
            return 5
        dp = [0]*(n+1)
        dp[0] = 1
        dp[1] = 1
        dp[2] = 2
        dp[3] = 5
        
        for x in range(4,n+1):
            for y in range(1,x+1):
                dp[x]+=dp[y-1]*dp[x-y]
                
        return dp[n]
        
