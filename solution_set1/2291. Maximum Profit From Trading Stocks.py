class Solution:
    def maximumProfit(self, present: List[int], future: List[int], budget: int) -> int:
        
        ## a stcok will either be bought or not bought
        
        #self.ans = -1
        
        @cache
        def find_ans(indx,left):
            if left < 0 or indx == len(present):
                return 0
            
            else:
                temp = 0
                
                if present[indx] <= left:
                    temp = max(temp, future[indx] - present[indx] + find_ans(indx+1,left-present[indx]))
                    
                temp = max(temp, find_ans(indx+1,left))
                
                return temp
        
        
        return find_ans(0,budget)
        
## Solution 2
class Solution:
    def maximumProfit(self, present: List[int], future: List[int], budget: int) -> int:
        
        ## a stcok will either be bought or not bought
        
        #self.ans = -1
        
        dp = [0 for x in range(budget + 1)]
        
        for x in range(len(present)):
            
            if future[x] - present[x] <=0:
                continue
                
            for y in range(budget, present[x]-1,-1):
                dp[y] = max(dp[y], dp[y-present[x]] + future[x] - present[x])
                
        return dp[-1]
        
