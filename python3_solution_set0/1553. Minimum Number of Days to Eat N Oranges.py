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
## Solution 2
## Both Solution 1 and Solution 2 are conceptually same but use of cache makes it fast
class Solution:
    def minDays(self, n: int) -> int:
        a = self.cal_dp(n)
        return a
        
    @lru_cache(None)
    def cal_dp(self,n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        
        else:
            return min(1+self.cal_dp(n//2)+n%2,1+self.cal_dp(n//3)+n%3)
        
