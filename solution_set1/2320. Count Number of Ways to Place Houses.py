class Solution:
    def countHousePlacements(self, n: int) -> int:
        
        mods = 10**9 + 7
        dp = [1] + [0]*(n+5)
        dp[-1] = 1
        
        for x in range(1,n+1):
            dp[x] = (dp[x-1] + dp[x-2]) % mods
            
        return (dp[n]*dp[n]) % mods
