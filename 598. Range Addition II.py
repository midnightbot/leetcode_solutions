##ss
class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        
        ##max element will be at (0,0)
        ## so we just have to count number of occurences of elem at (0,0)
        ## elem(0,0) = len(ops) as for every operation in ops (0,0) will be +1 its values
        ## we now just need to find all the points which are affected in every operation hence their value will also be equal to that of elem (0,0)
        
        if len(ops) == 0:
            return m*n
       
        
        min_x = float('inf')
        min_y = float('inf')
        
        for x in range(len(ops)):
            min_x = min(min_x,ops[x][0])
            min_y = min(min_y,ops[x][1])
            
        return min_x*min_y
                    
        
