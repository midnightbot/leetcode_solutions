class Solution:
    def twoEggDrop(self, n: int) -> int:
        
        dp = [0 for x in range(n+1)]
        
        if n == 1:
            return 1
        if n == 2:
            return 2
        ##dp[i] represents number of moves for floor i
        dp[0] = 0
        dp[1] = 1
        dp[2] = 2
        
        for x in range(3,len(dp)):
            mins = float('inf')
            for k in range(1,x+1):
                mins = min(mins,1 + max(k-1,dp[x-k]))
            
            dp[x] = mins
            
        return dp[len(dp)-1]
                
        
        
        
