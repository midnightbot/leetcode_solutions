##ss
## Simple DP (Similar to sequence alignment problem)
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        dp = [[0 for x in range(len(word1)+1)] for y in range(len(word2)+1)]
        
        for x in range(1,len(dp[0])):
            dp[0][x] = x
            
        for x in range(1,len(dp)):
            dp[x][0] = x
            
            
        #self.print_dp(dp)
        
        for x in range(1,len(dp)):
            for y in range(1,len(dp[0])):
                if word2[x-1] == word1[y-1]:
                    dp[x][y] = dp[x-1][y-1]
                    
                else:
                    dp[x][y] = 1 + min(dp[x-1][y],dp[x][y-1])
        #print("********")
        #self.print_dp(dp)
        return dp[len(word2)][len(word1)]
        
    def print_dp(self,dp):
        for x in range(len(dp)):
            print(dp[x])
