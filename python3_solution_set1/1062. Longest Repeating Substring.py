##ss
class Solution:
    def longestRepeatingSubstring(self, s: str) -> int:
        
        comb = set()
        ans = 0
        for x in range(len(s)):
            for y in range(x+1,len(s)+1):
                if s[x:y] in comb:
                    ans = max(ans, len(s[x:y]))
                    
                else:
                    comb.add(s[x:y])
                    
        return ans
     

        
