##ss
##simple comparison
class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        
        ##1 insertion, deletion or replacement is allowed
        
        if len(s) == 0 and len(t) == 0:
            return False
        
        elif (len(s) == 0 and len(t)==1) or (len(t)==0 and len(s)==1):
            return True
        
        i = 0
        j = 0
        
        while i<len(s) and j < len(t) and s[i] == t[j]:
            i+=1
            j+=1
          
        if i==len(s) and j == len(t):
            return False
        
        elif len(s) < len(t):
            return t[j+1:] == s[i:]
        
        elif len(s) > len(t):
            return s[i+1:] == t[j:]
        
        elif len(s) == len(t):
            return s[i+1:] == t[j+1:]
        
