##ss
class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        
        if s1 == s2:
            return True
        
        diff = []
        
        for x in range(len(s1)):
            if s1[x]!=s2[x]:
                diff.append(x)
                
        if len(diff) >=3 or len(diff) == 1:
            return False
        
        elif len(diff) == 2:
            if s1[diff[0]] == s2[diff[1]] and s1[diff[1]] == s2[diff[0]]:
                return True
            
        return False
        
