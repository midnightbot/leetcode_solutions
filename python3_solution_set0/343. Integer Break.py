##ss
class Solution:
    def integerBreak(self, n: int) -> int:
        
        ##dp[x] denote max product getting if we split 1...x
        
 
        if n == 2:
            return 1
        
        elif n == 3:
            return 2
        dp = [0 for x in range(n+1)]
        
        dp[0] = 0
        dp[1] = 1
        dp[2] = 1
        
        dp[3] = 2
        
        for x in range(4,len(dp)):
            maxs = -float('inf')
            for y in range(1,x//2+1):
                
                maxs = max(maxs, y * dp[x-y],y * (x-y))
                
            dp[x] = maxs
            
        return dp[n]
        
