##ss
class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        
        ## 0 left, 1 right
        
        for x in range(len(shift)):
            if shift[x][0] ==0:
                c = shift[x][1] % len(s)
                
                s = s[c:len(s)] + s[0:c]
                
                
            else:
                c = shift[x][1] % len(s)
                
                s = s[len(s)-c:len(s)] + s[0:len(s)-c]
                
                
        return s
        
