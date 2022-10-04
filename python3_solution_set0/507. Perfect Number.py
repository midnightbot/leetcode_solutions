##ss
import math
class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        
        ans = set()
        for x in range(1,int(math.sqrt(num))+1):
            if num%x==0:
                ans.add(x)
                ans.add(num//x)
                
        ans.remove(num)
        #print(ans)
        return sum(ans) == num
            
        
