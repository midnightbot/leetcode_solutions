##ss
class Solution:
    def printVertically(self, s: str) -> List[str]:
        
        comp = s.split(" ")
        
        maxs = 0
        
        for x in range(len(comp)):
            maxs = max(maxs, len(comp[x]))
            
        for x in range(len(comp)):
            if len(comp[x])!=maxs:
                diff = maxs - len(comp[x])
                apd = ""
                for y in range(diff):
                    apd+=" "
                    
                comp[x]+=apd
                
        result = []
        
        for x in range(len(comp[0])):
            thisans = ""
            for y in range(len(comp)):
                
                thisans+=comp[y][x]
            
            thisans = thisans.rstrip()##to remove trailing spaces
            result.append(thisans)
            
        return result
        
