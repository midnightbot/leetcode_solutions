##ss
class Solution:
    def uniquePathsWithObstacles(self, obs: List[List[int]]) -> int:
        
        dp = [[0 for x in range(len(obs[0]))] for y in range(len(obs))]
        
        
        for x in range(len(dp[0])):
            if obs[0][x] == 1:
                break
                
            else:
                dp[0][x] = 1
                
        for x in range(len(dp)):
            if obs[x][0] == 1:
                break
                
            else:
                dp[x][0] = 1
                
        for x in range(1,len(dp)):
            for y in range(1,len(dp[0])):
                if obs[x][y] == 1:
                    continue
                    
                else:
                    dp[x][y] = dp[x-1][y] + dp[x][y-1]
                    
        return dp[len(dp)-1][len(dp[0]) - 1]
