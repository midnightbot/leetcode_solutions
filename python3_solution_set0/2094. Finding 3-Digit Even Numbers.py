##SS
##Simple Recursion
from numpy import *
class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        ans = set()
        self.combinations(digits,"",ans)
        
        return sorted(ans)
    def combinations(self,digits,strs,ans):
        #print(strs)
        if len(strs) == 0:
            for x in range(len(digits)):
                if digits[x] !=0:
                    strs = str(digits[x])
                    temp = digits.copy()
                    temp.pop(x)
                    #print(temp)
                    self.combinations(temp,strs,ans)
                    
        elif len(strs) == 1:
            #print(len(digits))
            #temp_s = strs 
            for x in range(len(digits)):
                #strs+=str(digits[x])
                temp = digits.copy()
                temp.pop(x)
                #print(temp)
                self.combinations(temp,strs+str(digits[x]),ans)
                #print(len(digits))
                
        elif len(strs) == 2:
            for x in range(len(digits)):
                if digits[x]%2==0:
                    #strs+=str(digits[x])
                    ans.add(int(strs+str(digits[x])))
                    
        return ans
        
