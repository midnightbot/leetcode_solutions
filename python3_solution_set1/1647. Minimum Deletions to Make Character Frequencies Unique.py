##ss
import collections
class Solution:
    def minDeletions(self, s: str) -> int:
        
        c = 0
        comp = [0 for x in range(26)]
        
        for x in range(len(s)):
            comp[ord(s[x]) - ord('a')]+=1
         
        fmaps = {}
        maxs = max(comp)
        for z in range(maxs+1):
            fmaps[z] = []
            
        for x in range(len(comp)):
            if comp[x]!=0:
                fmaps[comp[x]].append(chr(x+ord('a')))
                
        #for x in range(len())
         
        #print(fmaps)
        for x in range(maxs,0,-1):
            if len(fmaps[x]) <= 1:
                continue
                
            else:
                temp = fmaps[x][1:]
                fmaps[x] = [fmaps[x][0]]
                
                for z in temp:
                    c+=1
                    fmaps[x-1].append(z)
                    
        return c
        
