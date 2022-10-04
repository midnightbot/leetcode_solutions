class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        
        ans = 0
        
        for x in range(1,len(prices)):
            if prices[x] > prices[x-1]:
                ans+=prices[x] - prices[x-1]
        return ans
            
            
        
