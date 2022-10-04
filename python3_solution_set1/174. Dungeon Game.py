class Solution:
    def calculateMinimumHP(self, dun: List[List[int]]) -> int:
        
        ## only right and down moves allowed
        ## find path that has min value at any given point 
        
        m = len(dun)
        n = len(dun[0])
        
        @cache
        def find_ans(x,y):
            if (x,y) in [(m-1,n), (m,n-1)]:
                return 1
            
            elif x == m or y == n:
                return float('inf')
            
            
            else:
                return max(min(find_ans(x+1,y), find_ans(x,y+1)) - dun[x][y],1)
            
            
        return find_ans(0,0)
            
            
