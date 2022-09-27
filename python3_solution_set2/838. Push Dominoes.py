class Solution:
    def pushDominoes(self, dom: str) -> str:
        
        while True:
            new_ans = dom.replace('R.L','|').replace('.L','LL').replace('R.','RR').replace('|','R.L')
            
            if new_ans == dom:
                break
                
            else:
                dom = new_ans
                
        return dom
        
