##ss
class Solution:
    def maxA(self, n: int) -> int:
        
        ##simple dp
        
        ##dp[x] denote max number of A on screen after a moves
        if n == 1:
            return 1
        elif n == 2:
            return 2
        
        elif n == 3:
            return 3
        dp = [0 for x in range(n+1)]
        dp[0] = 0
        dp[1] = 1
        dp[2] = 2
        dp[3] = 3
        
        for x in range(4,len(dp)):
            temp = -float('inf')
            for y in range(3,x):
                temp = max(temp,dp[y]*(x-y-1))
                
            dp[x] = max(1+dp[x-1],temp)
        #print(dp)   
        return dp[n]
        
