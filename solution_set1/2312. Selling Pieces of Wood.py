##ss
class Solution:
    def sellingWood(self, m: int, n: int, prices: List[List[int]]) -> int:
        
        ## simple dp
        
        ## if we cut a piece horizontally in size 'a'
        ## dp[w][h] = max(dp[w][h], dp[w][a] + dp[w][h-a])
        ## similary for vertical
        
        dp = [[0 for x in range(n+1)]for y in range(m+1)]
        
        for ht,wi,p in prices:
            dp[ht][wi] = p
            
        
        for x in range(1,m+1):
            for y in range(1,n+1):
                
                for a in range(1,x//2 + 1):
                    dp[x][y] = max(dp[x][y] , dp[x-a][y] + dp[a][y])
                    
                for b in range(1,y//2+1):
                    dp[x][y] = max(dp[x][y], dp[x][y-b] + dp[x][b])
                    
        return dp[-1][-1]
