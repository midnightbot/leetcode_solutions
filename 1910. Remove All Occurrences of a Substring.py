##ss
class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        
        var = True
        
        while var:
            
            inside = 0
            for x in range(len(s)-len(part)+1):
                if part == s[x:x+len(part)]:
                    inside+=1
                    s = s[0:x] + s[x+len(part):len(s)]
                    break
                    
            if inside == 0:
                var = False
                
        return s
                
        
