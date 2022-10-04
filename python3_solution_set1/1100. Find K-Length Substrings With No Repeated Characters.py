class Solution:
    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:
        
        maps = {}
        
        if len(s) < k:
            return 0
        
        ans = 0
        keys = 0
        for x in range(k):
            if s[x] in maps:
                maps[s[x]]+=1
                
            else:
                keys+=1
                maps[s[x]] = 1
                
        if keys == k:
            ans+=1
            
        for x in range(0,len(s)-k):
            maps[s[x]]-=1
            
            if maps[s[x]] == 0:
                keys-=1
                maps.pop(s[x])
                
            if s[x+k] in maps:
                maps[s[x+k]]+=1
                
            else:
                keys+=1
                maps[s[x+k]] = 1
                
            
            
            if keys == k:
                ans+=1
                
        return ans
        
