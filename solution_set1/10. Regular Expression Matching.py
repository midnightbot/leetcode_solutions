##ss
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        @cache
        def match(i,j):
            if j == len(p):
                return i == len(s)
            
            if j+1 < len(p) and p[j+1] in ["*"]:
                ans = match(i,j+2)
                if i < len(s) and (s[i]==p[j] or p[j] in ["."]):
                    ans = ans or match(i+1,j)
                    
                return ans
            
            
            if p[j] in ["."] or i < len(s) and s[i] == p[j]:
                return match(i+1,j+1)
            
            return False
        
        return match(0,0)
                
        
