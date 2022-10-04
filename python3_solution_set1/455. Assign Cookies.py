##ss
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        ans = 0
        
        g = sorted(g)
        s = sorted(s)
        
        i = 0
        j = 0
        
        while i < len(g) and j < len(s):
            if g[i] <= s[j]:
                #ans+=1
                i+=1
                
            j+=1
            
        return i
                
        
