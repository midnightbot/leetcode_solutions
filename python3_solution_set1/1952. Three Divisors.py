##ss
import math
class Solution:
    def isThree(self, n: int) -> bool:
        
        ans = set()
        
        for x in range(1,int(math.sqrt(n))+1,1):
            
            if n%x==0:
                ans.add(x)
                ans.add(n//x)
                
        return len(ans) == 3
        
