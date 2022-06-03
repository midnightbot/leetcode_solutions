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
        
