##ss
class Solution:
    def longestLine(self, mat: List[List[int]]) -> int:
        
        dp = [[[0,0,0,0] for x in range(len(mat[0]))] for y in range(len(mat))]
        
        ans = 0
        
        for x in range(len(mat)):
            for y in range(len(mat[0])):
                if mat[x][y] == 1:
                    dp[x][y][0] = dp[x][y-1][0] + 1 if y>0 else 1
                    dp[x][y][1] = dp[x-1][y][1]+1 if x>0 else 1
                    dp[x][y][2] = dp[x-1][y-1][2] + 1 if x>0 and y>0 else 1
                    dp[x][y][3] = dp[x-1][y+1][3] + 1 if x>0 and y < len(mat[0])-1 else 1
                    
                    ans = max(ans,max(dp[x][y]))
                    
        return ans
        
