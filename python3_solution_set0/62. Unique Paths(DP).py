class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        dp = [[0 for x in range(n)]for y in range(m)]
        
        for x in range(len(dp[0])):
            dp[0][x] = 1
            
        for y in range(len(dp)):
            dp[y][0] = 1
            
        for x in range(1,m):
            for y in range(1,n):
                dp[x][y] = dp[x-1][y]+dp[x][y-1]
                
        return dp[m-1][n-1]
