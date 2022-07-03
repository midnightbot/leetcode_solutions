class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        maxs = 0
        temp = 0
        
        freqs = {}
        
        for x in range(len(s)):
            freqs[s[x]] = freqs.get(s[x],0) + 1
            maxs = max(maxs, freqs[s[x]])
            
            if temp - maxs < k:
                temp+=1
                
            else:
                freqs[s[x-temp]]-=1
                
        return temp
        
