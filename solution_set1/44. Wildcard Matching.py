##ss
##very similar to 10. Regular Expression Matching

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        if len(s) == 0 and p.count("*") == len(p):
            return True
        @cache
        def match(i,j):
            if j == len(p):
                return i == len(s)
            
            if p[j] in ["?"] or i < len(s) and s[i] == p[j]:
                return match(i+1,j+1)
            
            #ans = False
            if p[j] in ["*"]:
                return match(i,j+1) or (i < len(s) and match(i+1,j))
                
                return ans
            
            return False
            
            
            
            
        return match(0,0)
        
