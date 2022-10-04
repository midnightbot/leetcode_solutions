class Solution:
    def numTilings(self, n: int) -> int:
        
        if n == 1:
            return 1
        elif n == 2:
            return 2
        
        dp = [0 for x in range(n+1)]
        
        dp[0] = 1
        dp[1] = 1
        dp[2] = 2
        
        sums = 3
        for x in range(3,n+1):
            #print(sums)
            dp[x] = 2 * dp[x-1] + dp[x-3]
            #sums+=dp[x]
        #print(dp)    
        return dp[n]%(pow(10,9)+7)
        
