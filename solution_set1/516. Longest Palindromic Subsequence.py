##ss
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        
        dp = [[0 for x in range(len(s))] for y in range(len(s))]
        ans = 1
        for x in range(len(s)):
            dp[x][x] = 1
            
        for x in range(len(s)-1,-1,-1):
            for y in range(x+1,len(s)):
                if s[x] == s[y]:
                    dp[x][y] = 2 + dp[x+1][y-1]
                    ans = max(ans,dp[x][y])
                    
                else:
                    dp[x][y] = max(dp[x+1][y],dp[x][y-1])
                    ans = max(ans,dp[x][y])
         
        #self.print_dp(dp)
        return ans
    def print_dp(self,dp):
        
        for x in range(len(dp)):
            print(dp[x])
