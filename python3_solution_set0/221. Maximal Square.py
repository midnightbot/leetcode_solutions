##ss
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        
        dp = [[0 for x in range(len(matrix[0]) +1)] for y in range(len(matrix)+1)]
        
        
        
        ans = 0
        
        for x in range(1,len(dp)):
            for y in range(1,len(dp[0])):
                if matrix[x-1][y-1] == "1":
                    dp[x][y] = min(min(dp[x-1][y],dp[x][y-1]),dp[x-1][y-1])+1
                    ans = max(ans,dp[x][y])
                    
        return ans*ans
