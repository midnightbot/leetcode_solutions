class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        n = len(triangle)
        
        dp = [[-1 for x in range(n+2)] for y in range(n)]
        
        for x in range(n):
            dp[x][0] = float('inf')
            dp[x][n+1] = float('inf')
            
        for x in range(1,n+1):
            dp[0][x] = triangle[n-1][x-1]
            
        #print(dp)
        for x in range(1,n):
            for y in range(1,n-x+1):
                #print(dp[x-1][y],dp[x-1][y-1],"a",triangle[n-1-x][y-1])
                dp[x][y] = min(dp[x-1][y],dp[x-1][y+1]) + triangle[n-1-x][y-1]
                
        return (dp[n-1][1])
