##ss
## Same as 159. Longest Substring with At Most Two Distinct Characters
class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        left = 0
        right = 0
        dicts = {}
        maxlen = 0
        
        while right < len(s):
            
            dicts[s[right]] = right
            
            if len(dicts.keys()) == k+1:
                indx = min(dicts.values())
                dicts.pop(s[indx],None)
                
                left = indx+1
                
            maxlen=max(maxlen,right-left+1)
                
            right+=1
        
        return maxlen
        
