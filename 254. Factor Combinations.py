##ss
import math
class Solution:
    def getFactors(self, n: int) -> List[List[int]]:
        
        ans = set()
        curr = []
        self.facts(n,ans,curr,2)
        
        return ans
        
    def facts(self,n,ans,curr,start):
        #print(ans)
        if len(curr) > 0:
            #print("inside")
            curr.append(n)
            ans.add(tuple((curr)))
            #print(ans)
            curr.pop(len(curr)-1)
            
        for x in range(start,int(math.sqrt(n))+1):
            if n%x==0:
                curr.append(x)
                self.facts(n//x,ans,curr,x)
                curr.pop(len(curr)-1)
            
        
