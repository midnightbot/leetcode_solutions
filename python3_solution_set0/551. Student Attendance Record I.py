##ss
class Solution:
    def checkRecord(self, s: str) -> bool:
        
        acount = s.count('A')
        
        count = 0
        for x in range(len(s)):
            if s[x] == "L":
                count+=1
                
            if count>=3:
                return False
            
            elif s[x]!="L":
                count = 0
                
                
        return acount < 2
        
