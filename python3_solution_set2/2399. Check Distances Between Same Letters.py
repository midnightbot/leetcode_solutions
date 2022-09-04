class Solution:
    def checkDistances(self, s: str, dist: List[int]) -> bool:
        
        g = {}
        for x in range(len(s)):
            if s[x] not in g:
                g[s[x]] = x
                
            else:
                g[s[x]] = x - g[s[x]] - 1
        
        for x in g:
            if g[x]!=dist[ord(x)-ord('a')]:
                return False
            
        return True
        
        
