from math import comb
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        
        dicts = {}
        for x in range(len(s)):
            if s[x] not in dicts.keys():
                dicts[s[x]] = 1
                
            else:
                dicts[s[x]]+=1
                
        #print(dicts)
        ans = 0
        for x in dicts.keys():
            ans+=comb(dicts[x],2)
        return ans + len(s)

        
