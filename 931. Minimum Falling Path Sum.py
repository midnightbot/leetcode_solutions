class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        
        n = len(matrix)
        
        dp = [[0 for x in range(n+2)] for y in range(n+2)]
        
        for x in range(n+2):
            dp[0][x] = float('inf')
            dp[n+1][x] = float('inf')
            
        for y in range(n):
            dp[1+y][0] = float('inf')
            dp[1+y][n+1] = float('inf')
            
        
        
        for x in range(1,n+1):
            dp[0][x] = matrix[n-1][x-1]
            
        #print(dp)
        
        for x in range(1,n+1):
            for y in range(1,n+1):
                dp[x][y] = min(dp[x-1][y-1],dp[x-1][y],dp[x-1][y+1]) + matrix[n-x-1][y-1]
                
        #print(dp)
        return min(dp[n-1])
