##ss
class Solution:
    def checkString(self, s: str) -> bool:
        
        aindex = -1
        bindex = len(s) + 1
        
        for i in range(len(s)):
            if s[i] == "b":
                bindex = i
                break
                
        for j in range(len(s)-1,-1,-1):
            if s[j] == "a":
                aindex = j
                
                break
                
        
        
        
                
        return bindex > aindex
        
