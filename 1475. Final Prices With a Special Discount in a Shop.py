class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        ans = []
        
        for x in range(len(prices)):
            discount = 0
            for y in range(x+1, len(prices)):
                if prices[x]>=prices[y]:
                    discount = prices[y]
                    break
                    
            ans.append(prices[x]-discount)
            
        return ans
                
        
