class Solution:
    def appealSum(self, s: str) -> int:
        
        dp = [0 for x in range(len(s)+1)]
        
        prev = {chr(x):-1 for x in range(ord('a'),ord('z')+1)}
        
        for x in range(len(s)):
            dp[x] = dp[x-1] + (x - prev[s[x]])
            prev[s[x]] = x
            
        #print(dp)
        return sum(dp)
        
        
