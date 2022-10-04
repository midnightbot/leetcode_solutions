##ss
##Solution1 (Proper DP, but Time Limit Exceeded)
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        
        ##only one transaction at a time
        ## buy, sell ,keep it
        ## at time 'x' I either have share or not have share
        
        if len(prices) == 1:
            return 0
        elif len(prices) == 2:
            return prices[1] - prices[0] - fee if prices[1] - prices[0] - fee > 0 else 0
        dp = [0 for x in range(len(prices))]
        
        if prices[1] - prices[0] - fee > 0:
            dp[1] = prices[1] - prices[0] - fee
            
        
        
        for x in range(2, len(prices)):
            ans = -1
            
            for y in range(1,x):
                if prices[x] - prices[y] - fee > 0:
                    profit = prices[x] - prices[y] - fee + dp[y-1]
                    
                    if profit > ans:
                        ans = profit
                        
            dp[x] = max(dp[x-1],0,ans,prices[x] - prices[0] - fee)
                    
                    
        #print(dp)
        return dp[-1]

##Solution 2 (Accepted)
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        
        
        if len(prices) < 2:
            return 0
        
        profit = 0
        temp = prices[0]
        
        for x in range(1,len(prices)):
            
            if prices[x] < temp:
                temp = prices[x]
                
            elif prices[x] > temp + fee:
                profit+= prices[x] - temp - fee
                temp = prices[x] - fee
                
        return profit
        
