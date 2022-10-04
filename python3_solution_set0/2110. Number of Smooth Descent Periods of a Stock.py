class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        
        dp = [0 for x in range(len(prices))]
        dp[0] = 1
        for x in range(1,len(dp)):
            if prices[x] == prices[x-1] - 1:
                dp[x] = 1 + dp[x-1]
                
            else:
                dp[x] = 1
                
        return sum(dp)
        
