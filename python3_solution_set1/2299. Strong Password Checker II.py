##ss
class Solution:
    def strongPasswordCheckerII(self, ps: str) -> bool:
        
        if len(ps) < 8:
            return False
        
        lower = 0
        upper = 0
        special = 0
        digit = 0
        
        for x in range(1,len(ps)):
            if ps[x] == ps[x-1]:
                return False
            
        for x in ps:
            if ord('A') <= ord(x) <= ord('Z'):
                upper+=1
                
            elif ord('a') <= ord(x) <= ord('z'):
                lower+=1
                
            elif ord('0') <= ord(x) <= ord('9'):
                digit+=1
                
            if x in "!@#$%^&*()-+":
                special+=1
                
                
        return lower>=1 and upper>=1 and special>=1 and digit>=1
