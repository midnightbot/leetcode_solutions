class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        ans = 0
        current = prices[0]
        for x in range(len(prices)):
            current = min(current,prices[x])
            ans = max(ans, prices[x] - current)

        return ans
        
