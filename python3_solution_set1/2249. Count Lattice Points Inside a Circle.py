##ss
import math
class Solution:
    def countLatticePoints(self, circles: List[List[int]]) -> int:
        
        def count_points(x,y,r):
            result = set()
            
            for xcor in range(x-r,x+r+1):
                for ycor in range(y-r,y+r+1):
                    if math.dist([x,y], [xcor,ycor]) <= r:
                        result.add((xcor,ycor))
                        
            return result
        
        
        ans = set()
        
        for x,y,r in circles:
            ans = ans.union(count_points(x,y,r))
            
        return len(ans)
        
        
        
