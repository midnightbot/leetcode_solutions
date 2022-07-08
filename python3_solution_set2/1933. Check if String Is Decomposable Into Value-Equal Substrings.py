##ss
class Solution:
    def isDecomposable(self, s: str) -> bool:
        grps = []
        
        c = 1
        for x in range(1,len(s)):
            if s[x] == s[x-1]:
                c+=1
            else:
                grps.append(c)
                c = 1
                
        grps.append(c)
        
        d = 0
        markit = []
        for x in grps:
            if x%3!=0:
                d+=1
                markit.append(x)
                
        if d!=1:
            return False
        
        else:
            if markit[0]%3 == 2:
                return True
            
            return False
        
