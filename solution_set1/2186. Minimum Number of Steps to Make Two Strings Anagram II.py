##ss
class Solution:
    def minSteps(self, s: str, t: str) -> int:
        
        sdict = {}
        tdict = {}
        
        ans = 0
        total = 0
        for x in range(len(s)):
            sdict[s[x]]  = sdict.get(s[x],0) + 1
            total+=1
            
        for x in range(len(t)):
            if t[x] in sdict:
                sdict[t[x]]-=1
                total-=1
                if sdict[t[x]] == 0:
                    sdict.pop(t[x])
                    
            else:
                ans+=1
        return ans+total
        
