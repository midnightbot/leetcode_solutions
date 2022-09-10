class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ## same as Best Time to Buy and Sell Stock IV
        k = 2
        n = len(prices)
        
        if k==0 or n == 0:
            return 0
        
        buy = [float('inf') for x in range(k)]
        profit = [0 for x in range(k)]
        
        for x in prices:
            buy[0] = min(buy[0], x)
            profit[0] = max(profit[0], x - buy[0])
            
            for it in range(1,k):
                buy[it] = min(buy[it], x - profit[it-1])
                profit[it] = max(profit[it], x - buy[it])
                
        return profit[-1]
        
