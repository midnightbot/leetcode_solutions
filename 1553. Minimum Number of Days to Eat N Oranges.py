##Solution 1(Time Limit Exceeded)
class Solution:
    def minDays(self, n: int) -> int:
        
        if n == 1:
            return 1
        
        elif n == 2:
            return 2
        dp = [0 for x in range(n+1)]
        
        dp[1] = 1
        
        dp[2] = 2
        
        for x in range(3,len(dp)):
            
            mins = float('inf')
            
            mins = min(mins, 1 + dp[x-1])
            
            if x%2 == 0:
                mins = min(mins,1 + dp[int(x/2)])
                
            if x%3 == 0:
                #print(x)
                mins = min(mins, 1 + dp[int(x/3)])
                
            dp[x] = mins
                
        return dp[len(dp)-1]
        
