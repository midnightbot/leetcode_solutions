##ss
import math
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        
        a = 0
        while a**2 <= c:
            if sqrt(c-a**2) == int(sqrt(c-a**2)):
                return True
            
            a+=1
            
        return False
        #for x in range(math.sqrt(c)):
        #return False
            
        
