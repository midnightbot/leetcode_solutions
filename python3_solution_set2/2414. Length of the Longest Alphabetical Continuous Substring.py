class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        
        ans = 1
        
        for x in range(len(s)):
            strs = s[x]
            for y in range(x+1,min(len(s), x+27)):
                if ord(s[y]) == ord(strs[-1]) + 1:
                    strs+=s[y]
                    
                else:
                    #print(strs)
                    ans = max(ans, len(strs))
                    break
                    
            
            ans = max(ans, len(strs))
        return ans
                
        
